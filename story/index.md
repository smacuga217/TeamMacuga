---
title: Our Story
layout: default
---

<section class="container">
  <h1 class="section-title">Our Story</h1>
  <p class="lead">
    Team Macuga is a family-powered ski crew from Park City. Three sisters, a younger brother in development,
    and two all-star parents keeping the show on the road. We travel, train, wax, race, jump, laugh, and learn together —
    aiming for <strong>Milano–Cortina 2026</strong> and beyond. Welcome to the journey. <strong>#TeamMacuga</strong>
  </p>
</section>

<section id="bios" class="container">
  <h2 class="section-title">Individual Bios</h2>

  <!-- Lauren -->
  <article id="bio-lauren" class="bio-block card">
    <div class="bio-grid">
      <div class="bio-text">
        <h3>Lauren</h3>
        <p>World Cup speed specialist with calm precision and scary-fast lines.</p>
        <p class="muted">Highlights: World Cup SG winner; Worlds SG bronze.</p>
        <p><a class="pill" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=228398" target="_blank" rel="noopener">See on FIS</a></p>
      </div>
      <figure class="bio-photo-wrap">
        <img id="photo-lauren" class="bio-photo" alt="Lauren headshot">
      </figure>
    </div>
  </article>

  <!-- Alli -->
  <article id="bio-alli" class="bio-block card">
    <div class="bio-grid">
      <div class="bio-text">
        <h3>Alli</h3>
        <p>Power + play — clean lines, sharp airs, fast feet. Trajectory: up.</p>
        <p class="muted">Highlights: World Cup podiums; 2023 FIS Rookie of the Year.</p>
        <p><a class="pill" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=FS&competitorid=220306" target="_blank" rel="noopener">See on FIS</a></p>
      </div>
      <figure class="bio-photo-wrap">
        <img id="photo-alli" class="bio-photo" alt="Alli headshot">
      </figure>
    </div>
  </article>

  <!-- Sam -->
  <article id="bio-sam" class="bio-block card">
    <div class="bio-grid">
      <div class="bio-text">
        <h3>Sam</h3>
        <p>Quiet focus, big-air confidence, steady leadership vibes.</p>
        <p class="muted">Highlights: Continental Cup starts; relentless work ethic.</p>
        <p><a class="pill" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=JP&competitorid=211435" target="_blank" rel="noopener">See on FIS</a></p>
      </div>
      <figure class="bio-photo-wrap">
        <img id="photo-sam" class="bio-photo" alt="Sam headshot">
      </figure>
    </div>
  </article>

  <!-- Daniel -->
  <article id="bio-daniel" class="bio-block card">
    <div class="bio-grid">
      <div class="bio-text">
        <h3>Daniel</h3>
        <p>Developing racer — learns fast, loves the grind, brings the energy.</p>
        <p class="muted">Highlights: future speedster; wax-room banter pro.</p>
        <p><a class="pill" href="https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=260517" target="_blank" rel="noopener">See on FIS</a></p>
      </div>
      <figure class="bio-photo-wrap">
        <img id="photo-daniel" class="bio-photo" alt="Daniel headshot">
      </figure>
    </div>
  </article>

  <!-- Amy -->
  <article id="bio-amy" class="bio-block card">
    <div class="bio-grid">
      <div class="bio-text">
        <h3>Amy</h3>
        <p>Operations lead — logistics, travel, and keeping the crew grounded.</p>
        <p class="muted">Highlights: solves problems before they exist; A-level road-trip DJ.</p>
      </div>
      <figure class="bio-photo-wrap">
        <img id="photo-amy" class="bio-photo" alt="Amy headshot">
      </figure>
    </div>
  </article>

  <!-- Dan -->
  <article id="bio-dan" class="bio-block card">
    <div class="bio-grid">
      <div class="bio-text">
        <h3>Dan</h3>
        <p>Gear &amp; wax-room sage, lifelong supporter and sideline strategist.</p>
        <p class="muted">Highlights: wax whisperer; chairlift-wisdom specialist.</p>
      </div>
      <figure class="bio-photo-wrap">
        <img id="photo-dan" class="bio-photo" alt="Dan headshot">
      </figure>
    </div>
  </article>
</section>

<!-- Back to top -->
<button id="back-to-top" aria-label="Scroll to top">↑ Top</button>

<script>
/* --- Automatic headshot rotators (no controls) ----------------------- */
/* Files live in /assets/img/gallery/headshots/ and names are consistent. */
const HEADSHOTS = {
  lauren: [
    '/assets/img/gallery/headshots/lauren-headshot-1.jpg',
    '/assets/img/gallery/headshots/lauren-headshot-2.jpg',
    '/assets/img/gallery/headshots/lauren-headshot-3.jpg',
    '/assets/img/gallery/headshots/lauren-headshot-4.jpg',
  ],
  alli: [
    '/assets/img/gallery/headshots/alli-headshot-1.jpg',
    '/assets/img/gallery/headshots/alli-headshot-2.jpg',
    '/assets/img/gallery/headshots/alli-headshot-3.jpg',
    '/assets/img/gallery/headshots/alli-headshot-4.jpg',
    '/assets/img/gallery/headshots/alli-headshot-5.jpg',
  ],
  sam: [
    '/assets/img/gallery/headshots/sam-headshot-1.jpg',
    '/assets/img/gallery/headshots/sam-headshot-2.jpg',
    '/assets/img/gallery/headshots/sam-headshot-3.jpg',
    '/assets/img/gallery/headshots/sam-headshot-4.jpg',
  ],
  daniel: [
    '/assets/img/gallery/headshots/daniel-headshot-1.jpg',
    '/assets/img/gallery/headshots/daniel-headshot-2.jpg',
    '/assets/img/gallery/headshots/daniel-headshot-3.jpg',
  ],
  amy: [
    '/assets/img/gallery/headshots/amy-headshot-2.jpg',
    '/assets/img/gallery/headshots/amy-headshot-3.jpg',
    '/assets/img/gallery/headshots/amy-headshot-4.jpg',
    '/assets/img/gallery/headshots/amy-headshot-5.jpg',
  ],
  dan: [
    '/assets/img/gallery/headshots/dan-headshot-1.jpg',
    '/assets/img/gallery/headshots/dan-headshot-2.jpg',
    '/assets/img/gallery/headshots/dan-headshot-3.jpg',
    '/assets/img/gallery/headshots/dan-headshot-4.jpg',
  ],
};

function startRotator(imgId, list, ms=3500){
  const img = document.getElementById(imgId);
  if (!img || !list?.length) return;
  let i = 0;
  // first frame
  img.src = list[i];
  // cycle
  setInterval(()=>{
    i = (i + 1) % list.length;
    // quick fade-out / in
    img.classList.remove('show');
    requestAnimationFrame(()=>{
      setTimeout(()=>{ img.src = list[i]; img.classList.add('show'); }, 180);
    });
  }, ms);
}

document.addEventListener('DOMContentLoaded', ()=>{
  startRotator('photo-lauren', HEADSHOTS.lauren);
  startRotator('photo-alli',   HEADSHOTS.alli);
  startRotator('photo-sam',    HEADSHOTS.sam);
  startRotator('photo-daniel', HEADSHOTS.daniel);
  startRotator('photo-amy',    HEADSHOTS.amy);
  startRotator('photo-dan',    HEADSHOTS.dan);

  // back-to-top button behavior
  const btn = document.getElementById('back-to-top');
  window.addEventListener('scroll', ()=> {
    (window.scrollY > 300) ? btn.classList.add('show') : btn.classList.remove('show');
  });
  btn.addEventListener('click', ()=> window.scrollTo({ top: 0, behavior: 'smooth' }));
});
</script>
