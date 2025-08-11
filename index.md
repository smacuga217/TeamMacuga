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


<section id="family" class="container">
  <h2 class="section-title">Family</h2>
  {% include athlete-grid.html %}
</section>



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

