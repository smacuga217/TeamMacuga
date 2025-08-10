// assets/js/carousel.js
(function(){
  function initCarousel(root){
    const track = root.querySelector('.tm-track');
    const slides = Array.from(root.querySelectorAll('.tm-slide'));
    const prev   = root.querySelector('.tm-arrow.prev');
    const next   = root.querySelector('.tm-arrow.next');
    const dotsEl = root.querySelector('.tm-dots');
    if (!track || slides.length === 0) return;

    // build dots if empty
    let dots = [];
    if (dotsEl && dotsEl.children.length === 0){
      const totalPages = slides.length; // one-index per “step”
      for (let i=0;i<totalPages;i++){
        const b = document.createElement('button');
        b.type = 'button';
        b.setAttribute('aria-label', `Go to slide ${i+1}`);
        dotsEl.appendChild(b);
      }
    }
    dots = dotsEl ? Array.from(dotsEl.querySelectorAll('button')) : [];

    let index = 0;

    function perView(){
      const w = root.clientWidth;
      if (w >= 960) return 3;
      if (w >= 640) return 2;
      return 1;
    }

    function clamp(i){
      const max = Math.max(0, slides.length - perView());
      return Math.min(Math.max(0, i), max);
    }

    function update(){
      const gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap || 0);
      const v = perView();
      const slideWidth = (track.clientWidth - gap * (v-1)) / v;
      const x = -(slideWidth + gap) * index;
      track.style.transform = `translate3d(${x}px,0,0)`;
      if (prev) prev.disabled = index <= 0;
      if (next) next.disabled = index >= slides.length - v;
      if (dots.length){
        dots.forEach((b,i)=> b.setAttribute('aria-current', i===index ? 'true' : 'false'));
      }
    }

    prev && prev.addEventListener('click', ()=>{ index = clamp(index - 1); update(); });
    next && next.addEventListener('click', ()=>{ index = clamp(index + 1); update(); });
    dots.forEach((b,i)=> b.addEventListener('click', ()=>{ index = clamp(i); update(); }));

    // basic swipe
    let sx=null, pid=null;
    root.addEventListener('pointerdown', e=>{ sx=e.clientX; pid=e.pointerId; root.setPointerCapture(pid); });
    root.addEventListener('pointerup',   e=>{
      if (sx==null) return;
      const dx = e.clientX - sx;
      if (dx > 40) index = clamp(index - 1);
      if (dx < -40) index = clamp(index + 1);
      sx=null; pid=null; update();
    });

    window.addEventListener('resize', update);
    update();
  }

  document.addEventListener('DOMContentLoaded', ()=> {
    document.querySelectorAll('[data-carousel]').forEach(initCarousel);
  });
})();
