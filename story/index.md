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
          {% assign side = forloop.index0 | modulo: 2 == 0 | ternary: 'left', 'right' %}
        {% endif %}

        {% assign label = it.label %}
        {% if label == nil or label == '' %}
          {% assign label = it.date | date: "%Y" %}
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
              {% assign medias = it.media %}
              {% if medias.size == nil %}
                {% assign medias = medias | split: ',' %}
              {% endif %}

              {% for m in medias %}
                {% assign m = m | strip %}
                <figure class="tl-media">
                  {% if m contains '.mp4' or m contains '.webm' or m contains '.mov' %}
                    <video controls preload="metadata" {% if it.poster %}poster="{{ it.poster | relative_url }}"{% endif %}>
                      <source src="{{ m | relative_url }}" type="video/{% if m contains '.webm' %}webm{% else %}mp4{% endif %}">
                    </video>
                  {% else %}
                    <img src="{{ m | relative_url }}" alt="{{ m | split: '/' | last }}">
                  {% endif %}
                </figure>
              {% endfor %}
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



<!-- ================ Bios ================= -->
<section id="bios" class="container">
  <h2 class="section-title">Team Macuga Bios</h2>
  <p class="muted">Click the button above to jump here anytime.</p>

  <div class="bios">

    <!-- Lauren -->
    <article id="bio-lauren" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/lauren-headshot-1.jpg' | relative_url }}" alt="Lauren Macuga" />
      <div class="bio-body">
        <h3>Lauren Macuga <span class="role">Alpine Skiing — Speed</span></h3>
        <p>
          Lauren Macuga is an American alpine ski racer specializing in downhill and super‑G. 
          She started racing at age seven and steadily climbed through the U.S. Ski Team ranks, 
          earning her first World Cup win in super‑G at St. Anton in 2025 — becoming the youngest 
          American woman to win a World Cup speed race in nearly two decades. She also captured 
          bronze in super‑G at the 2025 World Championships and was ranked among the top World Cup 
          speed skiers that season. Her positivity, bucket‑hat style, and competitive spirit have 
          made her a standout on the circuit.
        </p>
        <ul class="facts">
          <li>Discipline: Downhill / Super‑G</li>
          <li><a class="ext" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=228398" target="_blank" rel="noopener">FIS Profile</a></li>
        </ul>
      </div>
    </article>

    <!-- Alli -->
    <article id="bio-alli" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/alli-headshot-1.jpg' | relative_url }}" alt="Alli Macuga" />
      <div class="bio-body">
        <h3>Alli Macuga <span class="role">Freeski — Moguls</span></h3>
        <p>
          Alli Macuga is a U.S. moguls skier known for her strong technique and competitive drive. 
          A former junior world champion and dual moguls team gold medalist, she made her first 
          World Cup start in 2022–23 and was named FIS Rookie of the Year. Alli has also earned 
          World Cup podium finishes and has been ranked among the world’s best moguls skiers.
        </p>
        <ul class="facts">
          <li>Disciplines: Moguls / Dual Moguls</li>
          <li><a class="ext" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=FS&competitorid=220306" target="_blank" rel="noopener">FIS Profile</a></li>
        </ul>
      </div>
    </article>

    <!-- Sam -->
    <article id="bio-sam" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/sam-headshot-1.jpg' | relative_url }}" alt="Sam Macuga" />
      <div class="bio-body">
        <h3>Sam Macuga <span class="role">Ski Jumping</span></h3>
        <p>
          Sam Macuga has been a member of the U.S. ski jumping team since 2019 and represents 
          the U.S. at World Cup and World Championship levels. The oldest of the Macuga siblings, 
          Sam balances training with academic pursuits while aiming toward her Olympic goal. She’s 
          competed in multiple World Championships and has been a consistent presence on the 
          international circuit. 
        </p>
        <ul class="facts">
          <li>Discipline: Ski Jumping</li>
          <li><a class="ext" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=JP&competitorid=211435" target="_blank" rel="noopener">FIS Profile</a></li>
        </ul>
      </div>
    </article>

    <!-- Daniel -->
    <article id="bio-daniel" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/daniel-headshot-1.jpg' | relative_url }}" alt="Daniel Macuga" />
      <div class="bio-body">
        <h3>Daniel Macuga <span class="role">Alpine Skiing — Tech</span></h3>
        <p>
          Daniel is an up‑and‑coming alpine ski racer competing in FIS events throughout the West. 
          With a focus on slalom and giant slalom, he continues to develop his skills and gain 
          experience in competitive racing. Daniel’s steady progress reflects his commitment and 
          passion for the sport. 
        </p>
        <ul class="facts">
          <li>Disciplines: Slalom / Giant Slalom / Super G / Downhill</li>
          <li><a class="ext" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=260517" target="_blank" rel="noopener">FIS Profile</a></li>
        </ul>
      </div>
    </article>

    <!-- Amy -->
    <article id="bio-amy" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/amy-headshot-1.jpg' | relative_url }}" alt="Amy Macuga" />
      <div class="bio-body">
        <h3>Amy Macuga <span class="role">Mom — Team Support</span></h3>
        <p>
          Amy makes sure the logistics, schedules, and daily details are taken care of so the 
          family can focus on training and racing. Her thoughtful organization and encouragement 
          are an essential part of Team Macuga’s foundation.
        </p>
      </div>
    </article>

    <!-- Dan -->
    <article id="bio-dan" class="bio">
      <img class="bio-img" src="{{ '/assets/img/headshots/dan-headshot-1.jpg' | relative_url }}" alt="Dan Macuga" />
      <div class="bio-body">
        <h3>Dan Macuga <span class="role">Dad — Family Support</span></h3>
        <p>
          Dan is the steady presence that keeps the family grounded and motivated. 
          He’s always there to support the kids at training and competitions, and his 
          encouragement helps keep the focus on growth, balance, and enjoying the ride.
        </p>
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
