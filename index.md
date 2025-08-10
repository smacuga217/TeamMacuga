---
title: Home
layout: default
---
<!-- ================= Hero: full-bleed video ================= -->
<div class="full-bleed hero-video">
  <video autoplay muted loop playsinline
         poster="{{ '/assets/img/hero/poster.jpg' | relative_url }}">
    <source src="{{ '/assets/video/hero.mp4' | relative_url }}" type="video/mp4">
  </video>
</div>

<div class="container">

  <div class="hero-cta-row">
    <a class="btn primary" href="{{ '/shop/' | relative_url }}">Shop Merch</a>
    <a class="btn"          href="{{ '/updates/#results' | relative_url }}">Latest Results</a>
    <a class="btn"          href="{{ '/story/' | relative_url }}">Our Story</a>
  </div>
</div>
<!-- ========================================================== -->

<section class="hero">
  <div class="container hero-grid">
    <div>
      <p class="tagline">Three sisters, one brother, two legendary parents — one dream: Milano–Cortina 2026 and beyond. Follow the journey and rep the team. <strong>#TeamMacuga</strong></p>
    </div>
  </div>
</section>

<section class="container">
  <div class="hero-rotator">
    <div class="rotator">
      {% for p in site.data.gallery %}
      <figure class="slide">
        <img src="{{ p.img | relative_url }}" alt="{{ p.caption | escape }}" loading="eager">
        <figcaption class="sr-only">{{ p.caption }}</figcaption>
      </figure>
      {% endfor %}

      <!-- arrows -->
      <button class="tm-arrow prev" aria-label="Previous">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6" fill="none" stroke="currentColor" stroke-width="2"/></svg>
      </button>
      <button class="tm-arrow next" aria-label="Next">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg>
      </button>

      <!-- dots -->
      <div class="rotator-dots">
        {% for p in site.data.gallery %}
        <button aria-label="Slide {{ forloop.index }}"></button>
        {% endfor %}
      </div>
    </div>
  </div>
</section>


<section class="container">
  <h2 class="section-title">Family</h2>
  {% include athlete-grid.html %}
</section>

<script>
(function(){
  const r = document.querySelector('.hero-rotator .rotator');
  if (!r) return;
  const slides = [...r.querySelectorAll('.slide')];
  const dots   = [...r.querySelectorAll('.rotator-dots button')];
  const prev   = r.querySelector('.tm-arrow.prev');
  const next   = r.querySelector('.tm-arrow.next');

  let i = 0, t;
  function go(n){
    i = (n + slides.length) % slides.length;
    slides.forEach((s,k)=>s.classList.toggle('active', k===i));
    dots.forEach((d,k)=> d.toggleAttribute('aria-current', k===i));
  }
  const play  = () => (t = setInterval(()=>go(i+1), 4000));
  const pause = () => clearInterval(t);

  dots.forEach((d,k)=> d.addEventListener('click', ()=>{ pause(); go(k); play(); }));
  prev?.addEventListener('click', ()=>{ pause(); go(i-1); play(); });
  next?.addEventListener('click', ()=>{ pause(); go(i+1); play(); });

  r.addEventListener('mouseenter', pause);
  r.addEventListener('mouseleave', play);

  go(0); play();
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

