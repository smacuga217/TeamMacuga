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

  <!-- Grid (uses global .products / .product-card styles) -->
  <div class="products" id="products">
    {% for product in site.products %}
    {% assign cats = product.category %}
    {% assign cats_json = cats | jsonify %}
    <article class="product-card"
             data-cat="{% if cats %}{% if cats_json contains '[' %}{{ cats | join: ' ' }}{% else %}{{ cats }}{% endif %}{% endif %}"
             data-price="{{ product.price | default: 0 }}">

      {% if product.external_url %}
        <!-- Collab: link out, no quick-add -->
        <a class="card-link" href="{{ product.external_url }}" target="_blank" rel="noopener">
          <div class="media">
            <span class="img-badge collab">Collab</span>
            <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          </div>
          <div class="body">
            <div class="name">{{ product.title }}</div>
            {% if product.price %}<div class="price">${{ product.price }}</div>{% endif %}
          </div>
        </a>

      {% else %}
        <!-- Normal product -->
        <a class="card-link" href="{{ product.url | relative_url }}">
          <div class="media">
            {% if product.badge %}
              <span class="img-badge">{{ product.badge }}</span>
            {% endif %}
            <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          </div>
          <div class="body">
            <div class="name">{{ product.title }}</div>
            {% if product.price %}<div class="price">${{ product.price }}</div>{% endif %}
          </div>
        </a>

        {% if product.variant_ids or product.variant_id %}
          <!-- Compact quick add: size (optional) + qty stepper + button -->
          <div class="body quick-add">
            {% if product.sizes and product.sizes.size > 1 %}
              <select class="size-select" aria-label="Size">
                {% for s in product.sizes %}
                  <option value="{{ s }}">{{ s }}</option>
                {% endfor %}
              </select>
            {% endif %}

            <div class="qty-control" data-qty aria-label="Quantity selector">
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
  /* filter chips */
  .chip{ border:1px solid var(--border); padding:.35rem .75rem; border-radius:999px; background:#fff; cursor:pointer; }
  .chip.active{ background:var(--navy); color:#fff; }

  /* overlay badge on product image */
  .product-card .media{ position:relative; }
  .img-badge{
    position:absolute; left:10px; top:10px;
    padding:4px 10px; font-size:.75rem; font-weight:700; line-height:1;
    border-radius:999px; color:#fff; background: var(--brand);
    box-shadow:0 6px 16px rgba(0,0,0,.10);
    pointer-events:none; user-select:none;
  }
  .img-badge.collab{ background: linear-gradient(90deg, var(--brand), var(--navy)); }

  /* compact quick add row */
  .quick-add{
    display:flex; align-items:center; gap:.6rem; flex-wrap:wrap;
    padding:0; background:transparent; border:0;
  }
  .size-select{
    flex:0 1 160px;
    min-width:140px;
    padding:.45rem .6rem;
    border:1px solid var(--border);
    border-radius:10px;
    background:#fff;
  }
  .qty-control{
    flex:0 0 auto;
    display:inline-flex; align-items:center; gap:.5rem;
    padding:.25rem;
    border:1px solid var(--border);
    border-radius:12px; background:#fff;
    box-shadow:0 1px 2px rgba(0,0,0,.04);
  }
  .qty-btn{
    width:34px; height:34px;
    border:0; border-radius:10px;
    background:#f6f6f6;
    font-size:1.15rem; line-height:1; cursor:pointer;
  }
  .qty-val{ width:2ch; text-align:center; font-variant-numeric: tabular-nums; }

  .quick-add-btn{
    flex:0 0 auto;
    white-space:nowrap;
    padding:.6rem 1rem;
    border-radius:12px;
    display:inline-flex; align-items:center; justify-content:center;
  }

  /* stack nicely on small screens */
  @media (max-width:520px){
    .quick-add{ gap:.5rem; }
    .quick-add-btn{ width:100%; order:3; }
    .size-select{ flex:1 1 100%; order:1; }
    .qty-control{ order:2; }
  }
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // Qty stepper (– 1 +)
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

  // Quick add (supports one-size by falling back to first/only variant key)
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
