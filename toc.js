document.addEventListener('DOMContentLoaded', function() {
    var toc = document.getElementById('toc');
    if (!toc) return;

    var headers = document.querySelectorAll('#readme h1');
    if (headers.length === 0) {
        headers = document.querySelectorAll('h1');
    }
    var headers = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
    if (headers.length === 0) return;

    var ul = toc.querySelector('ul');
    if (!ul) {
        ul = document.createElement('ul');
        toc.appendChild(ul);
    }
    var ul = document.createElement('ul');

    headers.forEach(function(header) {
        if (!header.id) {
            header.id = header.textContent.trim().toLowerCase().replace(/\s+/g, '-');
        }
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = '#' + header.id;
        a.textContent = header.textContent;
        li.appendChild(a);
        ul.appendChild(li);
    });

});

    toc.appendChild(ul);
});
