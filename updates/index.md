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

      {% assign slug = a.slug | default: name | slugify %}
      {% assign headshot = '/assets/img/headshots/' | append: slug | append: '-headshot-1.jpg' | relative_url %}

      <article class="card res-card">
        <header class="res-head">
          <img class="res-avatar" src="{{ headshot }}" alt="{{ name }}">
          <div class="res-meta">
            <h3 id="res-{{ name | slugify }}">{{ name }}</h3>
            {% if a.discipline %}<span class="pill role">{{ a.discipline }}</span>{% endif %}
          </div>
          {% if a.url %}
            <a class="btn primary sm" href="{{ a.url }}" target="_blank" rel="noopener">FIS Profile ↗</a>
          {% endif %}
        </header>

        <div class="res-wrap">
          {% if top3 and top3.size > 0 %}
            <table class="res">
              <thead>
                <tr><th>Date</th><th>Discipline</th><th>Race</th><th>Place</th><th>Pts</th></tr>
              </thead>
              <tbody>
                {% for r in top3 %}
                  {%- assign PR = r.place | upcase -%}

                  {%- comment -%} classify the place {%- endcomment -%}
                  {%- assign place_class = '' -%}
                  {%- if PR == '1' or PR == '1ST' or PR == '1.' -%}
                    {%- assign place_class = 'p1' -%}
                  {%- elsif PR == '2' or PR == '2ND' or PR == '2.' -%}
                    {%- assign place_class = 'p2' -%}
                  {%- elsif PR == '3' or PR == '3RD' or PR == '3.' -%}
                    {%- assign place_class = 'p3' -%}
                  {%- elsif PR == 'DNF' or PR == 'DNS' or PR == 'DSQ' -%}
                    {%- assign place_class = 'dnf' -%}
                  {%- else -%}
                    {%- assign p_num = r.place | plus: 0 -%}
                    {%- if p_num > 0 and p_num <= 10 -%}
                      {%- assign place_class = 'top10' -%}
                    {%- endif -%}
                  {%- endif -%}

                  {%- comment -%} normalize label to DSQ/DNF/DNS exactly {%- endcomment -%}
                  {%- assign place_label = r.place -%}
                  {%- if PR == 'DQ' or PR == 'DSQ' -%}{%- assign place_label = 'DSQ' -%}{%- endif -%}
                  {%- if PR == 'DNF' -%}{%- assign place_label = 'DNF' -%}{%- endif -%}
                  {%- if PR == 'DNS' -%}{%- assign place_label = 'DNS' -%}{%- endif -%}

                  {%- comment -%} tiny medal icon for podiums {%- endcomment -%}
                  {%- assign medal = '' -%}
                  {%- if place_class == 'p1' -%}{%- assign medal = '🥇' -%}
                  {%- elsif place_class == 'p2' -%}{%- assign medal = '🥈' -%}
                  {%- elsif place_class == 'p3' -%}{%- assign medal = '🥉' -%}{%- endif -%}

                  <tr>
                    <td data-label="Date">{{ r.date | date: "%b %-d, %Y" }}</td>
                    <td data-label="Discipline">{{ r.discipline }}</td>
                    <td data-label="Race">
                      {% if r.venue %}{{ r.venue }}{% endif %}
                      {% if r.nation %} <span class="muted">({{ r.nation }})</span>{% endif %}
                      {% if r.competition %} — <span class="muted">{{ r.competition }}</span>{% endif %}
                    </td>
                    <td class="place {{ place_class }}" data-label="Place">
                      <span class="place-badge">
                        {% if medal != '' %}<span class="medal" aria-hidden="true">{{ medal }}</span>{% endif %}
                        <span class="place-text">{{ place_label }}</span>
                      </span>
                    </td>
                    <td class="pts" data-label="Pts">
                      {% if r.points %}<span class="pts-chip">{{ r.points }}</span>{% endif %}
                    </td>
                  </tr>
                {% endfor %}
              </tbody>

            </table>
          {% else %}
            <p class="muted">No results added yet.</p>
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
    <h2 class="section-title">Latest from the fam</h2>

    <!-- Featured videos -->
    <div class="video-grid">
      <!-- Lauren — USSS highlight -->
      <article class="card video">
        <div class="video-16x9">
          <iframe
            src="https://www.youtube-nocookie.com/embed/WSZOawWPVcM"
            title="Lauren Macuga wins in St. Anton — U.S. Ski & Snowboard"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        <p class="cap"><strong>Lauren Macuga</strong> — St. Anton win highlights (U.S. Ski & Snowboard)</p>
      </article>

      <!-- Lauren — FIS highlight -->
      <article class="card video">
        <div class="video-16x9">
          <iframe
            src="https://www.youtube-nocookie.com/embed/H9GTHJitgkQ"
            title="Lauren Macuga — First win with style | FIS Alpine"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        <p class="cap"><strong>Lauren</strong> — “First win with style” (FIS Alpine)</p>
      </article>

      <!-- Lauren — quick interview -->
      <article class="card video">
        <div class="video-16x9">
          <iframe
            src="https://www.youtube-nocookie.com/embed/PRYqJTONbY8"
            title="FIS interviews: Lauren Macuga — Atomic Ski Fans"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        <p class="cap"><strong>Lauren</strong> — short post-race chat (Atomic Ski Fans)</p>
      </article>

      <!-- Sam — news feature -->
      <article class="card video">
        <div class="video-16x9">
          <iframe
            src="https://www.youtube-nocookie.com/embed/UB6V1z0dr_8"
            title="Utah Teens Representing United States In Ski Jump World Cup — FOX 13"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        <p class="cap"><strong>Sam Macuga</strong> — World Cup feature (FOX 13 News / USA Nordic)</p>
      </article>
    </div>

    <div class="section-gap"></div>

    <!-- Instagram picks -->
    <h3 class="section-title">From Instagram</h3>
    <div class="ig-grid">
      <!-- Lauren -->
      <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/Bqlb4OBgFS8/" data-instgrm-version="14"></blockquote>

      <!-- Alli -->
      <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/C8BAON1R_my/" data-instgrm-version="14"></blockquote>

      <!-- Sam -->
      <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/CeqqXl2o8om/" data-instgrm-version="14"></blockquote>

      <!-- Daniel -->
      <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/Cfb0D2IsJeW/" data-instgrm-version="14"></blockquote>
    </div>
  </div>


<style>
/* Tabs */
.tabs{ display:flex; gap:.5rem; margin:10px 0 16px; flex-wrap:wrap; }
.tab{ border:1px solid var(--border); border-radius:999px; padding:.5rem 1rem; background:#fff; cursor:pointer; font-weight:700; }
.tab.active{ background:linear-gradient(90deg,var(--brand),var(--navy)); color:#fff; border-color:transparent; }
.tabpanel{ margin-top:10px; }
.tabpanel.show{ display:block; }

/* =========================
   RESULTS — Polished look
   ========================= */
.res-card{ position:relative; overflow:hidden; }
.res-card::before{
  content:""; position:absolute; left:0; right:0; top:0; height:4px;
  background:linear-gradient(90deg,var(--brand),var(--navy));
}
.res-head{
  display:grid; grid-template-columns:auto 1fr auto; align-items:center; gap:12px; margin-bottom:8px;
}
.res-avatar{
  width:56px; height:56px; border-radius:50%;
  object-fit:cover; border:1px solid var(--border); background:#fff;
}
.res-meta h3{ margin:0; font-size:1.15rem; }
.pill.role{
  display:inline-block; margin-top:4px; padding:.25rem .6rem; border-radius:999px;
  background:#eef4ff; border:1px solid var(--border); color:#334155; font-size:.82rem; font-weight:700;
}
.btn.sm{ padding:.45rem .7rem; border-radius:10px; }

.res{ width:100%; border-collapse:separate; border-spacing:0; }
.res thead th{
  text-align:left; font-size:.8rem; text-transform:uppercase; letter-spacing:.05em;
  padding:.55rem .65rem; color:#475569;
  border-bottom:2px solid var(--border);
}
.res td{
  padding:.65rem .65rem; vertical-align:top; border-top:1px solid var(--border);
}
.res tbody tr:nth-child(odd){ background:linear-gradient(0deg,#0000,#0000), #fff; }
.res tbody tr:hover{ background:#f8fbff; }

/* Place badges (gold/silver/bronze/top10/DNF) */
.place-badge{
  display:inline-flex; align-items:center; justify-content:center;
  min-width:2.4ch; padding:.15rem .5rem; border-radius:999px; font-weight:800;
  border:1px solid var(--border); background:#fff;
}
.place.p1 .place-badge{ background:linear-gradient(90deg,#FFD269,#E6B94A); color:#5b4100; border-color:#e6c370; }
.place.p2 .place-badge{ background:linear-gradient(90deg,#E8EEF5,#C9D3E1); color:#2f3a49; border-color:#cfd7e4; }
.place.p3 .place-badge{ background:linear-gradient(90deg,#EAC0A2,#D49B78); color:#4b2d19; border-color:#e0b79c; }
.place.top10 .place-badge{ background:#f2f7ff; color:#1f3161; border-color:#dbe5fb; }
.place.dnf .place-badge{ background:#f8f8f8; color:#6b7280; border-color:#e5e7eb; text-decoration:line-through; }

/* Points chip */
.pts-chip{
  display:inline-block; padding:.2rem .55rem; border-radius:999px; font-weight:700;
  background:#eef8f1; color:#14532d; border:1px solid #d7efe0;
}

/* Mobile: turn rows into stacked cards */
@media (max-width:720px){
  .res thead{ display:none; }
  .res, .res tbody, .res tr, .res td{ display:block; width:100%; }
  .res tr{ border:1px solid var(--border); border-radius:12px; padding:.4rem; margin:.55rem 0; background:#fff; box-shadow:var(--shadow); }
  .res td{ border:none; border-top:0; padding:.4rem .5rem; }
  .res td::before{
    content: attr(data-label);
    display:block; font-size:.75rem; letter-spacing:.04em; text-transform:uppercase; color:#64748b; margin-bottom:.2rem;
  }
  .res td.place{ display:flex; justify-content:flex-start; }
}

/* ===== NEWS tab polish (kept from your version) ===== */
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
.source-pill{ padding:.2rem .5rem; border-radius:999px; background:#f2f5ff; color:#334155; font-size:.8rem; font-weight:600; border:1px solid var(--border); }
.news-date{ color:var(--muted); font-size:.9rem; }
.news-title{ margin:.35rem 0 0; line-height:1.3; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; }
.news-thumb{ margin-top:10px; width:100%; height:140px; background-size:cover; background-position:center; border-radius:10px; border:1px solid var(--border); }

#updates-root #tab-news .section-head { margin-bottom: 12px; }
body.theme-navy #updates-root #tab-news .section-kicker,
body.theme-navy #updates-root #tab-news .section-heading { color:#fff !important; }
#updates-root #tab-news .divider{ border:0; border-top:4px solid var(--divider,#0b1220); margin:6px 0; }
body.theme-navy #updates-root #tab-news .divider{ --divider:#fff; opacity:.9; }

/* Make sure names/labels stay dark inside cards even on navy theme */
#updates-root .res-card h3{ color:var(--ink) !important; }
#updates-root .res-card .muted{ color:var(--muted) !important; }

/* allow space for the medal icon inside the badge */
.place-badge{
  display:inline-flex; align-items:center; gap:.35rem;
  min-width:auto; padding:.15rem .55rem;
}
.place-badge .medal{ font-size:.9rem; line-height:1; transform:translateY(-.5px); }

/* keep DSQ/DNS/DNF readable (you already style .place.dnf) */
.place.dnf .place-badge{ text-decoration:line-through; }

/* Social tab layout */
.video-grid,
.ig-grid{
  display:grid;
  gap:16px;
  grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
}

/* 16:9 safe iframe wrapper */
.video-16x9{
  position:relative;
  padding-top:56.25%;
  border-radius:12px;
  overflow:hidden;
  background:#000;
  border:1px solid var(--border);
}
.video-16x9 iframe{
  position:absolute; inset:0;
  width:100%; height:100%; border:0;
}

.cap{ margin:.5rem 0 0; color:var(--muted); }
.cap strong{ color:var(--ink); }

/* Make sure cards stay dark-on-white inside the navy theme */
body.theme-navy #tab-social .card,
body.theme-navy #tab-social .card *{
  color: var(--ink);
}

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
    e.preventDefault();
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

<script async src="//www.instagram.com/embed.js"></script>

