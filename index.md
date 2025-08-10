---
title: Home
layout: default
---

<!-- Full-bleed hero video -->
<div class="full-bleed hero-video">
  <video autoplay muted loop playsinline
         poster="{{ '/assets/img/hero/poster.jpg' | relative_url }}">
    <source src="{{ '/assets/video/hero.mp4' | relative_url }}" type="video/mp4">
  </video>
</div>

<!-- Logo + CTAs under the video -->
<div class="container">
  <img class="hero-logo" src="{{ '/assets/img/logo-full-color.png' | relative_url }}" alt="Team Macuga">

  <div class="hero-cta-row">
    <a class="btn primary" href="{{ '/shop/'    | relative_url }}">Shop Merch</a>
    <a class="btn"          href="{{ '/updates/#results' | relative_url }}">Latest Results</a>
    <a class="btn"          href="{{ '/story/'  | relative_url }}">Our Story</a>
  </div>
</div>


  <!-- Optional overlay text/button; delete if you want pure video -->
  <div class="hero-video__overlay container">
    <p class="hero-video__tag">TEAM MACUGA</p>
    <div class="hero-video__cta">
      <a class="btn primary" href="{{ '/shop/' | relative_url }}">Shop Merch</a>
      <a class="btn" href="{{ '/our story/' | relative_url }}">Our Story</a>
      <a class="btn" href="{{ '/updates/' | relative_url }}">Latest Results</a>
    </div>
  </div>
</section>


<section class="hero">
  <div class="container hero-grid">
    <div>
      <img class="hero-logo" src="{{ '/assets/img/logo-full-color.png' | relative_url }}" alt="Team Macuga">
      <p class="tagline">Three sisters, one brother, two legendary parents — one dream: Milano–Cortina 2026 and beyond. Follow the journey and rep the team. <strong>#TeamMacuga</strong></p>
    </div>

    <figure class="hero-rotator">
      <div class="frame" id="hero-rotator">
        <img class="slide active" src="{{ '/assets/img/placeholders/product.png' | relative_url }}" alt="Hero slide 1">
        <img class="slide" src="{{ '/assets/img/placeholders/product.png' | relative_url }}" alt="Hero slide 2">
        <img class="slide" src="{{ '/assets/img/placeholders/product.png' | relative_url }}" alt="Hero slide 3">
        <div class="dots"></div>
      </div>
    </figure>
  </div>
</section>

<script>
(function(){
  const wrap=document.getElementById('hero-rotator'); if(!wrap) return;
  const slides=[...wrap.querySelectorAll('.slide')], dots=wrap.querySelector('.dots');
  let i=0; slides.forEach((_,k)=>{const b=document.createElement('button');if(k===0)b.classList.add('active');b.onclick=()=>go(k);dots.appendChild(b);});
  function go(n){i=n;slides.forEach((s,k)=>s.classList.toggle('active',k===i));dots.querySelectorAll('button').forEach((d,k)=>d.classList.toggle('active',k===i));}
  setInterval(()=>go((i+1)%slides.length),5000);
})();
</script>

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

<section class="container">
  <h2 class="section-title">Featured Merch</h2>
  {% include merch-carousel.html %}
</section>

<section class="container">
  <h2 class="section-title">Family</h2>
  {% include athlete-grid.html %}
</section>
