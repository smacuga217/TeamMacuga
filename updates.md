---
layout: default
title: Updates
permalink: /updates/
---
{% include latest-results.html %}
<section class="container">
  <h2 class="section-title">News</h2>
  <ul class="listy">
    {% for n in site.data.news %}<li><span class="meta">{{ n.date }}</span> {{ n.title }}</li>{% endfor %}
  </ul>
</section>
