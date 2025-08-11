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
    <article class="product-card"
             data-cat="{% if cats %}{% if cats.first %}{{ cats | join: ' ' }}{% else %}{{ cats }}{% endif %}{% endif %}"
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

        {% if product.variant_ids %}
          <!-- Quick add -->
          <div class="quick-add">
            {% if product.sizes %}
              <select class="size-select">
                {% for s in product.sizes %}
                  <option value="{{ s }}">{{ s }}</option>
                {% endfor %}
              </select>
            {% endif %}
            <button class="btn quick-add-btn"
                    data-variants='{{ product.variant_ids | jsonify }}'
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
  .merch-index .grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; }
  @media (max-width: 960px){ .merch-index .grid{ grid-template-columns:repeat(2,1fr); } }
  @media (max-width: 640px){ .merch-index .grid{ grid-template-columns:1fr; } }

  .shop-controls{ display:flex; justify-content:space-between; align-items:center; gap:.75rem; margin-bottom:1rem; flex-wrap:wrap; }
  .chip{ border:1px solid var(--border); padding:.3rem .75rem; border-radius:999px; background:#fff; cursor:pointer; }
  .chip.active{ background:var(--navy); color:#fff; }
  .pill{ position:absolute; top:.5rem; left:.5rem; background:var(--brand); color:#fff; padding:.2rem .6rem; border-radius:999px; font-size:.75rem; font-weight:600; }
  .collab-badge{ background:#ff6600; }

  .product-card{ position:relative; background:#fff; border-radius:12px; box-shadow:var(--shadow); overflow:hidden; }
  .product-card img{ width:100%; height:260px; object-fit:cover; display:block; }
  .product-card h3, .product-card p{ margin:.5rem .75rem; }
  .quick-add{ display:flex; gap:.5rem; align-items:center; padding:.5rem .75rem .75rem; }
  .size-select{ flex:1; padding:.4rem; border:1px solid var(--border); border-radius:6px; }
  .quick-add-btn{ flex-shrink:0; padding:.5rem .75rem; border:0; border-radius:8px; background:var(--navy); color:#fff; cursor:pointer; }
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
    } else {
      // no-op: keeps current order
    }
    cards.forEach(c => grid.appendChild(c));
  });

  // Quick add (only for non-collab cards that rendered a .quick-add-btn)
  document.addEventListener('click', (e)=>{
    const btn = e.target.closest('.quick-add-btn');
    if(!btn) return;

    const variants = JSON.parse(btn.dataset.variants || '{}');
    const card = btn.closest('.product-card');
    const sel = card.querySelector('.size-select');
    const size = sel ? sel.value : Object.keys(variants)[0];
    const variantId = size && variants[size];

    if(!variantId){ alert('Please select a size.'); return; }

    window.dispatchEvent(new CustomEvent('tm:add', { detail:{
      id:String(variantId), qty:1,
      title: btn.dataset.title, price: btn.dataset.price, img: btn.dataset.img
    }}));

    // open mini-cart for feedback (if present)
    document.getElementById('mini-cart')?.classList.add('open');
    document.getElementById('cart-overlay')?.classList.add('show');
  });
});
</script>
