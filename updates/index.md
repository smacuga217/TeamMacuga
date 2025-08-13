---
layout: default
title: Updates
permalink: /updates/
---

<section id="updates-root" class="container">
  <h1 class="section-title">Updates</h1>

  <div class="tabs" role="tablist" aria-label="Updates tabs">
    <button class="tab active" data-tab="results" aria-selected="true">Results</button>
    <button class="tab" data-tab="news" aria-selected="false">News</button>
    <button class="tab" data-tab="social" aria-selected="false">Social</button>
  </div>

  <!-- Results -->
  <div id="tab-results" class="tabpanel show" role="tabpanel">
    {% assign athletes_src = site.data.athletes.athletes | default: site.data.athletes %}
    {% assign results_src   = site.data.results.athletes  | default: site.data.results  %}

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

      {% assign top3 = nil %}
      {% if res_obj and res_obj.results %}
        {% assign rows = res_obj.results | sort: "date" | reverse %}
        {% assign top3 = rows | slice: 0, 3 %}
      {% endif %}

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
    {% include news-highlights.html title="Featured" kicker="Hand-picked stories" %}
    <hr class="divider">
    {% include news-feed.html title="Latest Coverage" kicker="Updated daily" %}
  </div>

  <!-- Social -->
  <div id="tab-social" class="tabpanel" role="tabpanel" hidden>
    <div class="card">
      <p class="muted">Live social wall goes here.</p>
      {% comment %}
      Embed your social wall widget here (Walls.io / Curator / Elfsight / Juicer).
      {% endcomment %}
    </div>
  </div>
</section>

<style>
/* Tabs */
.tabs{ display:flex; gap:.5rem; margin:10px 0 16px; flex-wrap:wrap; }
.tab{ border:1px solid var(--border); border-radius:999px; padding:.4rem .9rem; background:#fff; cursor:pointer; }
.tab.active{ background:linear-gradient(90deg,var(--brand),var(--navy)); color:#fff; border-color:transparent; }
.tabpanel{ margin-top:10px; }
.tabpanel.show{ display:block; }

/* Results table */
.res-card .res-head{ display:flex; align-items:baseline; gap:.75rem; }
.res{ width:100%; border-collapse:collapse; }
.res th, .res td{ padding:.55rem .65rem; border-top:1px solid var(--border); vertical-align:top; }
.res-wrap .btn{ margin-top:10px; }

/* News */
.news-year{ margin:18px 0 8px; font-size:1.1rem; opacity:.9; }
.news-grid{ grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; }

.news-card{
  position:relative; display:block; padding:14px 16px;
  background:#fff; border:1px solid var(--border);
  border-radius:14px; box-shadow:var(--shadow); overflow:hidden;
  transition:transform .12s ease, box-shadow .12s ease;
}
.news-card::before{
  content:""; position:absolute; left:0; top:0; bottom:0; width:6px;
  background:linear-gradient(180deg,var(--brand),var(--navy));
  border-top-left-radius:14px; border-bottom-left-radius:14px;
}
.news-card:hover{ transform:translateY(-1px); box-shadow:0 12px 30px rgba(0,0,0,.12); }

.news-eyebrow{ display:flex; align-items:center; gap:.5rem; margin-bottom:.25rem; }
.source-pill{
  padding:.2rem .5rem; border-radius:999px;
  background:#f2f5ff; color:#334155; font-size:.8rem; font-weight:600;
  border:1px solid var(--border);
}
.news-date{ color:var(--muted); font-size:.9rem; }

.news-title{
  margin:.35rem 0 0; line-height:1.3;
  display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden;
}

.news-thumb{
  margin-top:10px; width:100%; height:140px;
  background-size:cover; background-position:center;
  border-radius:10px; border:1px solid var(--border);
}

/* ===== Updates page — News tab polish (scoped) ===== */
#updates-root #tab-news .section-head {
  /* a bit more space under the “Hand-picked stories / Updated daily” headings */
  margin-bottom: 12px;
}

/* keep section headings readable on the navy background */
body.theme-navy #updates-root #tab-news .section-kicker,
body.theme-navy #updates-root #tab-news .section-heading {
  color: #fff !important;
}

/* divider: thicker, white, and tighter spacing */
#updates-root #tab-news .divider {
  border: 0;
  border-top: 4px solid var(--divider, #0b1220);
  margin: 6px 0;            /* less space above/below */
}
body.theme-navy #updates-root #tab-news .divider {
  --divider: #ffffff;
  opacity: .9;
}

/* card content should be dark-on-white (names/titles not white) */
#updates-root #tab-news .news-card,
#updates-root #tab-news .news-card a,
#updates-root #tab-news .news-card .news-title,
#updates-root #tab-news .news-card .summary {
  color: var(--ink) !important;
}
#updates-root #tab-news .news-date { color: var(--muted) !important; }

/* also ensure Results tab names aren’t white */
#updates-root .res-card h3 { color: var(--ink) !important; }
#updates-root .res-card .muted { color: var(--muted) !important; }

/* optional: a touch more breathing room below each section block */
#updates-root #tab-news .news-highlights { margin-bottom: 10px; }
#updates-root #tab-news .news-feed      { margin-top: 10px; }

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
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
});
</script>

<script>
(function () {
  const VALID = ['results','news','social'];
  const tabs   = document.querySelectorAll('.tabs .tab');
  const panels = document.querySelectorAll('.tabpanel');

  function show(tab){
    const key = VALID.includes(tab) ? tab : 'results';
    tabs.forEach(b=>{
      const on = b.dataset.tab === key;
      b.classList.toggle('active', on);
      b.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    panels.forEach(p=>{
      const on = p.id === 'tab-' + key;
      p.toggleAttribute('hidden', !on);
      p.classList.toggle('show', on);
    });
  }

  // click -> update URL hash (so you can refresh/share)
  document.querySelector('.tabs').addEventListener('click', (e)=>{
    const t = e.target.closest('.tab');
    if(!t) return;
    e.preventDefault();                      // keep page in place
    const key = t.dataset.tab;
    if (location.hash !== '#'+key) history.pushState(null, '', '#'+key);
    show(key);
  });

  // on load
  const start = (location.hash || '#results').slice(1);
  show(VALID.includes(start) ? start : 'results');

  // back/forward buttons
  window.addEventListener('hashchange', ()=>{
    const cur = (location.hash || '#results').slice(1);
    show(VALID.includes(cur) ? cur : 'results');
  });
})();
</script>

