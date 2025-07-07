// toc.js
document.addEventListener('DOMContentLoaded', function() {
    const toc = document.getElementById('toc');
    const readme = document.getElementById('readme');
    if (!toc || !readme) return;
  
    const ul = document.createElement('ul');
  
    // Optional: add Home link
    const homeLi = document.createElement('li');
    const homeA = document.createElement('a');
    homeA.href = 'index.html';
    homeA.textContent = 'Home';
    homeLi.appendChild(homeA);
    ul.appendChild(homeLi);
  
    // Find each first-level heading in the README section
    readme.querySelectorAll('h1').forEach(header => {
      // Give it an ID if missing
      if (!header.id) {
        header.id = header.textContent.trim()
          .toLowerCase()
          .replace(/\s+/g, '-');
      }
      // Build the list item
      const li = document.createElement('li');
      const a  = document.createElement('a');
      a.href = `#${header.id}`;
      a.textContent = header.textContent;
      li.appendChild(a);
      ul.appendChild(li);
    });
  
    toc.appendChild(ul);
  });
  