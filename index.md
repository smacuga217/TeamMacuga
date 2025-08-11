---
title: Home
layout: default
---
<!-- ================= Hero: full-bleed video with overlay ================= -->
<div class="full-bleed hero-video">
  <video autoplay muted loop playsinline
         poster="{{ '/assets/img/hero/poster.jpg' | relative_url }}">
    <source src="{{ '/assets/video/hero.mp4' | relative_url }}" type="video/mp4">
  </video>

  <!-- Overlay (tagline + buttons) -->
  <div class="hero-overlay">
    <div class="hero-content">
      <div class="hero-box hero-centered">
        <p class="tagline">
          Three sisters, one brother, two legendary parents — one dream: Milano–Cortina 2026 and beyond.
          Follow the journey and rep the team. <strong>#TeamMacuga</strong>
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

<!-- Rotating headshots + link names to Story bios -->
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
  // Works if your cards include a data-slug on either the card or the headshot image.
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
  const px = () => Math.ceil(document.querySelector('.product-card')?.getBoundingClientRect().width || 360) + 20;

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
  document.querySelectorAll('.product-card a[href="#"]').forEach(a=>{
    a.addEventListener('click', e => e.preventDefault());
  });
})();
</script>

<style>
  /* === Hero: center & enlarge buttons === */
  .hero-centered{ text-align:center; }
  .hero-actions{ display:flex; flex-wrap:wrap; gap:12px; }
  .hero-actions--center{ justify-content:center; }
  .hero-btn{
    padding: 12px 18px;            /* bigger */
    border-radius: 14px;
    font-weight: 700;
    min-width: 220px;              /* wider buttons */
    justify-content: center;
  }
  @media (max-width:560px){
    .hero-btn{ width:100%; }
  }

  /* Mission band */
  .mission-card{
    background:#fff;
    border:1px solid var(--border);
    border-radius:14px;
    box-shadow: var(--shadow);
    padding:18px;
    position:relative;
  }
  .mission-card::before{
    content:"";
    position:absolute; left:0; top:0; bottom:0; width:6px;
    border-top-left-radius:14px; border-bottom-left-radius:14px;
    background: linear-gradient(180deg, var(--brand), var(--navy));
  }
  .mission-copy{ margin:8px 0 0; }
  .mission-actions{ margin-top:12px; display:flex; justify-content:center; }

  /* About summary band */
  .about-summary .about-wrap{
    background: linear-gradient(180deg,#ffffff, #f7f9ff);
    border:1px solid var(--border);
    border-radius:14px;
    box-shadow: var(--shadow);
    padding:18px;
  }
  .about-summary p{
    margin:0;
    color: var(--muted);
    font-size: clamp(1rem, 1.05vw, 1.05rem);
    line-height: 1.55;
  }

  /* Section spacing helpers */
  .section-gap{ height: 20px; }
  .section-gap.lg{ height: 28px; }
  .section-gap.xl{ height: 36px; }
  /* In case a section pair is missing a gap div */
  section.container + section.container{ margin-top: 24px; }
  /* === Hero box: brighter white + dark text for clarity === */
  .hero-overlay::before{ background: none !important; } /* no dark scrim */
  .hero-box{
    background: rgba(255,255,255,.92) !important;
    color: var(--ink) !important;
    border: 1px solid rgba(11,18,32,.08);
    box-shadow: 0 10px 28px rgba(0,0,0,.16);
  }

  /* Force two-line tagline */
  .hero-box .tagline{ margin: 0 0 12px; line-height: 1.35; }
  .hero-box .tagline span{ display:block; }
  .hero-box .tagline .t-1{ font-weight: 700; }
  .hero-box .tagline .t-2{ margin-top: 2px; }

  /* Center + bigger hero buttons */
  .hero-actions{ justify-content: center; gap: 12px; }
  .hero-actions .btn{ padding: 12px 18px; border-radius: 14px; font-weight: 700; }
  .hero-actions .btn.primary{ color:#fff; }
  .hero-actions .btn{ min-width: 220px; justify-content: center; }
  @media (max-width:560px){ .hero-actions .btn{ width:100%; } }

  /* === Featured Merch: smaller cards === */
  /* show 4-up on large screens; keep 3-up on mid screens */
  @media (min-width: 1100px){
    .tm-slide{ flex: 0 0 calc(25% - var(--gap)*3/4); } /* 4 across */
  }
  /* tighten image height */
  .tm-imgwrap{ aspect-ratio: 4 / 3; } /* was 16/9; shorter cards */
  /* compact card body */
  .tm-meta{ padding: 10px 12px; }
  .tm-name{ font-size: .95rem; }
  .tm-price{ font-size: .92rem; }

</style>
