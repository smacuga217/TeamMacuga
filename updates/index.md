---
layout: default
title: Updates
permalink: /updates/
---

<section class="container">
  <h1 class="section-title">Updates</h1>

  <div class="tabs" role="tablist" aria-label="Updates tabs">
    <button class="tab active" data-tab="results" aria-selected="true">Results</button>
    <button class="tab" data-tab="news" aria-selected="false">News</button>
    <button class="tab" data-tab="social" aria-selected="false">Social</button>
  </div>

  <!-- Results -->
  <div id="tab-results" class="tabpanel show" role="tabpanel">
    {% assign athletes_src = site.data.athletes.athletes | default: site.data.athletes %}
    {% assign results_src   = site.data.results.athletes | default: site.data.results %}

    {% for a in athletes_src %}
      {% assign name = a.name %}
      {% assign res_obj = results_src | where: "name", name | first %}
      {% if res_obj == nil %}
        {% assign nslug = name | slugify %}
        {% for r in results_src %}
          {% if r.name | slugify == nslug %}
            {% assign res_obj = r %}
          {% endif %}
        {% endfor %}
      {% endif %}

      {% assign rows = res_obj.results | sort: "date" | reverse %}
      {% assign top3 = rows | slice: 0, 3 %}

      <article class="card res-card">
        <header class="res-head">
          <h3 id="res-{{ name | slugify }}">{{ name }}</h3>
          <span class="muted">{{ a.discipline }}</span>
        </header>

        <div class="res-wrap">
          {% if top3 and top3.size > 0 %}
            <table class="res">
              <thead>
                <tr><th>Date</th><th>Discipline</th><th>Race</th><th>Place</th><th>Pts</th></tr>
              </thead>
              <tbody>
                {% for r in top3 %}
                <tr>
                  <td>{{ r.date | date: "%b %-d, %Y" }}</td>
                  <td>{{ r.discipline }}</td>
                  <td>
                    {% if r.venue %}{{ r.venue }}{% endif %}
                    {% if r.nation %} <span class="muted">({{ r.nation }})</span>{% endif %}
                    {% if r.competition %} — <span class="muted">{{ r.competition }}</span>{% endif %}
                  </td>
                  <td>{{ r.place }}</td>
                  <td>{{ r.points }}</td>
                </tr>
                {% endfor %}
              </tbody>
            </table>
          {% else %}
            <p class="muted">No results added yet.</p>
          {% endif %}

          {% if a.url %}
            <a class="btn" href="{{ a.url }}" target="_blank" rel="noopener">View on FIS</a>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>



  <!-- News -->
  <div id="tab-news" class="tabpanel" role="tabpanel" hidden>
    {% assign news_raw = site.data.news | default: site.data.news_json %}
    {% assign news = news_raw | sort: "ts" | reverse %}

    {% if news and news.size > 0 %}
      <div class="news-grid">
        {% for n in news %}
          <a class="news-card" href="{{ n.link }}" target="_blank" rel="noopener">
            <div class="news-media">
              {% if n.image %}
                <img src="{{ n.image }}" alt="" loading="lazy">
              {% else %}
                <div class="news-ph"></div>
              {% endif %}
            </div>
            <div class="news-body">
              <strong class="news-title">{{ n.title }}</strong>
              <span class="news-meta">
                {{ n.source }}
                {% if n.date %} • {{ n.date | date: "%b %-d, %Y" }}{% endif %}
              </span>
            </div>
          </a>
        {% endfor %}
      </div>
    {% else %}
      <p class="muted">News will appear after the next fetch.</p>
    {% endif %}
  </div>



  <!-- Social -->
  <div id="tab-social" class="tabpanel" role="tabpanel" hidden>
    <div class="card">
      <p class="muted">Live social wall goes here.</p>
      <!-- Replace the snippet below with your widget provider’s embed -->
      <!-- Example: Walls.io, Curator, Elfsight, Juicer, etc. -->
      <!--
      <script src="https://your-widget.js" async></script>
      <div data-your-widget="feed-id"></div>
      -->
    </div>
  </div>
</section>

<style>
.tabs{ display:flex; gap:.5rem; margin:10px 0 16px; flex-wrap:wrap; }
.tab{ border:1px solid var(--border); border-radius:999px; padding:.4rem .9rem; background:#fff; cursor:pointer; }
.tab.active{ background:linear-gradient(90deg,var(--brand),var(--navy)); color:#fff; border-color:transparent; }
.tabpanel{ margin-top:10px; }
.tabpanel.show{ display:block; }

.res-card .res-head{ display:flex; align-items:baseline; gap:.75rem; }
.res{ width:100%; border-collapse:collapse; }
.res th, .res td{ padding:.5rem .6rem; border-top:1px solid var(--border); vertical-align:top; }
.news-img{ width:100%; height:160px; object-fit:cover; border-radius:10px; }
.news-title{ display:block; margin:.4rem 0 .2rem; }
</style>

<style>
/* News grid + cards */
.news-grid{
  display:grid; gap:16px;
  grid-template-columns: repeat(12, 1fr);
}
.news-card{
  grid-column: span 4;
  display:flex; flex-direction:column; overflow:hidden;
  background:#fff; border:1px solid var(--border);
  border-radius:14px; box-shadow: var(--shadow);
  transition: transform .12s ease, box-shadow .12s ease;
}
.news-card:hover{ transform: translateY(-2px); box-shadow: 0 10px 28px rgba(0,0,0,.14); }

.news-media{ position:relative; aspect-ratio: 16/9; background:#f3f6ff; }
.news-media img{ width:100%; height:100%; object-fit:cover; display:block; }
.news-ph{ width:100%; height:100%;
  background: repeating-linear-gradient(45deg,#f5f7fb 0 12px,#eef2f9 12px 24px);
}

.news-body{ padding:12px 14px; display:grid; gap:6px; }
.news-title{ font-size:1.02rem; line-height:1.35; }
.news-meta{ color:#64748b; font-size:.92rem; }

/* responsive columns */
@media (max-width: 1100px){ .news-card{ grid-column: span 6; } }
@media (max-width: 640px){ .news-card{ grid-column: span 12; } }

</style>


<script>
document.querySelectorAll('.tabs .tab').forEach(btn=>{
  btn.addEventListener('click',()=>{
    document.querySelectorAll('.tabs .tab').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const id = btn.dataset.tab;
    document.querySelectorAll('.tabpanel').forEach(p=>{
      const show = p.id === 'tab-'+id;
      p.toggleAttribute('hidden', !show);
      p.classList.toggle('show', show);
    });
  });
});
</script>
