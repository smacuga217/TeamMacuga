---
title: Our Story
layout: default
permalink: /story/
---

<!-- =================== Hero =================== -->
<header class="story-hero full-bleed">
  <!-- Optional hero video (poster required) -->
  <video autoplay muted loop playsinline webkit-playsinline preload="metadata"
         poster="{{ '/assets/img/story/hero-poster.jpg' | relative_url }}">
    <source src="{{ '/assets/video/story-hero.mp4' | relative_url }}" type="video/mp4">
  </video>

  <div class="hero-overlay">
    <div class="container">
      <h1 class="story-title">Our Story</h1>
      <p class="story-sub">From a UCSD ski club to a family chasing snow and big dreams.</p>
      <div class="hero-cta-row">
        <a class="btn primary" href="#timeline">Read the Timeline</a>
        <a class="btn" href="#bios">Skip to Bios</a>
      </div>
    </div>
  </div>
</header>

<div class="section-gap"></div>

<!-- ========== Family quick nav (jump to bios) ========== -->
<nav class="container story-nav" aria-label="Family members">
  <span class="nav-label">Jump to:</span>
  <a class="chip" href="#bio-lauren">Lauren</a>
  <a class="chip" href="#bio-alli">Alli</a>
  <a class="chip" href="#bio-sam">Sam</a>
  <a class="chip" href="#bio-daniel">Daniel</a>
  <a class="chip" href="#bio-amy">Amy</a>
  <a class="chip" href="#bio-dan">Dan</a>
</nav>

<div class="section-gap"></div>

<!-- =================== TIMELINE =================== -->
<section id="timeline" class="container">
  <h2 class="section-title">The Macuga Timeline</h2>
  <p class="muted" style="margin:6px 0 18px">Highlights you can scroll — photos, video, and the moments that shaped the team.</p>

  <ol class="timeline" role="list">
    <!-- 1995 — Honeymoon + UCSD club -->
    <li class="tl-item">
      <div class="tl-media">
        <figure class="ph tl-ph">
          <!-- Replace with real image -->
          <img src="{{ '/assets/img/story/vail-1995.jpg' | relative_url }}" alt="Honeymoon in Vail, 1995" loading="lazy">
        </figure>
      </div>
      <article class="tl-card cardish">
        <div class="tl-eyebrow">1995 · Vail</div>
        <h3>It started with a ski club (and a honeymoon)</h3>
        <p>Amy &amp; Dan met through the <em>Radically Inclined Ski Club</em> at UC San Diego. The first big chapter: a honeymoon in Vail, and a shared decision that snow would always be part of the story.</p>
      </article>
      <span class="tl-dot" aria-hidden="true"></span>
    </li>

    <!-- Move to Park City -->
    <li class="tl-item">
      <div class="tl-media">
        <figure class="ph tl-ph">
          <img src="{{ '/assets/img/story/park-city-move.jpg' | relative_url }}" alt="Move to Park City" loading="lazy">
        </figure>
      </div>
      <article class="tl-card cardish">
        <div class="tl-eyebrow">1999 →</div>
        <h3>West to a ski town</h3>
        <p>Dan’s job offer opened the door to Park City. The goal was simple: share a love of skiing with the kids — and give them mountains for a backyard.</p>
        <p class="muted">Fun fact: all four were born in different states before the crew finally settled in Utah.</p>
      </article>
      <span class="tl-dot" aria-hidden="true"></span>
    </li>

    <!-- Snowbird video -->
    <li class="tl-item">
      <div class="tl-media">
        <div class="tl-video ph tl-ph">
          <!-- Replace with your family clip -->
          <video controls preload="metadata" poster="{{ '/assets/img/story/snowbird-kids-poster.jpg' | relative_url }}">
            <source src="{{ '/assets/video/snowbird-kids.mp4' | relative_url }}" type="video/mp4">
          </video>
        </div>
      </div>
      <article class="tl-card cardish">
        <div class="tl-eyebrow">Early 2000s · Snowbird</div>
        <h3>Skiing young</h3>
        <p>Long days, short skis, and big grins. The mountains were school, playground, and family room all at once.</p>
      </article>
      <span class="tl-dot" aria-hidden="true"></span>
    </li>

    <!-- Competitive path -->
    <li class="tl-item">
      <div class="tl-media">
        <figure class="ph tl-ph">
          <img src="{{ '/assets/img/story/first-races.jpg' | relative_url }}" alt="First races and comps" loading="lazy">
        </figure>
      </div>
      <article class="tl-card cardish">
        <div class="tl-eyebrow">Next chapters</div>
        <h3>From local races to world stages</h3>
        <ul class="story-list">
          <li>First gates, first bumps, first jump.</li>
          <li>State &amp; regional races → national teams.</li>
          <li>World Cup starts, World Champs, and an Olympic dream: Milano–Cortina 2026.</li>
        </ul>
      </article>
      <span class="tl-dot" aria-hidden="true"></span>
    </li>
  </ol>
</section>

<!-- =================== Pull-quote band =================== -->
<section class="story-quote">
  <div class="container">
    <blockquote>
      <p>“We just wanted to share the love of skiing with our kids. The rest grew from there.”</p>
      <cite>— Amy &amp; Dan</cite>
    </blockquote>
  </div>
</section>

<!-- =================== Bios =================== -->
<section id="bios" class="container">
  <h2 class="section-title">Team Macuga Bios</h2>
  <p class="muted">Click a name at the top to jump directly to any bio.</p>

  <div class="bios-grid">
    <article id="bio-lauren" class="bio-card">
      <div class="bio-media ph ph-1x1"></div>
      <div class="bio-body">
        <h3>Lauren Macuga</h3>
        <p class="muted role">Alpine Ski — Speed</p>
        <p>Short bio copy goes here.</p>
      </div>
    </article>

    <article id="bio-alli" class="bio-card">
      <div class="bio-media ph ph-1x1"></div>
      <div class="bio-body">
        <h3>Alli Macuga</h3>
        <p class="muted role">Freeski — Moguls</p>
        <p>Short bio copy goes here.</p>
      </div>
    </article>

    <article id="bio-sam" class="bio-card">
      <div class="bio-media ph ph-1x1"></div>
      <div class="bio-body">
        <h3>Sam Macuga</h3>
        <p class="muted role">Ski Jumping</p>
        <p>Short bio copy goes here.</p>
      </div>
    </article>

    <article id="bio-daniel" class="bio-card">
      <div class="bio-media ph ph-1x1"></div>
      <div class="bio-body">
        <h3>Daniel Macuga</h3>
        <p class="muted role">Alpine Ski — Tech</p>
        <p>Short bio copy goes here.</p>
      </div>
    </article>

    <article id="bio-amy" class="bio-card">
      <div class="bio-media ph ph-1x1"></div>
      <div class="bio-body">
        <h3>Amy Macuga</h3>
        <p class="muted role">Mom / Team Ops</p>
        <p>Short bio copy goes here.</p>
      </div>
    </article>

    <article id="bio-dan" class="bio-card">
      <div class="bio-media ph ph-1x1"></div>
      <div class="bio-body">
        <h3>Dan Macuga</h3>
        <p class="muted role">Dad / Logistics</p>
        <p>Short bio copy goes here.</p>
      </div>
    </article>
  </div>

  <div class="back-top" style="text-align:center;margin-top:14px">
    <a class="btn" href="#top">Back to top</a>
  </div>
</section>

<style>
/* Offsets for fixed nav + smooth anchors */
html{ scroll-behavior:smooth; }
[id]{ scroll-margin-top: 96px; }

/* -------- Hero -------- */
.story-hero{ position:relative; height:clamp(320px, 52vh, 560px); }
.story-hero > video{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }
.story-hero .hero-overlay{
  position:absolute; inset:0; display:flex; align-items:flex-end;
  background: linear-gradient(180deg, transparent 50%, rgba(0,0,0,.5));
}
.story-title{ color:#fff; margin:0 0 .35rem; }
.story-sub{ color:#fff; margin:0 0 1rem; max-width:60ch; }

/* -------- Centered nav chips -------- */
.story-nav{ display:flex; align-items:center; gap:.5rem; flex-wrap:wrap; justify-content:center; }
.story-nav .nav-label{ color:var(--muted); }
.chip{ border:1px solid var(--border); padding:.35rem .75rem; border-radius:999px; background:#fff; }

/* -------- Timeline -------- */
.timeline{
  position:relative; margin: 16px auto 0; padding:0; list-style:none;
  max-width: 1040px;
}
.timeline::before{
  content:""; position:absolute; top:0; bottom:0; left:50%; transform:translateX(-50%);
  width:3px; background: linear-gradient(180deg, var(--brand), var(--navy));
  border-radius: 999px;
}
.tl-item{
  position:relative;
  display:grid; grid-template-columns: 1fr 1fr; gap:18px; align-items:center;
  margin: 24px 0 40px;
}
.tl-item:nth-child(odd) .tl-card{ grid-column:1; justify-self:end; }
.tl-item:nth-child(odd) .tl-media{ grid-column:2; }
.tl-item:nth-child(even) .tl-card{ grid-column:2; justify-self:start; }
.tl-item:nth-child(even) .tl-media{ grid-column:1; }

.tl-dot{
  position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
  width:14px; height:14px; border-radius:999px; background:#fff;
  border:3px solid var(--brand); box-shadow:0 0 0 4px #fff;
}

.tl-card{ width: min(520px, 92%); }
.tl-eyebrow{ font-weight:700; color: var(--navy); margin-bottom:.25rem; }
.tl-media .tl-ph,
.tl-video{ border-radius:14px; overflow:hidden; background:#f3f6ff; border:1px solid var(--border); }
.tl-media img, .tl-video video{ width:100%; height:100%; object-fit:cover; display:block; }
.tl-ph{ aspect-ratio: 16/10; }

/* -------- Quote band -------- */
.story-quote{ background:#0f172a; color:#fff; padding:44px 0; margin:26px 0; }
.story-quote blockquote{ margin:0; font-size: clamp(1.1rem, 2vw, 1.4rem); line-height:1.45; }
.story-quote cite{ display:block; opacity:.8; margin-top:.5rem; font-style:normal; }

/* -------- Bios -------- */
.bios-grid{ display:grid; grid-template-columns: repeat(3,1fr); gap:16px; margin-top:12px; }
.bio-card{ display:flex; gap:12px; background:#fff; border:1px solid var(--border); border-radius:12px; padding:12px; }
.bio-media{ width:96px; aspect-ratio:1/1; border-radius:10px; background:#eef3ff; border:1px solid var(--border); }

/* -------- Cards look bright everywhere -------- */
.cardish{
  background:#fff; border:1px solid rgba(11,18,32,.10); border-radius:14px;
  box-shadow: 0 12px 28px rgba(0,0,0,.12); padding:16px;
}

/* -------- Responsive -------- */
@media (max-width: 1080px){
  .tl-card{ width: 100%; }
}
@media (max-width: 900px){
  .timeline::before{ left: 20px; transform:none; } /* line to the left */
  .tl-item{ grid-template-columns: 1fr; padding-left: 50px; }
  .tl-item .tl-media{ order:2; }
  .tl-item .tl-card{ order:1; justify-self:stretch; }
  .tl-dot{ left:20px; }
  .bios-grid{ grid-template-columns: repeat(2,1fr); }
}
@media (max-width: 640px){
  .bios-grid{ grid-template-columns: 1fr; }
}
  
/* ------- Lightweight placeholders if images missing ------- */
.ph{ background: repeating-linear-gradient(45deg,#f3f4f6 0 10px,#eceff3 10px 20px); }
</style>
