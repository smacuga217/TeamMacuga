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

      {% if product.external_url %}
        <!-- Collab card (no full-card link; use a clear CTA button) -->
        <div class="media">
          <span class="img-badge collab">Collab</span>
          <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
        </div>
        <div class="body">
          <div class="name">{{ product.title }}</div>
          {% if product.price %}<div class="price">${{ product.price }}</div>{% endif %}
        </div>
        <div class="body actions">
          <a class="btn primary collab-cta full"
             href="{{ product.external_url }}" target="_blank" rel="noopener"
             aria-label="Shop the {{ product.title }} collab on partner site">
            Shop Collab ↗
          </a>
        </div>

      {% else %}
        <!-- Normal product -->
        <a class="card-link" href="{{ product.url | relative_url }}">
          <div class="media">
            {% if product.badge %}
              {% assign badge_slug = product.badge | downcase | replace: ' ', '-' | replace: '!', '' %}
              <span class="img-badge badge-{{ badge_slug }}">{{ product.badge }}</span>
            {% endif %}
            <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          </div>
          <div class="body">
            <div class="name">{{ product.title }}</div>
            {% if product.price %}<div class="price">${{ product.price }}</div>{% endif %}
          </div>
        </a>

        {% if product.variant_ids or product.variant_id %}
        <!-- Actions: Size (top row), then Qty + Add (bottom row) -->
        <div class="actions">
          <div class="top">
            <label class="sr-only" for="size-{{ forloop.index }}">Size</label>
            <select id="size-{{ forloop.index }}" class="size-select" aria-label="Size">
              {% if product.sizes %}
                {% for s in product.sizes %}
                  <option value="{{ s }}">{{ s }}</option>
                {% endfor %}
              {% else %}
                <option value="One Size">One Size</option>
              {% endif %}
            </select>
          </div>

          <div class="bottom">
            <div class="qty-control" data-qty aria-label="Quantity selector">
              <button type="button" class="qty-btn" data-qty-dec aria-label="Decrease quantity">−</button>
              <span class="qty-val" aria-live="polite">1</span>
              <button type="button" class="qty-btn" data-qty-inc aria-label="Increase quantity">+</button>
            </div>

            <button class="btn primary quick-add-btn"
              data-variants='{% if product.variant_ids %}{{ product.variant_ids | jsonify }}{% else %}{"One Size": {{ product.variant_id }} }{% endif %}'
              data-title="{{ product.title }}"
              data-price="{{ product.price }}"
              data-img="{{ product.featured_image | relative_url }}">
              Add to cart
            </button>
          </div>
        </div>
        {% endif %}
      {% endif %}
    </article>
    {% endfor %}
  </div>
</section>

<style>
  /* chips */
  .chip{ border:1px solid var(--border); padding:.35rem .75rem; border-radius:999px; background:#fff; cursor:pointer; }
  .chip.active{ background:var(--navy); color:#fff; }

  /* overlay badge pinned on image */
  .product-card .media{ position:relative; }
  .img-badge{
    position:absolute; left:10px; top:10px;
    padding:4px 10px; font-size:.75rem; font-weight:700; line-height:1;
    border-radius:999px; color:#fff; background: var(--brand);
    box-shadow:0 6px 16px rgba(0,0,0,.10); pointer-events:none; user-select:none;
  }
  .img-badge.collab{ background: linear-gradient(90deg, var(--brand), var(--navy)); }

  /* explicit color mapping for known badges */
  .img-badge.badge-new{ background: var(--brand); }        /* team red */
  .img-badge.badge-bestseller{ background: var(--navy); }  /* team navy */

  /* actions layout: size row, then qty + button row */
  .actions{
    display:grid; grid-template-columns: 1fr; gap:.6rem;
    padding:12px 14px 14px; margin-top:auto;
  }
  .actions .top{ width:100%; }
  .actions .bottom{
    display:grid; grid-template-columns: auto 1fr; gap:.6rem; align-items:center;
  }

  .size-select{
    width:100%;
    min-height:40px;
    padding:.45rem .6rem;
    border:1px solid var(--border);
    border-radius:10px; background:#fff;
  }

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

  .quick-add-btn{
    width:100%; justify-content:center; white-space:nowrap;
    border:0; border-radius:12px;
  }

  /* Collab CTA full-width, same gradient look */
  .collab-cta.full{ width:100%; justify-content:center; }

  /* a11y helper for the hidden label */
  .sr-only{
    position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden;
    clip:rect(0,0,0,0); white-space:nowrap; border:0;
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

  // Qty steppers
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

    const sel = card.querySelector('.size-select');
    const size = sel ? sel.value : Object.keys(variants)[0];
    let variantId = variants[size];

    // Fallback for one-size objects if key mismatch
    if(!variantId){
      const vals = Object.values(variants);
      if(vals.length) variantId = vals[0];
    }

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
