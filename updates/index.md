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
    {% assign news = site.data.news | sort: 'date' | reverse %}
    {% if news and news.size > 0 %}
      {% assign current_year = "" %}
      {% for n in news %}
        {% assign y = n.date | date: "%Y" %}

        {% if y != current_year %}
          {% unless forloop.first %}</div>{% endunless %}
          <h3 class="news-year">{{ y }}</h3>
          <div class="grid news-grid">
          {% assign current_year = y %}
        {% endif %}

        <a class="news-card" href="{{ n.link }}" target="_blank" rel="noopener">
          <div class="news-eyebrow">
            <img class="news-ico"
                src="https://www.google.com/s2/favicons?domain={{ n.link | uri_escape }}&sz=64"
                alt="" loading="lazy">
            <span class="news-source">{{ n.source }}</span>
            <span aria-hidden="true">•</span>
            <time class="news-date" datetime="{{ n.date }}">{{ n.date | date: "%b %-d, %Y" }}</time>
          </div>

          <h4 class="news-title">{{ n.title }}</h4>

          {% if n.image %}
            <div class="news-thumb" style="background-image:url('{{ n.image }}')"></div>
          {% endif %}
        </a>
      {% endfor %}
      </div>
    {% else %}
      <p class="muted">News will appear after the first daily fetch runs.</p>
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

/* News layout */
.news-year{ margin: 18px 0 8px; font-size: 1.1rem; opacity:.9; }
.news-grid{ grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }

/* Press card */
.news-card{
  position: relative;
  display: block;
  padding: 14px 16px;
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 14px;
  box-shadow: var(--shadow);
  overflow: hidden;
  transition: transform .12s ease, box-shadow .12s ease;
}
.news-card::before{
  content:"";
  position:absolute; left:0; top:0; bottom:0; width:6px;
  background: linear-gradient(180deg, var(--brand), var(--navy));
  border-top-left-radius:14px; border-bottom-left-radius:14px;
}
.news-card:hover{ transform: translateY(-1px); box-shadow: 0 12px 30px rgba(0,0,0,.12); }

.news-eyebrow{
  display:flex; align-items:center; gap:.5rem;
  color: var(--muted); font-size: .92rem;
}
.news-ico{ width:16px; height:16px; border-radius:4px; }

.news-title{
  margin:.35rem 0 0;
  line-height:1.3;
  display:-webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow:hidden;
}

/* Optional tiny thumb (shows only if n.image exists) */
.news-thumb{
  margin-top:10px;
  width:100%; height:140px;
  background-size: cover; background-position: center;
  border-radius: 10px;
  border: 1px solid var(--border);
}


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
