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
(function(){
  const HEAD_BASE = '{{ "/assets/img/headshots/" | relative_url }}';
  const counts = { lauren:4, alli:5, sam:4, daniel:3, amy:4, dan:4 }; // default to 5 if missing
  const photos = Array.from(document.querySelectorAll('.ath-photo'));
  let step = 1;                   // global frame index
  const PERIOD = 3500;            // ms between swaps

  function nextFrame(){
    step++;
    photos.forEach(img => {
      const slug = img.dataset.slug;
      const max  = counts[slug] || 5;
      const idx  = ((step - 1) % max) + 1;
      const url  = `${HEAD_BASE}${slug}-headshot-${idx}.jpg`;

      // simple crossfade to avoid flash
      const pre = new Image();
      pre.onload = () => { img.src = url; img.style.opacity = 1; };
      pre.src = url;
    });
  }

  // kick off in sync
  nextFrame();
  setInterval(nextFrame, PERIOD);
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

