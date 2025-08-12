---
title: Home
layout: default
---
<!-- ================= Hero: full-bleed video with overlay ================= -->
<div class="full-bleed hero-video">
  <video
    autoplay
    muted
    loop
    playsinline
    webkit-playsinline
    preload="metadata"
    poster="{{ '/assets/img/hero/poster.jpg' | relative_url }}"
  >
    <source src="{{ '/assets/video/hero.mp4' | relative_url }}" type="video/mp4">
  </video>

  <!-- Overlay (desktop / tablet) -->
  <div class="hero-overlay hero-overlay--desktop">
    <div class="hero-content">
      <div class="hero-box hero-centered">
        <p class="tagline">
          <span class="t-1">Four siblings, three sports, two parents — one dream: Milano–Cortina 2026 and beyond.</span>
          <span class="t-2">Follow the journey and rep the team. <strong>#TeamMacuga</strong></span>
        </p>
        <div class="hero-actions hero-actions--center">
          <a class="btn primary hero-btn" href="{{ '/shop/' | relative_url }}">Shop Merch</a>
          <a class="btn hero-btn"          href="{{ '/updates/#results' | relative_url }}">Latest Results</a>
          <a class="btn hero-btn"          href="{{ '/story/' | relative_url }}">Our Story</a>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Overlay (mobile-only, placed AFTER the video so it doesn’t cover it) -->
<div class="container hero-overlay--mobile">
  <div class="hero-box hero-centered">
    <p class="tagline">
      <span class="t-1">Four siblings, three sports, two parents — one dream: Milano–Cortina 2026 and beyond.</span>
      <span class="t-2">Follow the journey and rep the team. <strong>#TeamMacuga</strong></span>
    </p>
    <div class="hero-actions hero-actions--center">
      <a class="btn primary hero-btn" href="{{ '/shop/' | relative_url }}">Shop Merch</a>
      <a class="btn hero-btn"          href="{{ '/updates/#results' | relative_url }}">Latest Results</a>
      <a class="btn hero-btn"          href="{{ '/story/' | relative_url }}">Our Story</a>
    </div>
  </div>
</div>

<div class="section-gap lg"></div>

<!-- ================= Mission Statement ================= -->
<section id="mission" class="container">
  <div class="mission-card">
    <h2 class="section-title">Our Mission</h2>
    <p class="lead mission-copy">
      We compete as a family — pushing limits, lifting each other, and showing that grit, joy, and community
      can carry you from hometown hills to the world stage. Team Macuga exists to inspire the next generation,
      celebrate the people who help us get there, and race with heart in everything we do.
    </p>
    <div class="mission-actions">
      <a class="btn primary" href="{{ '/story/' | relative_url }}">Read More</a>
    </div>
  </div>
</section>

<div class="section-gap lg"></div>

<!-- ================= Family ================= -->
<section id="family" class="container">
  <h2 class="section-title">Team Macuga Members</h2>
  {% include athlete-grid.html %}
</section>

<script>
(function(){
  // Headshot rotator
  const HEAD_BASE = '{{ "/assets/img/headshots/" | relative_url }}';
  const counts = { lauren:4, alli:5, sam:4, daniel:3, amy:4, dan:4 };
  const photos = Array.from(document.querySelectorAll('.ath-photo'));
  let step = 1, PERIOD = 3500;

  function nextFrame(){
    step++;
    photos.forEach(img => {
      const slug = img.dataset.slug;
      const max  = counts[slug] || 5;
      const idx  = ((step - 1) % max) + 1;
      const url  = `${HEAD_BASE}${slug}-headshot-${idx}.jpg`;
      const pre = new Image();
      pre.onload = () => { img.src = url; img.style.opacity = 1; };
      pre.src = url;
    });
  }
  nextFrame(); setInterval(nextFrame, PERIOD);

  // Link member names to Story anchors
  document.querySelectorAll('.athlete-card').forEach(card=>{
    const slug = card.dataset.slug || card.querySelector('[data-slug]')?.dataset.slug;
    const nameEl = card.querySelector('h3, .name');
    if(slug && nameEl && !nameEl.querySelector('a')){
      const a = document.createElement('a');
      a.href = '{{ "/story/#bio-" | relative_url }}' + slug;
      a.textContent = nameEl.textContent.trim();
      nameEl.replaceChildren(a);
    }
  });
})();
</script>

<div class="section-gap lg"></div>

<!-- ================= About Summary (after the grid) ================= -->
<section class="container about-summary">
  <div class="about-wrap">
    <p>
      From the first turns to World Cup starts, our story has always been bigger than a podium.
      It’s about family miles in a van, small-town backing, early-morning training, and a belief
      that doing things the right way matters. We’re proud to wear our colors, to partner with brands
      who share our values, and to bring fans along for the ride — on snow and beyond.
    </p>
  </div>
</section>

<div class="section-gap xl"></div>

<section class="container">
  <h2 class="section-title">Featured Merch</h2>
  {% include merch-carousel.html %}
</section>

<div class="section-gap xl"></div>

<section class="container">
  <h2 class="section-title">Featured Collab</h2>
  <div class="card" style="display:flex;gap:16px;align-items:center">
    <img src="{{ '/assets/img/logo-mark-color.png' | relative_url }}" alt="" style="width:64px;height:64px">
    <div style="flex:1">
      <strong>Lauren Macuga × Pit Viper</strong>
      <p class="muted" style="margin:4px 0 0">Bold speed-inspired shades designed by Lauren.</p>
    </div>
    <a class="btn primary" href="#">Shop the collab</a>
  </div>
</section>

<div class="section-gap xl"></div>

<style>
  /* Solid, bright hero box (no transparency) */
  .hero-overlay--desktop{ position:absolute; inset:0; display:flex; align-items:flex-end; justify-content:center; padding:min(6vw,28px); }
  .hero-centered{ text-align:center; }
  .hero-box{
    background:#fff !important;            /* force solid white */
    color:var(--ink) !important;
    border:1px solid rgba(17,24,39,.08);
    border-radius:14px;
    padding: clamp(16px, 2.2vw, 24px);     /* more breathing room */
    box-shadow: 0 14px 34px rgba(0,0,0,.16);
  }
  .hero-box .tagline{ margin:0 0 12px; line-height:1.38; }
  .hero-box .tagline .t-1, .hero-box .tagline .t-2{ display:block; }
  .hero-actions{ display:flex; flex-wrap:wrap; gap:12px; justify-content:center; }
  .hero-btn{ padding:12px 18px; border-radius:14px; font-weight:700; min-width:220px; justify-content:center; }
  @media (max-width:560px){ .hero-btn{ width:100%; } }

  /* Mobile: overlay below video */
  .hero-overlay--mobile{ display:none; }
  @media (max-width:700px){
    .hero-overlay--desktop{ display:none; }
    .hero-overlay--mobile{ display:block; margin-top:10px; }
  }

  /* Text boxes: brighter + roomier */
  .mission-card,
  .about-summary .about-wrap{
    background:#fff;
    border:1px solid rgba(17,24,39,.08);
    border-radius:14px;
    padding: clamp(16px, 2.2vw, 24px);
    box-shadow: 0 12px 28px rgba(0,0,0,.12);
  }

  /* Section spacing helpers */
  .section-gap{ height:20px; }
  .section-gap.lg{ height:28px; }
  .section-gap.xl{ height:36px; }
  section.container + section.container{ margin-top:24px; }

  /* Keep “My Story” from wrapping */
  .ath-actions .btn,
  .family-card .actions .btn{ white-space:nowrap; min-width:110px; }
</style>
