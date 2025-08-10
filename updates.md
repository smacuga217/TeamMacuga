---
layout: default
title: Updates
nav: updates
---

<section class="container">
  <h1>Updates</h1>
  <p class="muted">Latest results and news across Team Macuga.</p>

  <h2 class="section-title">Results</h2>
  <ul class="listy">
    {% for r in site.data.results %}
    <li>
      <span class="meta">{{ r.date }}</span>
      <strong>{{ r.athlete }}</strong> — {{ r.discipline }} — <em>{{ r.event }}</em>:
      <span class="chip">{{ r.result }}</span>
      {% if r.link %}<a href="{{ r.link }}" target="_blank" rel="noopener" class="pill">Details</a>{% endif %}
    </li>
    {% endfor %}
  </ul>

  <h2 class="section-title" style="margin-top:30px">News</h2>
  <ul class="listy">
    {% for n in site.data.news %}
    <li>
      <span class="meta">{{ n.date }}</span>
      {{ n.title }}
      {% if n.link %}<a href="{{ n.link }}" target="_blank" rel="noopener" class="pill">Read</a>{% endif %}
    </li>
    {% endfor %}
  </ul>
</section>
