---
layout: default
title: Shop
permalink: /shop/
redirect_from:
  - /merch/
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
  <div class="products" id="products">
    {% for product in site.products %}
    {% assign cats = product.category %}
    {% assign cats_json = cats | jsonify %}

    <article class="product-card"
      data-cat="{% if cats %}{% if cats_json contains '[' %}{{ cats | join: ' ' }}{% else %}{{ cats }}{% endif %}{% endif %}"
      data-price="{{ product.price | default: 0 }}">

      <a class="card-link" href="{{ product.url | relative_url }}">
        <div class="media">
          {% if product.badge %}
            {% assign badge_slug = product.badge | downcase | replace: ' ', '-' | replace: '!', '' %}
            <span class="img-badge badge-{{ badge_slug }}">{{ product.badge }}</span>
          {% endif %}
          <img class="main-img" src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
        </div>
      </a>

      <div class="body">
        <div class="name">{{ product.title }}</div>
        {% if product.price %}<div class="price">${{ product.price | number:2 }}</div>{% endif %}
      </div>

      {% if product.colors %}
        <div class="colors">
          {% for color in product.colors %}
            <label class="color-option">
              <input type="radio" name="color-{{ forloop.index0 }}" value="{{ color }}" {% if forloop.first %}checked{% endif %}>
              {{ color }}
            </label>
          {% endfor %}
        </div>
      {% endif %}

      {% if product.sizes %}
        <select class="size-select" aria-label="Size">
          {% for s in product.sizes %}
            <option value="{{ s }}">{{ s }}</option>
          {% endfor %}
        </select>
      {% endif %}

      <div class="actions">
        <div class="qty-control" data-qty aria-label="Quantity selector">
          <button type="button" class="qty-btn" data-qty-dec aria-label="Decrease quantity">−</button>
          <span class="qty-val" aria-live="polite">1</span>
          <button type="button" class="qty-btn" data-qty-inc aria-label="Increase quantity">+</button>
        </div>

        <button class="btn primary quick-add-btn"
          data-variants='{% if product.variant_ids %}{{ product.variant_ids | jsonify }}{% else %}{"One Size": {{ product.variant_id }} }{% endif %}'
          data-title="{{ product.title }}"
          data-price="{{ product.price | number:2 }}"
          data-img="{{ product.featured_image | relative_url }}">
          Add to cart
        </button>
      </div>
    </article>
    {% endfor %}
  </div>
</section>

<style>
.product-card .colors{ display:flex; gap:0.4rem; margin:0.5rem 0; flex-wrap:wrap; }
.color-option{ cursor:pointer; border:1px solid var(--border); border-radius:8px; padding:0.25rem 0.5rem; font-size:0.85rem; }
.size-select{ width:100%; margin-bottom:0.5rem; padding:0.4rem; border:1px solid var(--border); border-radius:10px; }
.main-img{ width:100%; border-radius:10px; object-fit:cover; }
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

  // Qty stepper
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

  // Quick add
  document.addEventListener('click', (e)=>{
    const btn = e.target.closest('.quick-add-btn');
    if(!btn) return;
    const card = btn.closest('.product-card');
    const variants = JSON.parse(btn.dataset.variants || '{}');

    const selSize = card.querySelector('.size-select');
    const size = selSize ? selSize.value : Object.keys(variants)[0];
    let variantId = variants[size];
    if(!variantId){ const vals = Object.values(variants); if(vals.length) variantId = vals[0]; }

    const qty = Math.max(1, parseInt(card.querySelector('.qty-val')?.textContent || '1', 10));
    if(!variantId){ alert('Please select a size.'); return; }

    window.dispatchEvent(new CustomEvent('tm:add', { detail:{
      id:String(variantId), qty,
      title: btn.dataset.title, price: btn.dataset.price, img: btn.dataset.img
    }}));

    document.getElementById('mini-cart')?.classList.add('open');
    document.getElementById('cart-overlay')?.classList.add('show');
  });

  // Color selector: update main image
  document.querySelectorAll('.product-card').forEach((card, idx)=>{
    const radios = card.querySelectorAll('input[name^="color-"]');
    if(radios.length){
      const mainImg = card.querySelector('.main-img');
      const imgMap = JSON.parse(card.querySelector('.quick-add-btn').dataset.variants || '{}');
      radios.forEach(r => r.addEventListener('change', e=>{
        const color = e.target.value;
        // Try to find first variant for that color
        let variantKey = Object.keys(imgMap).find(k => k.toLowerCase().startsWith(color.toLowerCase()));
        if(variantKey && imgMap[variantKey]){
          // Replace img with featured image if you want, or keep static
          // For simplicity, we leave main image unchanged; can extend to per-color images if needed
        }
      }));
    }
  });

});
</script>
