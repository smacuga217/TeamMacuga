---
title: Our Story
layout: default
---

<section class="container">
  <h1 class="section-title">Our Story</h1>
  <p class="lead">
    Team Macuga is a family-powered ski crew from Park City. Three sisters—each carving their own path in
    <strong>alpine</strong>, <strong>moguls</strong>, and <strong>ski jumping</strong>—a younger brother in development,
    and two all-star parents keeping the show on the road. We travel, train, wax, race, jump, laugh, and learn together,
    aiming for <strong>Milano–Cortina 2026</strong> and beyond. This is a team that grows by doing—supporting each other at
    sunrise training runs, late-night tune sessions, and everything between. Welcome to the journey. #TeamMacuga
  </p>
</section>

<!-- ===== Gallery Rotator ===== -->
<section class="container">
  <div class="hero-rotator">
    <div class="rotator">
      {% for p in site.data.gallery %}
      <figure class="slide">
        <img src="{{ p.img | relative_url }}" alt="{{ p.caption | escape }}" loading="eager">
        <figcaption class="sr-only">{{ p.caption }}</figcaption>
      </figure>
      {% endfor %}

      <button class="tm-arrow prev" aria-label="Previous">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6" fill="none" stroke="currentColor" stroke-width="2"/></svg>
      </button>
      <button class="tm-arrow next" aria-label="Next">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg>
      </button>

      <div class="rotator-dots">
        {% for p in site.data.gallery %}<button aria-label="Slide {{ forloop.index }}"></button>{% endfor %}
      </div>
    </div>
  </div>
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

<!-- ===== Individual Bios (data-driven) ===== -->
<section id="bios">
  <div class="container">
    <h2 class="section-title">Individual Bios</h2>

    {% for a in site.data.family %}
    <article id="{{ a.slug }}-bio" class="bio-block card">
      <div class="bio-grid">
        <div class="bio-text">
          <h3>{{ a.name }}</h3>

          {% if a.bio %}
            <p>{{ a.bio }}</p>
          {% elsif a.teaser %}
            <p>{{ a.teaser }}</p>
          {% endif %}

          {% if a.highlights %}
            <p class="muted">{{ a.highlights }}</p>
          {% endif %}

          <div class="social-links" style="display:flex;gap:10px;align-items:center;margin-top:8px">
            {% if a.fis %}
              <a class="icon" href="{{ a.fis }}" target="_blank" rel="noopener" title="FIS profile">
                <img src="{{ '/assets/img/icons/fis-logo.png' | relative_url }}" alt="FIS" style="width:22px;height:22px">
              </a>
            {% endif %}
            {% if a.instagram %}
              <a class="icon" href="{{ a.instagram }}" target="_blank" rel="noopener" title="Instagram">
                <img src="{{ '/assets/img/icons/instagram-logo.png' | relative_url }}" alt="Instagram" style="width:22px;height:22px">
              </a>
            {% endif %}
            {% if a.facebook %}
              <a class="icon" href="{{ a.facebook }}" target="_blank" rel="noopener" title="Facebook">
                <img src="{{ '/assets/img/icons/facebook-logo.png' | relative_url }}" alt="Facebook" style="width:22px;height:22px">
              </a>
            {% endif %}

            {% if a.results %}
              <a class="pill" href="{{ a.results | relative_url }}" style="margin-left:8px">Results</a>
            {% endif %}
          </div>
        </div>

        <figure class="mini-rotator">
          {% if a.headshots and a.headshots.size > 0 %}
            {% for src in a.headshots %}
              <img class="slide{% if forloop.first %} active{% endif %}" src="{{ src | relative_url }}" alt="{{ a.name }} headshot {{ forloop.index }}">
            {% endfor %}
          {% else %}
            <img class="slide active" src="{{ a.photo | default: '/assets/img/placeholders/person.png' | relative_url }}" alt="{{ a.name }}">
          {% endif %}
          <div class="dots" aria-hidden="true"></div>
        </figure>
      </div>
    </article>
    {% endfor %}
  </div>
</section>

<script>
/* Mini headshot rotators inside each bio */
(function(){
  document.querySelectorAll('.mini-rotator').forEach(wrap=>{
    const slides = [...wrap.querySelectorAll('.slide')];
    if (!slides.length) return;

    const dotsWrap = wrap.querySelector('.dots');
    slides.forEach((_,k)=>{
      const b = document.createElement('button');
      if (k===0) b.classList.add('active');
      b.addEventListener('click', ()=>{ stop(); go(k); play(); });
      dotsWrap.appendChild(b);
    });
    const dots = [...dotsWrap.querySelectorAll('button')];

    let i = 0, t;
    function go(n){
      i = (n + slides.length) % slides.length;
      slides.forEach((s,k)=>s.classList.toggle('active', k===i));
      dots.forEach((d,k)=>d.classList.toggle('active', k===i));
    }
    const play = ()=> t = setInterval(()=>go(i+1), 3000);
    const stop = ()=> clearInterval(t);

    wrap.addEventListener('mouseenter', stop);
    wrap.addEventListener('mouseleave', play);

    go(0); play();
  });
})();
</script>

<!-- Back to top -->
<button id="back-to-top" aria-label="Scroll to top">↑ Top</button>
<script>
document.addEventListener("DOMContentLoaded", function(){
  const btn = document.getElementById("back-to-top");
  window.addEventListener("scroll", () => {
    btn.classList.toggle("show", window.scrollY > 300);
  });
  btn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: 'smooth' }));
});
</script>
