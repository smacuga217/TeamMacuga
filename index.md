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
      <div class="hero-box">
        <p class="tagline">
          Three sisters, one brother, two legendary parents — one dream: Milano–Cortina 2026 and beyond.
          Follow the journey and rep the team. <strong>#TeamMacuga</strong>
        </p>
        <div class="hero-actions">
          <a class="btn primary" href="{{ '/shop/' | relative_url }}">Shop Merch</a>
          <a class="btn"          href="{{ '/updates/#results' | relative_url }}">Latest Results</a>
          <a class="btn"          href="{{ '/story/' | relative_url }}">Our Story</a>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- ===================================================================== -->

<div class="section-gap"></div>  <!-- ← added spacer -->
<div class="section-gap"></div>  <!-- ← added spacer -->

<section id="family" class="container">
  <h2 class="section-title">Team Macuga Members</h2>
  {% include athlete-grid.html %}
</section>

<script>
/* Map of rotating headshots by slug */
const HEADSHOTS = {
  lauren: [
    '/assets/img/headshots/lauren-headshot-1.jpg',
    '/assets/img/headshots/lauren-headshot-2.jpg',
    '/assets/img/headshots/lauren-headshot-3.jpg',
    '/assets/img/headshots/lauren-headshot-4.jpg',
  ],
  alli: [
    '/assets/img/headshots/alli-headshot-1.jpg',
    '/assets/img/headshots/alli-headshot-2.jpg',
    '/assets/img/headshots/alli-headshot-3.jpg',
    '/assets/img/headshots/alli-headshot-4.jpg',
    '/assets/img/headshots/alli-headshot-5.jpg',
  ],
  sam: [
    '/assets/img/headshots/sam-headshot-1.jpg',
    '/assets/img/headshots/sam-headshot-2.jpg',
    '/assets/img/headshots/sam-headshot-3.jpg',
    '/assets/img/headshots/sam-headshot-4.jpg',
  ],
  daniel: [
    '/assets/img/headshots/daniel-headshot-1.jpg',
    '/assets/img/headshots/daniel-headshot-2.jpg',
    '/assets/img/headshots/daniel-headshot-3.jpg',
  ],
  amy: [
    '/assets/img/headshots/amy-headshot-2.jpg',
    '/assets/img/headshots/amy-headshot-3.jpg',
    '/assets/img/headshots/amy-headshot-4.jpg',
    '/assets/img/headshots/amy-headshot-5.jpg',
  ],
  dan: [
    '/assets/img/headshots/dan-headshot-1.jpg',
    '/assets/img/headshots/dan-headshot-2.jpg',
    '/assets/img/headshots/dan-headshot-3.jpg',
    '/assets/img/headshots/dan-headshot-4.jpg',
  ],
};

(function(){
  const cards = document.querySelectorAll('.family-card[data-slug]');
  const INTERVAL = 4000;

  // Preload images to reduce flicker
  Object.values(HEADSHOTS).flat().forEach(src => { const i = new Image(); i.src = src; });

  cards.forEach(card => {
    const slug = card.getAttribute('data-slug');
    const list = HEADSHOTS[slug];
    if (!list || list.length < 2) return;

    const img = card.querySelector('.media.headshot img');
    let idx = 0;

    setInterval(() => {
      idx = (idx + 1) % list.length;
      // quick fade swap
      img.style.opacity = 0;
      setTimeout(() => { img.src = list[idx]; img.style.opacity = 1; }, 120);
    }, INTERVAL);
  });
})();
</script>



<div class="section-gap"></div>  <!-- ← added spacer -->

<section class="container">
  <h2 class="section-title">Featured Merch</h2>
  {% include merch-carousel.html %}
</section>

<div class="section-gap"></div>  <!-- ← added spacer -->

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

<div class="section-gap"></div>  <!-- ← added spacer -->

