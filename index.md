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
          <span class="t-1">Three sisters, one brother, two legendary parents — one dream: Milano–Cortina 2026 and beyond.</span>
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
      <span class="t-1">Three sisters, one brother, two legendary parents — one dream: Milano–Cortina 2026 and beyond.</span>
      <span class="t-2">Follow the journey and rep the team. <strong>#TeamMacuga</strong></span>
    </p>
    <div class="hero-actions hero-actions--center">
      <a class="btn primary hero-btn" href="{{ '/shop/' | relative_url }}">Shop Merch</a>
      <a class="btn hero-btn"          href="{{ '/updates/#results' | relative_url }}">Latest Results</a>
      <a class="btn hero-btn"          href="{{ '/story/' | relative_url }}">Our Story</a>
    </div>
  </div>
</div>
<!-- ===================================================================== -->

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
  // ----- headshot rotator -----
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

  // ----- link each member name to Story bio anchor -----
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

<script>
(function(){
  // Arrow scroll for carousels
  const by = (sel, root=document) => Array.from(root.querySelectorAll(sel));
  const px = () => Math.ceil(document.querySelector('.tm-card')?.getBoundingClientRect().width || 280) + 16;

  by('.slider-btn').forEach(btn=>{
    const target = document.querySelector(btn.dataset.target);
    if(!target) return;
    const update = () => {
      btn.closest('section').querySelector('.prev').disabled = (target.scrollLeft <= 0);
      btn.closest('section').querySelector('.next').disabled =
        (Math.ceil(target.scrollLeft + target.clientWidth) >= target.scrollWidth);
    };
    btn.addEventListener('click', () => {
      target.scrollBy({ left: btn.classList.contains('next') ? px() : -px(), behavior:'smooth' });
      setTimeout(update, 300);
    });
    target.addEventListener('scroll', update, { passive:true });
    update();
  });

  // Prevent "#" links from jumping to top (legacy)
  document.querySelectorAll('.tm-card a[href="#"]').forEach(a=>{
    a.addEventListener('click', e => e.preventDefault());
  });
})();
</script>

<style>
  /* ----- brighter white cards sitewide ----- */
  .card,
  .mission-card,
  .about-summary .about-wrap,
  .hero-box{
    background:#fff !important;
    border:1px solid rgba(17,24,39,.08);
    box-shadow: 0 10px 28px rgba(0,0,0,.14);
  }

  /* ===== HERO ===== */
  .hero-overlay--desktop{ position:absolute; inset:0; display:flex; align-items:flex-end; justify-content:center; padding: min(6vw, 28px); }
  .hero-centered{ text-align:center; }
  .hero-box{ border-radius:14px; padding:14px 16px; color:var(--ink); }
  .hero-box .tagline{ margin: 0 0 12px; line-height:1.38; }
  .hero-box .tagline .t-1,
  .hero-box .tagline .t-2{ display:block; }
  .hero-actions{ display:flex; flex-wrap:wrap; gap:12px; justify-content:center; }
  .hero-btn{ padding:12px 18px; border-radius:14px; font-weight:700; min-width:220px; justify-content:center; }
  @media (max-width:560px){ .hero-btn{ width:100%; } }

  /* Mobile: don’t overlay the video — show the hero box below it */
  .hero-overlay--mobile{ display:none; }
  @media (max-width: 700px){
    .hero-overlay--desktop{ display:none; }
    .hero-overlay--mobile{ display:block; margin-top: 10px; }
  }

  /* Section spacing helpers */
  .section-gap{ height: 20px; }
  .section-gap.lg{ height: 28px; }
  .section-gap.xl{ height: 36px; }
  section.container + section.container{ margin-top: 24px; }

  /* ===== Featured Merch carousel: smaller cards + overlay badges + dots ===== */
  .tm-carousel{ --gap:14px; position:relative; overflow:hidden; }
  .tm-track{ display:flex; gap:var(--gap); overflow-x:auto; scroll-snap-type:x mandatory; padding-bottom: 6px; }
  .tm-card{ flex:0 0 260px; scroll-snap-align:start; background:#fff; border:1px solid var(--border); border-radius:14px; box-shadow: var(--shadow); }
  .tm-imgwrap{ position:relative; aspect-ratio:4/3; background:#f3f6ff; }
  .tm-imgwrap img{ width:100%; height:100%; object-fit:cover; display:block; }

  /* badge on image like shop */
  .m-badge,
  .tm-imgwrap .img-badge{
    position:absolute; left:10px; top:10px;
    padding:4px 10px; font-size:.75rem; font-weight:700; line-height:1;
    border-radius:999px; color:#fff; background: var(--brand);
    box-shadow:0 6px 16px rgba(0,0,0,.10); pointer-events:none; user-select:none;
  }
  .img-badge.collab{ background: linear-gradient(90deg, var(--brand), var(--navy)); }
  .img-badge.badge-new{ background: var(--brand); }       /* red */
  .img-badge.badge-bestseller{ background: var(--navy); } /* navy */

  .tm-meta{ display:flex; justify-content:space-between; align-items:center; padding:10px 12px; }
  .tm-name{ font-size:.95rem; font-weight:700; }
  .tm-price{ font-size:.92rem; color:#64748b; }

  /* arrows */
  .tm-arrow{
    position:absolute; top:50%; transform:translateY(-50%);
    border:0; width:38px; height:38px; border-radius:999px;
    background:#ffffff; box-shadow:0 4px 14px rgba(0,0,0,.12);
    cursor:pointer; display:grid; place-items:center;
  }
  .tm-arrow.prev{ left:6px; } .tm-arrow.next{ right:6px; }
  .tm-arrow:disabled{ opacity:.35; cursor:default; }

  /* dots */
  .tm-dots{ display:flex; gap:8px; justify-content:center; margin-top:10px; }
  .tm-dots button{ width:8px; height:8px; border-radius:999px; border:0; background:#c3c9db; cursor:pointer; }
  .tm-dots button[aria-current="true"]{ background: var(--brand); }

  /* ===== Family cards: keep “My Story” on one line and even heights ===== */
  .ath-actions .btn,
  .family-card .actions .btn{ white-space: nowrap; }
  .family-card .actions{ align-items:center; }
</style>
