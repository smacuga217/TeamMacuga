---
title: Our Story
layout: default
---

<section class="container">
  <h1 class="section-title">Our Story</h1>
  <p class="lead">Team Macuga is a family-powered ski crew from Park City: three sisters (alpine, moguls, ski jumping), one younger brother in training, and two all-star parents keeping the show on the road.</p>
</section>

<section class="container">
  <h2 class="section-title">The Family</h2>
  {% include athlete-grid.html %}
</section>

<section class="container">
  <h2 class="section-title">Deep dive</h2>
  {% for a in site.data.family %}
  <article id="{{ a.slug }}" class="card" style="margin-bottom:16px">
    <div class="family-card">
      <img src="{{ a.photo | default: '/assets/img/placeholders/person.png' | relative_url }}" alt="{{ a.name }}">
      <div>
        <h3>{{ a.name }}</h3>
        <p>{{ a.bio | default: a.teaser }}</p>
        <div style="margin-top:8px;display:flex;gap:10px;flex-wrap:wrap">
          {% if a.fis %}<a class="btn" target="_blank" rel="noopener" href="{{ a.fis }}">See on FIS</a>{% endif %}
          {% if a.instagram %}<a class="btn" target="_blank" rel="noopener" href="{{ a.instagram }}">Instagram</a>{% endif %}
          {% if a.facebook %}<a class="btn" target="_blank" rel="noopener" href="{{ a.facebook }}">Facebook</a>{% endif %}
        </div>
      </div>
    </div>
  </article>
  {% endfor %}
</section>
