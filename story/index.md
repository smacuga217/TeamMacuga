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

<section class="container">
  <h2 class="section-title">The Family</h2>
  <!-- Grid cards; each name links to an anchor below -->
  {% include athlete-grid.html %}
</section>

<section class="container">
  <!-- In-depth bios with mini image rotators; the anchors match the grid links -->
  {% for a in site.data.family %}
  <article id="{{ a.slug }}-bio" class="card" style="margin-bottom:16px">
    <div style="display:grid;gap:16px;grid-template-columns:1.2fr .8fr;align-items:center">
      <div>
        <h3 style="margin-top:0">{{ a.name }}</h3>
        <p>
          {% if a.bio %}
            {{ a.bio }}
          {% else %}
            {{ a.name }}’s full bio is coming soon. For now, follow along on social and check competition results.
          {% endif %}
        </p>
        <div style="margin-top:8px;display:flex;gap:10px;flex-wrap:wrap">
          {% if a.fis %}<a class="btn" target="_blank" rel="noopener" href="{{ a.fis }}">See on FIS</a>{% endif %}
          {% if a.instagram %}<a class="btn" target="_blank" rel="noopener" href="{{ a.instagram }}">Instagram</a>{% endif %}
          {% if a.facebook %}<a class="btn" target="_blank" rel="noopener" href="{{ a.facebook }}">Facebook</a>{% endif %}
        </div>
      </div>
      <figure class="hero-rotator">
        <div class="frame rotator-{{ a.slug }}">
          <!-- three placeholder slides per person for now -->
          <img class="slide active" src="{{ '/assets/img/placeholders/person.png' | relative_url }}" alt="{{ a.name }} photo 1">
          <img class="slide" src="{{ '/assets/img/placeholders/person.png' | relative_url }}" alt="{{ a.name }} photo 2">
          <img class="slide" src="{{ '/assets/img/placeholders/person.png' | relative_url }}" alt="{{ a.name }} photo 3">
          <div class="dots"></div>
        </div>
      </figure>
    </div>
  </article>
  {% endfor %}
</section>

<script>
/* tiny per-person rotator (re-uses the hero rotator behavior) */
document.querySelectorAll('[class^="rotator-"]').forEach((wrap)=>{
  const slides=[...wrap.querySelectorAll('.slide')], dots=wrap.querySelector('.dots'); let i=0;
  slides.forEach((_,k)=>{const b=document.createElement('button');if(k===0)b.classList.add('active');b.onclick=()=>go(k);dots.appendChild(b);});
  function go(n){ i=n; slides.forEach((s,k)=>s.classList.toggle('active',k===i));
    dots.querySelectorAll('button').forEach((d,k)=>d.classList.toggle('active',k===i)); }
  setInterval(()=>go((i+1)%slides.length), 5000);
});
</script>
