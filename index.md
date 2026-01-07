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
<h1>{{ site.title }}</h1>
<p>{{ site.description }}</p>
<section id="readme">
{% capture readme_content %}{% include_relative home.md %}{% endcapture %}
{{ readme_content | markdownify }}
</section>
</main>
