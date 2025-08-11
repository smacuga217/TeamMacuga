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
        <!-- Collab: image + details -->
        <a class="card-link" href="{{ product.external_url }}" target="_blank" rel="noopener">
          <div class="media">
            <span class="img-badge collab">Collab</span>
            <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          </div>
        </a>
        <div class="body">
          <div class="name">{{ product.title }}</div>
          {% if product.price %}<div class="price">${{ product.price }}</div>{% endif %}
        </div>
        <!-- Gradient CTA that makes it clear you leave the site -->
        <div class="actions collab-actions">
          <a class="btn primary external-btn" href="{{ product.external_url }}" target="_blank" rel="noopener">
            Shop collab&nbsp;↗
          </a>
        </div>

      {% else %}
        <!-- Normal product: image links to product page -->
        <a class="card-link" href="{{ product.url | relative_url }}">
          <div class="media">
            {% if product.badge %}<span class="img-badge">{{ product.badge }}</span>{% endif %}
            <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          </div>
        </a>
        <div class="body">
          <div class="name">{{ product.title }}</div>
          {% if product.price %}<div class="price">${{ product.price }}</div>{% endif %}
        </div>

        {% assign has_sizes = product.sizes and product.sizes.size > 1 %}
        {% if product.variant_ids or product.variant_id %}
          <div class="actions {% unless has_sizes %}no-size{% endunless %}">
            {% if has_sizes %}
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
  /* chips */
  .chip{ border:1px solid var(--border); padding:.35rem .75rem; border-radius:999px; background:#fff; cursor:pointer; }
  .chip.active{ background:var(--navy); color:#fff; }

  /* card skeleton + smaller media */
  .product-card{
    display:flex; flex-direction:column; background:#fff; border:1px solid var(--border);
    border-radius:var(--r); box-shadow:var(--shadow); overflow:hidden;
  }
  .product-card .media{ position:relative; background:#eef3ff; }
  .product-card .media img{ width:100%; height:200px; object-fit:cover; } /* smaller image height */
  .product-card .body{ padding:12px 14px; display:grid; gap:6px; }
  .product-card .name{ font-weight:700; font-size:1rem; }
  .product-card .price{ color:var(--muted); }

  /* overlay badge on image */
  .img-badge{
    position:absolute; left:10px; top:10px;
    padding:4px 10px; font-size:.75rem; font-weight:700; line-height:1;
    border-radius:999px; color:#fff; background: var(--brand);
    box-shadow:0 6px 16px rgba(0,0,0,.1); pointer-events:none;
  }
  .img-badge.collab{ background: linear-gradient(90deg, var(--brand), var(--navy)); }

  /* Uniform action row: 3 fixed columns on desktop */
  .actions{
    display:grid;
    align-items:center;
    gap:.6rem;
    grid-template-columns: 160px 1fr 180px;   /* size | qty | button */
    padding:12px 14px 14px;
    margin-top:auto;
  }

  /* Hide the size dropdown when there’s only one size,
     but keep the 1st column reserved so qty & button align */
  .actions.no-size .size-select{ display:none; }
  .actions.no-size::before{
    content:"";
    grid-column:1;                 /* occupies the Size column invisibly */
  }

  /* Compact qty and full-width button inside their columns */
  .qty-control{ justify-self:start; }
  .quick-add-btn{ width:100%; justify-content:center; }

  /* Select width matches the Size column */
  .size-select{
    width:100%; min-width:160px;   /* fills that first column cleanly */
    padding:.45rem .6rem;
    border:1px solid var(--border);
    border-radius:10px; background:#fff;
  }

  /* Collab CTA still fills its row */
  .collab-actions{ grid-template-columns: 1fr; }
  .external-btn{ width:100%; }

  /* Mobile: stack nicely */
  @media (max-width: 560px){
    .actions, .actions.no-size{
      grid-template-columns: 1fr 1fr;
    }
    .size-select{ grid-column: 1 / -1; }
    .quick-add-btn{ grid-column: 1 / -1; }
  }

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // qty stepper
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

  // quick add
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

    document.getElementById('mini-cart')?.classList.add('open');
    document.getElementById('cart-overlay')?.classList.add('show');
  });
});
</script>
