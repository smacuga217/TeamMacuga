---
title: Our Story
layout: default
permalink: /story/
---

<!-- ================ Hero ================= -->
<header class="story-hero">
  <div class="story-hero-media">
    <img src="{{ '/assets/img/story/hero-wide.jpg' | relative_url }}" alt="" />
  </div>

  <div class="story-hero-overlay">
    <div class="container">
      <h1>Our Story</h1>
      <p class="sub">From a UCSD ski club to a family chasing snow and big dreams.</p>

      <div class="hero-cta">
        <a class="btn primary" href="#timeline">Read the Timeline</a>
        <a class="btn" href="#bios">Skip to Bios</a>
      </div>
    </div>
  </div>
</header>

<div class="section-gap"></div>

<!-- ================ Timeline ================= -->
<section id="timeline" class="container">
  <h2 class="section-title">The Macuga Timeline</h2>
  <p class="muted tl-intro">Highlights you can scroll — photos, video, and the moments that shaped the team.</p>

  <div class="tl">
    <div class="tl-line" aria-hidden="true"></div>

    {% assign items = site.data.timeline | sort: 'date' %}
    {% if items and items.size > 0 %}
      {% for it in items %}
        {% assign side = it.side %}
        {% if side == nil or side == '' %}
          {% if forloop.index0 | modulo: 2 == 0 %}
            {% assign side = 'left' %}
          {% else %}
            {% assign side = 'right' %}
          {% endif %}
        {% endif %}

        {% assign label = it.label %}
        {% if label == nil or label == '' %}
          {% if it.date %}
            {% assign label = it.date | date: "%Y" %}
          {% else %}
            {% assign label = "" %}
          {% endif %}
        {% endif %}

        <article class="tl-item {{ side }}">
          {% if label != "" or it.place %}
            <time class="tl-time">
              {{ label }}{% if it.place %} • {{ it.place }}{% endif %}
            </time>
          {% endif %}

          <div class="tl-card">

            {% if it.title %}
              <h3 class="tl-title">{{ it.title }}</h3>
            {% endif %}

            {% if it.media %}
              {% assign m = it.media | downcase %}
              <figure class="tl-media">
                {% if m contains '.mp4' or m contains '.webm' or m contains '.mov' %}
                  <video controls preload="metadata" {% if it.poster %}poster="{{ it.poster | relative_url }}"{% endif %}>
                    <source src="{{ it.media | relative_url }}" type="video/{% if m contains '.webm' %}webm{% else %}mp4{% endif %}">
                  </video>
                {% else %}
                  <img src="{{ it.media | relative_url }}" alt="{{ it.alt | default: it.title }}">
                {% endif %}
              </figure>
            {% endif %}

            {% if it.body %}
              <p>{{ it.body }}</p>
            {% endif %}

            {% if it.list and it.list.size > 0 %}
              <ul>
                {% for li in it.list %}<li>{{ li }}</li>{% endfor %}
              </ul>
            {% endif %}
          </div>

        </article>
      {% endfor %}
    {% else %}
      <p class="muted">Add timeline items in <code>/_data/timeline.yml</code> to see them here.</p>
    {% endif %}
  </div>
</section>

<div class="section-gap xl"></div>

<!-- ================ Bios ================= -->
<section id="bios" class="container">
  <h2 class="section-title">Team Macuga Bios</h2>
  <p class="muted">Click the button above to jump here anytime.</p>

  <div class="bios">
    <!-- Lauren -->
    <article id="bio-lauren" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/lauren-headshot-1.jpg' | relative_url }}" alt="Lauren Macuga" />
      <div class="bio-body">
        <h3>Lauren Macuga <span class="role">Alpine — Speed</span></h3>
        <p>Explosive in downhill and super-G, Lauren surged from U.S. development ranks to full-gas World Cup speed — highlighted by a <strong>first World Cup win (St. Anton, 2025)</strong>. Off-snow, she’s a go-to gear nerd and mountain-bike chaser.</p>
        <ul class="facts">
          <li>Strengths: DH / SG</li>
          <li>Career note: World Cup victory, Jan 12, 2025 (St. Anton)</li>
          <li>Hometown: Park City, UT</li>
          <li><a class="ext" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=228398" target="_blank" rel="noopener">FIS profile</a></li>
        </ul>
      </div>
    </article>

    <!-- Alli -->
    <article id="bio-alli" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/alli-headshot-1.jpg' | relative_url }}" alt="Alli Macuga" />
      <div class="bio-body">
        <h3>Alli Macuga <span class="role">Freeski — Moguls</span></h3>
        <p>Powerful turns, fearless airs. Alli’s NorAm titles and <strong>FIS Rookie of the Year (2023)</strong> led into World Cup podiums and a steady march toward the games.</p>
        <ul class="facts">
          <li>Strengths: Moguls / Duals</li>
          <li>Career note: FIS Rookie of the Year (2023); World Cup podiums (’24–’25)</li>
          <li>Hometown: Park City, UT</li>
          <li><a class="ext" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=FS&competitorid=220306" target="_blank" rel="noopener">FIS profile</a></li>
        </ul>
      </div>
    </article>

    <!-- Sam -->
    <article id="bio-sam" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/sam-headshot-1.jpg' | relative_url }}" alt="Sam Macuga" />
      <div class="bio-body">
        <h3>Sam Macuga <span class="role">Ski Jumping</span></h3>
        <p>Part of USA Nordic’s push in women’s jumping, Sam stacks World Cup and Summer GP experience across Europe while mentoring the next wave at home.</p>
        <ul class="facts">
          <li>Strengths: HS90–HS138</li>
          <li>Recent: WC/GP starts (Hinzenbach, Trondheim, Courchevel) in 2025</li>
          <li>Hometown: Park City, UT</li>
          <li><a class="ext" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=JP&competitorid=211435" target="_blank" rel="noopener">FIS profile</a></li>
        </ul>
      </div>
    </article>

    <!-- Daniel -->
    <article id="bio-daniel" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/daniel-headshot-1.jpg' | relative_url }}" alt="Daniel Macuga" />
      <div class="bio-body">
        <h3>Daniel Macuga <span class="role">Alpine — Tech</span></h3>
        <p>Tech specialist with a taste for long road trips and longer GS sets, Daniel mixes FIS racing with the world’s most patient ski-tuner energy.</p>
        <ul class="facts">
          <li>Strengths: GS / SL</li>
          <li>Recent: FIS starts across the West in 2025</li>
          <li><a class="ext" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=260517" target="_blank" rel="noopener">FIS profile</a></li>
        </ul>
      </div>
    </article>

    <!-- Parents -->
    <article id="bio-amy" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/amy-headshot-1.jpg' | relative_url }}" alt="Amy Macuga" />
      <div class="bio-body">
        <h3>Amy Macuga <span class="role">Mom — Team Ops</span></h3>
        <p>Logistics captain, snack strategist, and the quiet glue that keeps wheels (and edges) turning.</p>
      </div>
    </article>

    <article id="bio-dan" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/dan-headshot-1.jpg' | relative_url }}" alt="Dan Macuga" />
      <div class="bio-body">
        <h3>Dan Macuga <span class="role">Dad — Driver of Dreams</span></h3>
        <p>Van miles, wax tables, and life lessons — Dan turned a UCSD ski-club spark into a family tradition.</p>
      </div>
    </article>
  </div>
</section>

<!-- Floating back-to-top -->
<button id="storyBackTop" class="back-top-fab" aria-label="Back to top">↑</button>

<style>
/* Centering + bright cards */
.story-hero-overlay{ position:absolute; inset:0; display:flex; align-items:flex-end; justify-content:center; }
.story-hero-overlay .container{ width:100%; max-width:var(--container); margin:0 auto; padding:0 20px; }
.story-hero{ position:relative; }
.story-hero-media img{ width:100%; height: clamp(280px,55vh,520px); object-fit:cover; display:block; filter: saturate(1.05) contrast(1.02); }
.story-hero .sub{ color:#fff; opacity:.9; margin:.25rem 0 1rem; }
.story-hero h1{ color:#fff; margin:0; }
.hero-cta{ display:flex; gap:.5rem; flex-wrap:wrap; margin:.5rem 0 1rem; }

/* Timeline */
.tl-intro{ margin: 0 0 18px; }                 /* space under the intro line */
.tl{ position:relative; margin-top: 16px; padding-top: 18px; }  /* extra headroom for first date label */
.tl-line{ position:absolute; left:50%; top:0; bottom:0; width:3px; background:linear-gradient(var(--brand),var(--navy)); transform:translateX(-50%); border-radius:999px; }
.tl-item{ position:relative; margin:34px 0; display:grid; grid-template-columns: 1fr; }
.tl-item.left  .tl-card{ grid-column:1; margin-right: min(6%, 40px); }
.tl-item.right .tl-card{ grid-column:1; margin-left:  min(6%, 40px); }
.tl-time{ position:absolute; top:-8px; left:50%; transform:translate(-50%,-100%); font-size:.8rem; color:#64748b; background:#fff; padding:2px 8px; border-radius:999px; border:1px solid var(--border); }
.tl-card{
  background:#fff; border:1px solid var(--border); border-radius:14px;
  box-shadow:0 10px 28px rgba(0,0,0,.10);
  padding:12px 14px; max-width:600px;
}
.tl-media{ margin:0 0 .5rem; border-radius:10px; overflow:hidden; background:#eef3ff; border:1px solid var(--border); }
.tl-media img, .tl-media video{ width:100%; height:auto; display:block; }

/* Two-column feel on wide screens */
@media (min-width: 980px){
  .tl-item{ display:grid; grid-template-columns: 1fr 1fr; align-items:start; }
  .tl-item.left  .tl-card{ grid-column: 1; justify-self: end; }
  .tl-item.right .tl-card{ grid-column: 2; justify-self: start; }
}

/* Bios */
.bios{ display:grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap:16px; }
.bio{
  display:flex; gap:12px; background:#fff; border:1px solid var(--border);
  border-radius:14px; box-shadow:0 10px 28px rgba(0,0,0,.10); padding:14px;
}
.bio-img{ width:120px; height:120px; object-fit:cover; border-radius:12px; border:1px solid var(--border); }
.bio h3{ margin:.2rem 0 .1rem; }
.role{ color:#64748b; font-weight:600; font-size:.9rem; margin-left:.35rem; }
.facts{ display:grid; gap:4px; margin:.5rem 0 0; padding-left:1rem; }
.facts li{ margin:0; }
.ext{ color:var(--navy); text-decoration:underline; }
@media (max-width: 760px){ .bios{ grid-template-columns:1fr; } .bio{ flex-direction:row; } }

/* Floating back-to-top */
.back-top-fab{
  position: fixed; right: 20px; bottom: 22px;
  width: 44px; height: 44px; border-radius: 999px; border: 0;
  background: #ffffff; box-shadow: 0 8px 22px rgba(0,0,0,.16);
  color: #111827; font-size: 18px; font-weight: 700;
  display: grid; place-items: center;
  opacity: 0; transform: translateY(6px); pointer-events: none;
  transition: opacity .2s ease, transform .2s ease, box-shadow .2s ease;
  z-index: 2000;
}
.back-top-fab.show{ opacity: 1; transform: none; pointer-events: auto; }
.back-top-fab:hover{ box-shadow: 0 10px 28px rgba(0,0,0,.2); }

/* General spacing */
.section-gap{ height:24px; }
.section-gap.xl{ height:40px; }

/* =========================
   OUR STORY — READABILITY
   ========================= */

/* 1) "Skip to Bios" should be dark text on a white button */
.story-hero .btn:not(.primary){
  background: #fff;
  color: #0b1220 !important;
  border: 1px solid rgba(11,18,32,.15);
}
.story-hero .btn:not(.primary):hover{
  text-decoration: none;
  box-shadow: 0 8px 22px rgba(0,0,0,.12);
}

/* 2) On the navy theme, force dark tokens INSIDE white cards */
body.theme-navy .tl-card,
body.theme-navy .bio{
  --ink:   #0b1220;
  --muted: #384559;
  color: var(--ink);
}

/* Timeline card text: dark + readable */
body.theme-navy .tl-card h3,
body.theme-navy .tl-card p,
body.theme-navy .tl-card li,
body.theme-navy .tl-card a{
  color: var(--ink) !important;
}
body.theme-navy .tl-card .muted{
  color: var(--muted) !important;
}

/* Timeline date pill remains dark on white */
body.theme-navy .tl-time{
  color: #334155;
  background: #fff;
  border-color: var(--border);
}

/* 3) Bio cards: names and body copy must be dark */
body.theme-navy .bio h3,
body.theme-navy .bio p,
body.theme-navy .bio li,
body.theme-navy .bio a{
  color: var(--ink) !important;
}
body.theme-navy .bio .role{
  color: #475569 !important;  /* medium-dark for the subtitle */
}

/* 4) Make sure links inside white cards don’t become white */
body.theme-navy .tl-card a:not(.btn),
body.theme-navy .bio a:not(.btn){
  color: var(--ink) !important;
  text-decoration: underline;
}

</style>

<script>
(() => {
  // Floating Back-to-top
  const btn = document.getElementById('storyBackTop');
  const toggle = () => (window.scrollY > 400 ? btn.classList.add('show') : btn.classList.remove('show'));
  window.addEventListener('scroll', toggle, { passive: true });
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  toggle();
})();
</script>
