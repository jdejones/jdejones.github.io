// recent_commits.js
// Renders the latest commits for this GitHub Pages repo into #recent-commits.

document.addEventListener('DOMContentLoaded', () => {
  const mount = document.getElementById('recent-commits');
  if (!mount) return;

  const perPageAttr = mount.getAttribute('data-per-page');
  const perPage = Math.max(1, Math.min(10, Number(perPageAttr || 3) || 3));

  const repoInfo = getRepoInfo();
  if (!repoInfo) {
    mount.innerHTML = '<p>Unable to determine repository for recent commits.</p>';
    return;
  }

  const { owner, repo } = repoInfo;
  const apiUrl = `https://api.github.com/repos/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}/commits?per_page=${perPage}`;

  fetch(apiUrl, {
    headers: {
      'Accept': 'application/vnd.github+json'
    }
  })
    .then(async (res) => {
      if (!res.ok) {
        const text = await res.text().catch(() => '');
        throw new Error(`GitHub API error (${res.status}): ${text || res.statusText}`);
      }
      return res.json();
    })
    .then((commits) => renderCommits(mount, commits, owner, repo))
    .catch((err) => {
      // Keep this user-friendly; details still visible in DevTools.
      console.error(err);
      mount.innerHTML = '<p>Could not load recent commits right now.</p>';
    });
});

function getRepoInfo() {
  // Optional manual override:
  // <div id="recent-commits" data-owner="..." data-repo="...">
  const mount = document.getElementById('recent-commits');
  const owner = mount?.getAttribute('data-owner')?.trim();
  const repo = mount?.getAttribute('data-repo')?.trim();
  if (owner && repo) return { owner, repo };

  // Auto-detect for user/org GitHub Pages: {username}.github.io -> repo is {username}.github.io
  const host = (window.location.hostname || '').toLowerCase();
  const m = host.match(/^([a-z0-9-]+)\.github\.io$/);
  if (m) {
    const username = m[1];
    return { owner: username, repo: `${username}.github.io` };
  }

  // Fallback (this is your current repo name; safe default for local previews too)
  return { owner: 'jdejones', repo: 'jdejones.github.io' };
}

function renderCommits(mount, commits, owner, repo) {
  if (!Array.isArray(commits) || commits.length === 0) {
    mount.innerHTML = '<p>No commits found.</p>';
    return;
  }

  const ul = document.createElement('ul');
  ul.className = 'recent-commits-list';

  commits.forEach((c) => {
    const msg = (c?.commit?.message || '').split('\n')[0].trim();
    const sha = (c?.sha || '').slice(0, 7);
    const htmlUrl = c?.html_url || `https://github.com/${owner}/${repo}/commit/${c?.sha || ''}`;
    const dateStr = c?.commit?.author?.date || c?.commit?.committer?.date;
    const author = c?.commit?.author?.name || c?.commit?.committer?.name || '';

    const li = document.createElement('li');
    li.className = 'recent-commits-item';

    const a = document.createElement('a');
    a.href = htmlUrl;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.textContent = msg || sha || 'Commit';

    const meta = document.createElement('div');
    meta.className = 'recent-commits-meta';
    meta.textContent = formatMeta({ sha, author, dateStr });

    li.appendChild(a);
    li.appendChild(meta);
    ul.appendChild(li);
  });

  mount.innerHTML = '';
  mount.appendChild(ul);
}

function formatMeta({ sha, author, dateStr }) {
  const parts = [];
  if (sha) parts.push(sha);
  if (author) parts.push(author);
  if (dateStr) parts.push(formatDate(dateStr));
  return parts.join(' • ');
}

function formatDate(iso) {
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: '2-digit' });
}


