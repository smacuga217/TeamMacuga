/* Simple bio carousels */
document.querySelectorAll('[data-carousel]').forEach(carousel=>{
  const track = carousel.querySelector('.carousel__track');
  const slides = [...carousel.querySelectorAll('.carousel__slide')];
  let i = 0;
  const go = n => { i = (n + slides.length) % slides.length; track.style.transform = `translateX(-${i*100}%)`; };
  carousel.querySelector('[data-prev]')?.addEventListener('click', ()=>go(i-1));
  carousel.querySelector('[data-next]')?.addEventListener('click', ()=>go(i+1));
});

/* Merch filters + price sort */
const grid = document.getElementById('merchGrid');
if (grid){
  const products = [...grid.children];

  const applyFilters = ()=>{
    const allBtn = document.querySelector('[data-filter].is-active');
    const collabFilter = allBtn ? allBtn.dataset.filter : 'all';
    const catBtn = document.querySelector('.btn[data-category].is-active');
    const cat = catBtn ? catBtn.dataset.category : null;

    products.forEach(p=>{
      const isCollab = p.dataset.collab === 'true';
      const matchesAll = (collabFilter === 'all') || (collabFilter === 'collab' && isCollab);
      const matchesCat = !cat || p.dataset.category === cat;
      p.style.display = (matchesAll && matchesCat) ? '' : 'none';
    });
  };

  const sortByPrice = dir=>{
    const visible = products.filter(p=>p.style.display !== 'none');
    visible.sort((a,b)=> dir==='asc' ? (+a.dataset.price)-(+b.dataset.price) : (+b.dataset.price)-(+a.dataset.price));
    visible.forEach(el=>grid.appendChild(el));
  };

  const toggleGroup = (sel,btn)=> document.querySelectorAll(sel).forEach(b=>b.classList.toggle('is-active', b===btn));

  document.querySelectorAll('[data-filter]').forEach(btn=>{
    btn.addEventListener('click', ()=>{ toggleGroup('[data-filter]', btn); applyFilters(); });
  });
  document.querySelectorAll('[data-category]').forEach(btn=>{
    btn.addEventListener('click', ()=>{ toggleGroup('[data-category]', btn); applyFilters(); });
  });
  document.getElementById('sortPrice')?.addEventListener('change', e=>{
    if(e.target.value==='asc') sortByPrice('asc');
    else if(e.target.value==='desc') sortByPrice('desc');
  });
}
