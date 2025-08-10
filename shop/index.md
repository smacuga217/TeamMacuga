---
title: Shop
layout: default
---

<section class="container">
  <h1 class="section-title">Shop</h1>
  <p class="lead">Team Macuga merch and collaborations.</p>
</section>

<section class="container">
  <h2 class="section-title">Team Macuga Merch</h2>
  {% include merch-carousel.html %}
</section>

<section class="container">
  <h2 class="section-title">Collabs</h2>
  <div class="card" style="display:flex;gap:16px;align-items:center">
    <img src="{{ '/assets/img/logo-mark-color.png' | relative_url }}" alt="" style="width:64px;height:64px">
    <div style="flex:1">
      <strong>Lauren Macuga × Pit Viper</strong>
      <p class="muted" style="margin:4px 0 0">Speed-inspired shades designed by Lauren.</p>
    </div>
    <a class="btn primary" href="#">Shop</a>
  </div>
</section>
