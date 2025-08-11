---
layout: default
title: Shop
permalink: /shop/
---

<section class="container merch-index">
  <h1>Shop</h1>

  <!-- Filters + Sort -->
  <div class="shop-controls">
    <div class="filter">
      <button class="chip active" data-filter="all">All</button>
      <button class="chip" data-filter="tops">Tops</button>
      <button class="chip" data-filter="hats">Hats</button>
      <button class="chip" data-filter="misc">Misc</button>
      <button class="chip" data-filter="collab">Collabs</button>
    </div>
    <div class="sort">
      <label for="sortPrice">Sort by price:</label>
      <select id="sortPrice">
        <option value="default">Default</option>
        <option value="asc">Low to High</option>
        <option value="desc">High to Low</option>
      </select>
    </div>
  </div>

  <!-- Grid -->
  <div class="grid" id="products">
    {% for product in site.products %}
    {% assign cats = product.category %}
    {% assign cats_json = cats | jsonify %}
    <article class="product-card"
             data-cat="{% if cats %}{% if cats_json contains '[' %}{{ cats | join: ' ' }}{% else %}{{ cats }}{% endif %}{% endif %}"
             data-price="{{ product.price }}">

      {% if product.external_url %}
        <!-- Collab: link out, no quick-add -->
        <a class="card-link" href="{{ product.external_url }}" target="_blank" rel="noopener">
          <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          <span class="pill collab-badge">{{ product.badge | default: 'Collab' }}</span>
          <h3>{{ product.title }}</h3>
          {% if product.price %}<p class="price">${{ product.price }}</p>{% endif %}
        </a>
      {% else %}
        <!-- Normal product: link to product page -->
        <a class="card-link" href="{{ product.url | relative_url }}">
          <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          {% if product.badge %}<span class="pill">{{ product.badge }}</span>{% endif %}
          <h3>{{ product.title }}</h3>
          {% if product.price %}<p class="price">${{ product.price }}</p>{% endif %}
        </a>

        {% if product.variant_ids or product.variant_id %}
          <!-- Quick add with size + pretty qty stepper -->
          <div class="quick-add">
            {% if product.sizes %}
              <select class="size-select" aria-label="Size">
                {% for s in product.sizes %}
                  <option value="{{ s }}">{{ s }}</option>
                {% endfor %}
              </select>
            {% endif %}

            <div class="qty-control" data-qty>
              <button type="button" class="qty-btn" data-qty-dec aria-label="Decrease quantity">−</button>
              <span class="qty-val" aria-live="polite">1</span>
              <button type="button" class="qty-btn" data-qty-inc aria-label="Increase quantity">+</button>
            </div>

            <button class="btn primary quick-add-btn"
                    data-variants='{% if product.variant_ids %}{{ product.variant_ids | jsonify }}{% else %}{"default": {{ product.variant_id }} }{% endif %}'
                    data-title="{{ product.title }}"
                    data-price="{{ product.price }}"
                    data-img="{{ product.featured_image | relative_url }}">
              Add to cart
            </button>
          </div>
        {% endif %}
      {% endif %}
    </article>
    {% endfor %}
  </div>
</section>

<style>
  /* Grid: 3 per row on desktop, 4 on wide, 2 tablet, 1 mobile */
  .merch-index .grid{
    display:grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem 1.25rem;
  }
  @media (min-width:1280px){ .merch-index .grid{ grid-template-columns: repeat(4, 1fr); } }
  @media (max-width: 960px){ .merch-index .grid{ grid-template-columns: repeat(2, 1fr); } }
  @media (max-width: 640px){ .merch-index .grid{ grid-template-columns: 1fr; } }

  .shop-controls{ display:flex; justify-content:space-between; align-items:center; gap:.75rem; margin-bottom:1rem; flex-wrap:wrap; }
  .chip{ border:1px solid var(--border); padding:.3rem .75rem; border-radius:999px; background:#fff; cursor:pointer; }
  .chip.active{ background:var(--navy); color:#fff; }

  .product-card{ position:relative; background:#fff; border-radius:12px; box-shadow:var(--shadow); overflow:hidden; }
  .product-card img{ width:100%; height:240px; object-fit:cover; display:block; }
  .product-card h3, .product-card p{ margin:.5rem .75rem; }
  .pill{ position:absolute; top:.5rem; left:.5rem; background:var(--brand); color:#fff; padding:.2rem .6rem; border-radius:999px; font-size:.75rem; font-weight:600; }
  .collab-badge{ background:#ff6600; }

  .quick-add{ display:flex; gap:.5rem; align-items:center; padding:.5rem .75rem .75rem; }
  .size-select{ flex:1; min-width:110px; padding:.45rem .6rem; border:1px solid var(--border); border-radius:8px; background:#fff; }

  /* Pretty qty stepper with white background */
  .qty-control{
    display:inline-flex; align-items:center; gap:.5rem;
    background:#fff; border:1px solid var(--border);
    border-radius:12px; padding:.25rem;
    box-shadow: 0 1px 2px rgba(0,0,0,.04);
  }
  .qty-btn{
    width:34px; height:34px; border:0; background:#f6f6f6;
    border-radius:10px; font-size:1.15rem; line-height:1; cursor:pointer;
  }
  .qty-val{ min-width:2ch; text-align:center; font-variant-numeric: tabular-nums; }

  /* Make the Add to cart match homepage gradient via .btn.primary. 
     If .btn.primary already exists sitewide, this fallback won't clash. */
  .btn.primary{
    background: linear-gradient(90deg, var(--brand, #1e90ff), var(--brand-2, #22c55e));
    color:#fff; border:0;
  }
  .quick-add-btn{
    flex-shrink:0; padding:.6rem .9rem; border-radius:12px; cursor:pointer;
  }
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // Filter
  const chips = document.querySelectorAll('.chip');
  const grid = document.getElementById('products');
  const filter = cat => {
    document.querySelectorAll('.product-card').forEach(c => {
      const cats = (c.dataset.cat || '').toLowerCase();
      c.style.display = (cat === 'all' || cats.includes(cat)) ? '' : 'none';
    });
  };
  chips.forEach(ch => ch.addEventListener('click', () => {
    chips.forEach(c => c.classList.remove('active'));
    ch.classList.add('active');
    filter(ch.dataset.filter);
  }));

  // Sort
  const sortSel = document.getElementById('sortPrice');
  sortSel.addEventListener('change', () => {
    const cards = [...document.querySelectorAll('.product-card')].filter(c => c.style.display !== 'none');
    if (sortSel.value !== 'default') {
      const dir = sortSel.value === 'asc' ? 1 : -1;
      cards.sort((a,b) => ((parseFloat(a.dataset.price)||0) - (parseFloat(b.dataset.price)||0)) * dir);
    }
    cards.forEach(c => grid.appendChild(c));
  });

  // Qty steppers in grid
  document.addEventListener('click', (e)=>{
    const dec = e.target.closest('[data-qty-dec]');
    const inc = e.target.closest('[data-qty-inc]');
    if(dec || inc){
      const wrap = (dec||inc).closest('[data-qty]');
      const valEl = wrap.querySelector('.qty-val');
      let n = parseInt(valEl.textContent || '1', 10) || 1;
      n += inc ? 1 : -1;
      n = Math.max(1, Math.min(99, n));
      valEl.textContent = n;
    }
  });

  // Quick add (reads size + qty, supports one-size via first variant fallback)
  document.addEventListener('click', (e)=>{
    const btn = e.target.closest('.quick-add-btn');
    if(!btn) return;

    const card = btn.closest('.product-card');
    const variants = JSON.parse(btn.dataset.variants || '{}');

    const sel = card.querySelector('.size-select');
    const size = sel ? sel.value : Object.keys(variants)[0];
    const variantId = size && variants[size];

    const qty = Math.max(1, parseInt(card.querySelector('.qty-val')?.textContent || '1', 10));

    if(!variantId){ alert('Please select a size.'); return; }

    window.dispatchEvent(new CustomEvent('tm:add', { detail:{
      id:String(variantId), qty,
      title: btn.dataset.title, price: btn.dataset.price, img: btn.dataset.img
    }}));

    // open mini-cart for feedback
    document.getElementById('mini-cart')?.classList.add('open');
    document.getElementById('cart-overlay')?.classList.add('show');
  });
});
</script>
