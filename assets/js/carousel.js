(function () {
  function initCarousel(root) {
    const track = root.querySelector('.tm-track');
    const slides = Array.from(root.querySelectorAll('.tm-slide'));
    const prev = root.querySelector('.tm-arrow.prev');
    const next = root.querySelector('.tm-arrow.next');
    const dotsWrap = root.querySelector('.tm-dots');

    if (!track || slides.length === 0) return;

    let index = 0;
    let pageWidth = 0;
    let pages = 1;

    function compute() {
      // width of one “page” (the visible area of the carousel)
      pageWidth = root.clientWidth;
      // total pages based on total scrollable width:
      pages = Math.max(1, Math.ceil(track.scrollWidth / pageWidth));
      renderDots();
      go(Math.min(index, pages - 1), false);
    }

    function renderDots() {
      dotsWrap.innerHTML = '';
      for (let i = 0; i < pages; i++) {
        const b = document.createElement('button');
        b.type = 'button';
        b.setAttribute('aria-label', `Go to slide ${i + 1}`);
        if (i === index) b.setAttribute('aria-current', 'true');
        b.addEventListener('click', () => go(i, true));
        dotsWrap.appendChild(b);
      }
    }

    function go(i, animate = true) {
      index = Math.max(0, Math.min(i, pages - 1));
      const x = -index * pageWidth;
      track.style.transition = animate ? 'transform .45s ease' : 'none';
      track.style.transform = `translateX(${x}px)`;
      // update dots + arrows
      dotsWrap.querySelectorAll('button').forEach((d, k) => {
        d.toggleAttribute('aria-current', k === index);
      });
      prev.disabled = index === 0;
      next.disabled = index >= pages - 1;
    }

    prev && prev.addEventListener('click', () => go(index - 1, true));
    next && next.addEventListener('click', () => go(index + 1, true));
    window.addEventListener('resize', () => compute(), { passive: true });

    // first layout
    compute();
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.tm-carousel').forEach(initCarousel);
  });
})();
