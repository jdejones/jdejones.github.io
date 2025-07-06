---
title: Home
---

<link rel="stylesheet" href="style.css">
<script src="toc.js" defer></script>

<nav id="toc">
  <ul>
    <li><a href="index.html">Home</a></li>
  </ul>
</nav>

<main>
{% capture readme_content %}{% include_relative README.md %}{% endcapture %}
{{ readme_content | markdownify }}
=======
{% include_relative README.md %}
</main>
