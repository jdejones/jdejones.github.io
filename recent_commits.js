// recent_commits.js
// Renders your latest (public) commits across all repositories into #recent-commits.
//
// Primary source: GitHub Search API (commits) filtered by author.
// Fallback: GitHub public events (PushEvent) for recent activity.

document.addEventListener('DOMContentLoaded', function () {
  var mount = document.getElementById('recent-commits-widget');
  if (!mount) return;

  var perPageAttr = mount.getAttribute('data-per-page');
  var perPage = clampInt(perPageAttr, 3, 1, 10);

  var username = getUsername(mount) || 'jdejones';

  renderLoading(mount);
  fetchLatestCommitsByAuthor(username, perPage)
    .then(function (items) {
      if (!items || !items.length) throw new Error('No commits returned.');
      renderCommitSearchResults(mount, items);
    })
    .catch(function (err) {
      // Fallback: public events (limited window, but useful if search is blocked)
      console.error(err);
      fetchLatestCommitsFromEvents(username, perPage)
        .then(function (commits) {
          if (!commits || !commits.length) throw new Error('No recent public commits found.');
          renderEventCommits(mount, commits);
        })
        .catch(function (err2) {
          console.error(err2);
          renderError(mount, 'Could not load recent commits right now (GitHub API).');
        });
    });
});

function fetchLatestCommitsByAuthor(username, perPage) {
  // Commit search may require a special Accept header in some environments.
  var q = encodeURIComponent('author:' + username);
  var url =
    'https://api.github.com/search/commits?q=' +
    q +
    '&sort=committer-date&order=desc&per_page=' +
    encodeURIComponent(String(perPage));

  return fetchJson(url, {
    Accept:
      'application/vnd.github.cloak-preview+json, application/vnd.github+json'
  }).then(function (json) {
    return json && json.items ? json.items : [];
  });
}

function fetchLatestCommitsFromEvents(username, perPage) {
  // Note: events are time-limited and only include public activity.
  var url =
    'https://api.github.com/users/' +
    encodeURIComponent(username) +
    '/events/public?per_page=30';

  return fetchJson(url, { Accept: 'application/vnd.github+json' }).then(function (
    events
  ) {
    var commits = [];
    if (!events || !events.length) return commits;

    for (var i = 0; i < events.length; i++) {
      var e = events[i];
      if (!e || e.type !== 'PushEvent') continue;
      if (!e.payload || !e.payload.commits || !e.repo) continue;

      for (var j = 0; j < e.payload.commits.length; j++) {
        var c = e.payload.commits[j];
        // Only include commits attributed to this user (best-effort; events are already user-scoped)
        commits.push({
          repo: e.repo.name,
          sha: c && c.sha ? c.sha : '',
          message: c && c.message ? c.message : '',
          created_at: e.created_at || ''
        });
        if (commits.length >= perPage) return commits;
      }
    }
    return commits.slice(0, perPage);
  });
}

function renderCommitSearchResults(mount, items) {
  var ul = document.createElement('ul');
  ul.className = 'recent-commits-list';

  for (var i = 0; i < items.length; i++) {
    var item = items[i] || {};
    var commit = item.commit || {};
    var msg = firstLine((commit.message || '').trim());
    var sha = (item.sha || '').slice(0, 7);
    var commitUrl = item.html_url || '';
    var repoFullName =
      item.repository && item.repository.full_name ? item.repository.full_name : '';
    var repoUrl =
      item.repository && item.repository.html_url ? item.repository.html_url : '';
    var dateStr =
      commit.committer && commit.committer.date
        ? commit.committer.date
        : commit.author && commit.author.date
          ? commit.author.date
          : '';

    ul.appendChild(
      buildCommitListItem({
        title: msg || sha || 'Commit',
        url: commitUrl,
        metaLeft: repoFullName,
        metaLeftUrl: repoUrl,
        metaRight: joinMeta([sha, formatDate(dateStr)])
      })
    );
  }

  mount.innerHTML = '';
  mount.appendChild(ul);
}

function renderEventCommits(mount, commits) {
  var ul = document.createElement('ul');
  ul.className = 'recent-commits-list';

  for (var i = 0; i < commits.length; i++) {
    var c = commits[i] || {};
    var repoFullName = c.repo || '';
    var sha = (c.sha || '').slice(0, 7);
    var msg = firstLine((c.message || '').trim());
    var url =
      repoFullName && c.sha
        ? 'https://github.com/' + repoFullName + '/commit/' + c.sha
        : '';
    var repoUrl = repoFullName ? 'https://github.com/' + repoFullName : '';

    ul.appendChild(
      buildCommitListItem({
        title: msg || sha || 'Commit',
        url: url,
        metaLeft: repoFullName,
        metaLeftUrl: repoUrl,
        metaRight: joinMeta([sha, formatDate(c.created_at || '')])
      })
    );
  }

  mount.innerHTML = '';
  mount.appendChild(ul);
}

function buildCommitListItem(opts) {
  var li = document.createElement('li');
  li.className = 'recent-commits-item';

  var a = document.createElement('a');
  a.className = 'recent-commits-title';
  a.href = opts.url || '#';
  a.target = '_blank';
  a.rel = 'noopener noreferrer';
  a.textContent = opts.title || 'Commit';
  li.appendChild(a);

  var meta = document.createElement('div');
  meta.className = 'recent-commits-meta';

  if (opts.metaLeft) {
    if (opts.metaLeftUrl) {
      var repoA = document.createElement('a');
      repoA.href = opts.metaLeftUrl;
      repoA.target = '_blank';
      repoA.rel = 'noopener noreferrer';
      repoA.textContent = opts.metaLeft;
      meta.appendChild(repoA);
    } else {
      var repoSpan = document.createElement('span');
      repoSpan.textContent = opts.metaLeft;
      meta.appendChild(repoSpan);
    }
  }

  if (opts.metaRight) {
    var right = document.createElement('span');
    right.className = 'recent-commits-meta-right';
    right.textContent = opts.metaRight;
    meta.appendChild(document.createTextNode(' • '));
    meta.appendChild(right);
  }

  li.appendChild(meta);
  return li;
}

function fetchJson(url, headersObj) {
  var headers = headersObj || {};
  return fetch(url, { headers: headers }).then(function (res) {
    if (!res.ok) {
      return res.text().then(function (txt) {
        throw new Error('GitHub API error (' + res.status + '): ' + (txt || res.statusText));
      });
    }
    return res.json();
  });
}

function getUsername(mount) {
  var attr = mount.getAttribute('data-user');
  if (attr && attr.trim()) return attr.trim();

  // Auto-detect for user/org GitHub Pages: {username}.github.io
  var host = (window.location.hostname || '').toLowerCase();
  var m = host.match(/^([a-z0-9-]+)\.github\.io$/);
  if (m && m[1]) return m[1];
  return '';
}

function clampInt(value, fallback, min, max) {
  var n = parseInt(value, 10);
  if (isNaN(n)) n = fallback;
  if (n < min) n = min;
  if (n > max) n = max;
  return n;
}

function firstLine(s) {
  var idx = s.indexOf('\n');
  return idx >= 0 ? s.slice(0, idx) : s;
}

function joinMeta(parts) {
  var out = [];
  for (var i = 0; i < parts.length; i++) {
    if (parts[i]) out.push(parts[i]);
  }
  return out.join(' • ');
}

function formatDate(iso) {
  if (!iso) return '';
  var d = new Date(iso);
  if (isNaN(d.getTime())) return iso;
  return d.toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'short',
    day: '2-digit'
  });
}

function renderLoading(mount) {
  mount.innerHTML = '<p>Loading recent commits…</p>';
}

function renderError(mount, msg) {
  mount.innerHTML = '<p>' + escapeHtml(msg) + '</p>';
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}


