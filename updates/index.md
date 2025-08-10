---
title: Updates
layout: default
---

<section class="container">
  <h1 class="section-title">Latest Results</h1>
  <p class="lead">Auto-pull from FIS coming later. For now, here are quick links and placeholders for recent finishes.</p>

  <div class="grid cols-2">
    {% for a in site.data.family %}
    {% if a.fis %}
    <article id="{{ a.slug }}" class="card family-card">
      <img src="{{ a.photo | default: '/assets/img/placeholders/person.png' | relative_url }}" alt="{{ a.name }}">
      <div>
        <h3>{{ a.name }}</h3>
        <p class="muted">{{ a.latest_result.event | default: 'Recent event' }} — <strong>{{ a.latest_result.place | default: '—' }}</strong></p>
        <div style="margin-top:8px;display:flex;gap:10px;flex-wrap:wrap">
          <a class="btn" target="_blank" rel="noopener" href="{{ a.fis }}">See on FIS</a>
          {% if a.results %}<a class="btn" href="{{ a.results | relative_url }}">Team results page</a>{% endif %}
        </div>
      </div>
    </article>
    {% endif %}
    {% endfor %}
  </div>
</section>
