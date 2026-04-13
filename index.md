---
title: Home
layout: default
---
<!-- ================= Hero: full-bleed video with overlay ================= -->
<div class="full-bleed hero-video">
  <video id="heroVideo"
         playsinline
         muted
         loop
         preload="metadata"
         poster="{{ '/assets/img/hero/poster.jpg' | relative_url }}">
    <source data-src="{{ '/assets/video/hero.mp4' | relative_url }}" type="video/mp4">
  </video>

  <!-- Overlay (desktop / tablet) -->
  <div class="hero-overlay hero-overlay--desktop" aria-hidden="false">
    <div class="hero-content">
      <div class="hero-box hero-centered">
        <p class="tagline">
          <span class="t-1">Four siblings, three sports, two parents — one dream: the 2030 Winter Olympics and beyond.</span>
          <span class="t-2">Follow the journey and rep the team. <strong>#TeamMacuga</strong></span>
        </p>
        <div class="hero-actions hero-actions--center">
          <a class="btn primary hero-btn" href="{{ '/story/' | relative_url }}">How This Happened</a>
          <a class="btn primary hero-btn" href="{{ '/updates/#results' | relative_url }}">Latest Updates</a>
          <a class="btn primary hero-btn" href="{{ '/shop/' | relative_url }}">Rep the Team</a>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Overlay (mobile-only, placed AFTER the video so it doesn't cover it) -->
<div class="container hero-overlay--mobile">
  <div class="hero-box hero-centered">
    <p class="tagline">
      <span class="t-1">Four siblings, three sports, two parents — one dream: the 2030 Winter Olympics and beyond.</span>
      <span class="t-2">Follow the journey and rep the team. <strong>#TeamMacuga</strong></span>
    </p>
    <div class="hero-actions hero-actions--center">
      <a class="btn primary hero-btn" href="{{ '/story/' | relative_url }}">Our Story</a>
      <a class="btn primary hero-btn" href="{{ '/updates/#results' | relative_url }}">Latest Results</a>
      <a class="btn primary hero-btn" href="{{ '/shop/' | relative_url }}">Rep the Team</a>
    </div>
  </div>
</div>

<div class="section-gap lg"></div>

<!-- ================= Mission Statement ================= -->
<section id="mission" class="container">
  <div class="mission-card cardish">
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
  <h2 class="section-title">Meet the Team</h2>
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

<script>
  document.querySelectorAll('.athlete-card .actions .social, .family-card .actions .social')
    .forEach(row => {
      const n = row.querySelectorAll('.icon-btn').length;
      if (n) row.classList.add('icons-' + n);
    });
</script>

<div class="section-gap lg"></div>

<!-- ================= About Summary ================= -->
<section class="container about-summary">
  <div class="about-wrap cardish">
    <p>
      From the first turns to World Cup starts, our story has always been bigger than a podium.
      It's about family miles in a van, small-town backing, early-morning training, and a belief
      that doing things the right way matters. We're proud to wear our colors, to partner with brands
      who share our values, and to bring fans along for the ride — on snow and beyond.
    </p>
  </div>
</section>

<div class="section-gap xl"></div>

<!-- ================= Merch Callout ================= -->
<section class="container">
  <div class="merch-callout cardish" style="text-align:center; padding: clamp(24px, 4vw, 48px);">
    <h2 class="section-title">Rep the Team</h2>
    <p style="font-size:1rem; color:#555; max-width:480px; margin:0 auto 1.5rem; line-height:1.7;">
      Gear up and show your support. All Team Macuga merch is available now in our Shopify store.
    </p>
    <a class="btn primary" href="{{ '/shop/' | relative_url }}">Shop Now →</a>
  </div>
</section>

<div class="section-gap xl"></div>

<style>
  .full-bleed.hero-video{ position:relative; z-index:0; }
  .full-bleed.hero-video > video{
    position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0;
    display:block;
  }
  .hero-overlay--desktop{
    position:absolute; inset:0; z-index:1;
    display:flex; align-items:flex-end; justify-content:center; padding:min(6vw,28px);
  }
  .hero-centered{ text-align:center; }
  .hero-box{
    pointer-events:auto;
    background:#fff !important;
    color:var(--ink) !important;
    border:1px solid rgba(11,18,32,.10);
    border-radius:14px;
    padding: clamp(16px, 2.2vw, 24px);
    box-shadow: 0 14px 34px rgba(0,0,0,.16);
  }
  .hero-box .tagline{ margin:0 0 12px; line-height:1.38; }
  .hero-box .tagline .t-1, .hero-box .tagline .t-2{ display:block; }
  .hero-actions{ display:flex; flex-wrap:wrap; gap:12px; justify-content:center; }
  .hero-btn{ padding:12px 18px; border-radius:14px; font-weight:700; min-width:220px; justify-content:center; }
  @media (max-width:560px){ .hero-btn{ width:100%; } }

  .hero-overlay--mobile{ display:none; }
  @media (max-width:700px){
    .hero-overlay--desktop{ display:none; }
    .hero-overlay--mobile{ display:block; margin-top:10px; }
  }

  .cardish,
  .mission-card,
  .about-summary .about-wrap{
    background:#fff !important;
    border:1px solid rgba(11,18,32,.10) !important;
    border-radius:14px !important;
    padding: clamp(16px, 2.2vw, 24px) !important;
    box-shadow: 0 12px 28px rgba(0,0,0,.12) !important;
  }

  .section-gap{ height:20px; }
  .section-gap.lg{ height:28px; }
  .section-gap.xl{ height:36px; }
  section.container + section.container{ margin-top:24px; }

  .ath-actions .btn,
  .family-card .actions .btn{ white-space:nowrap; min-width:110px; }

  body.theme-navy #mission .section-title,
  body.theme-navy #mission h2.section-title{
    color: var(--ink) !important;
  }
  body.theme-navy #mission .section-title::after{
    opacity: 1;
  }
</style>