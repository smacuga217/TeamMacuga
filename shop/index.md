<section class="shop-section">
  <div class="shop-header">
    <h2>Team Macuga Merchandise</h2>
    <div class="shop-notice">
      <p>Shipping and taxes are calculated by Shopify at checkout. If you want to shop in a different currency or see full details, please visit our Shopify store:</p>
      <a class="btn primary hero-btn" href="https://teammacuga.myshopify.com" target="_blank" rel="noopener">
        Visit Shopify Store
      </a>
    </div>

    <!-- Filters & Sort -->
    <div class="shop-controls">
      <label>
        Filter by category:
        <select id="filter-category">
          <option value="all">All</option>
          {% assign categories = site.products | map: "category" | uniq %}
          {% for cat in categories %}
            <option value="{{ cat }}">{{ cat | capitalize }}</option>
          {% endfor %}
        </select>
      </label>

      <label>
        Sort by price:
        <select id="sort-price">
          <option value="none">Default</option>
          <option value="asc">Low to High</option>
          <option value="desc">High to Low</option>
        </select>
      </label>
    </div>
  </div>

  <!-- Grid -->
  <div class="merch-grid" id="merch-grid">
    {% for product in site.products %}
      <article class="tm-card"
               data-product-id="{{ product.id }}"
               data-price="{{ product.price | float }}"
               data-category="{{ product.category }}"
               data-variant-ids='{{ product.variant_ids | jsonify }}'>
        <a class="tm-link" href="{{ product.external_url | default: product.url | relative_url }}" {% if product.external_url %}target="_blank" rel="noopener"{% endif %}>
          <div class="tm-imgwrap">
            {% if product.badge %}
              {% assign b = product.badge | downcase %}
              <span class="img-badge
                {% if b contains 'collab' %}collab
                {% elsif b contains 'new' %}badge-new
                {% elsif b contains 'best' %}badge-bestseller{% endif %}">
                {{ product.badge }}
              </span>
            {% endif %}
            {% if product.featured_image %}
              <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
            {% endif %}
          </div>
          <div class="tm-meta">
            <span class="tm-name">{{ product.title }}</span>
          </div>
        </a>

        {% if product.colors %}
          <div class="colors">
            <label>
              Color:
              <select name="color-{{ product.id }}">
                {% for color in product.colors %}
                  <option value="{{ color }}">{{ color }}</option>
                {% endfor %}
              </select>
            </label>
          </div>
        {% endif %}

        {% if product.sizes %}
          <div class="sizes">
            <label>
              Size:
              <select name="size-{{ product.id }}">
                {% for size in product.sizes %}
                  <option value="{{ size }}">{{ size }}</option>
                {% endfor %}
              </select>
            </label>
          </div>
        {% endif %}

        <div class="qty-control" data-qty>
          <button type="button" class="qty-btn" data-qty-dec>−</button>
          <span class="qty-val" aria-live="polite">1</span>
          <button type="button" class="qty-btn" data-qty-inc>+</button>
        </div>

        <button class="btn primary hero-btn add-to-cart-btn">
          Add to cart - ${{ product.price }}
        </button>

      </article>
    {% endfor %}
  </div>
</section>

<script>
(function(){
  const grid = document.getElementById('merch-grid');
  const filterCategory = document.getElementById('filter-category');
  const sortPrice = document.getElementById('sort-price');

  function filterAndSort() {
    const category = filterCategory.value;
    const sort = sortPrice.value;

    let cards = Array.from(grid.querySelectorAll('.tm-card'));

    // Filter by category
    cards.forEach(card => {
      const cat = card.dataset.category;
      card.style.display = (category === "all" || cat === category) ? '' : 'none';
    });

    // Sort by price
    if(sort === 'asc' || sort === 'desc'){
      cards = cards.sort((a,b)=>{
        const pa = parseFloat(a.dataset.price);
        const pb = parseFloat(b.dataset.price);
        return sort === 'asc' ? pa - pb : pb - pa;
      });
      cards.forEach(card => grid.appendChild(card));
    }
  }

  filterCategory.addEventListener('change', filterAndSort);
  sortPrice.addEventListener('change', filterAndSort);

  // Quantity stepper
  grid.querySelectorAll('.qty-control').forEach(qtyWrap=>{
    qtyWrap.addEventListener('click', e=>{
      const dec = e.target.closest('[data-qty-dec]');
      const inc = e.target.closest('[data-qty-inc]');
      if(!dec && !inc) return;
      const valEl = qtyWrap.querySelector('.qty-val');
      let n = parseInt(valEl.textContent||'1',10);
      n += inc?1:-1;
      n = Math.max(1,Math.min(99,n));
      valEl.textContent = n;
    });
  });

  // Add-to-cart with variant and dynamic price
  grid.querySelectorAll('.add-to-cart-btn').forEach(btn=>{
    const card = btn.closest('.tm-card');
    const price = card.dataset.price;
    btn.textContent = `Add to cart - $${price}`;

    btn.addEventListener('click', ()=>{
      const productId = card.dataset.productId;
      const qty = parseInt(card.querySelector('.qty-val').textContent||'1',10);
      const selectedColor = card.querySelector('select[name="color-'+productId+'"]')?.value;
      const selectedSize = card.querySelector('select[name="size-'+productId+'"]')?.value;


      const variantIds = JSON.parse(card.dataset.variantIds || '{}');
      const variantKey = `${selectedColor}|${selectedSize}`;
      const variantId = variantIds[variantKey] || productId;

      window.dispatchEvent(new CustomEvent('tm:add', { detail:{
        id: variantId,
        qty,
        price,
        title: card.querySelector('.tm-name').textContent,
        color: selectedColor,
        size: selectedSize,
        img: card.querySelector('img')?.src
      }}));
    });
  });
})();
</script>

<style>
/* Section & header */
.shop-section { max-width: 1200px; margin: 2rem auto; padding: 0 1rem; }
.shop-header { text-align: center; margin-bottom: 1.5rem; }
.shop-header h2 { font-size: 2rem; margin-bottom: 1rem; color: #333; }

/* Notice */
.shop-notice {
  background: #ffe6e6;
  border: 1px solid #f5c2c7;
  padding: 16px;
  border-radius: 12px;
  margin: 0 auto 1.5rem;
  max-width: 800px;
  color: #5a1a1a;
  font-size: 1rem;
}
.shop-notice .btn { display: inline-block; margin-top: 0.5rem; }

/* Filters */
.shop-controls {
  display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 2rem; flex-wrap: wrap;
}
.shop-controls select { padding: 0.3rem 0.5rem; border-radius: 6px; border: 1px solid #ccc; }

/* Grid */
.merch-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap: 1.5rem; }

/* Card */
.tm-card { display: flex; flex-direction: column; background: #fff; border-radius: 12px; border: 1px solid #ddd; padding: 1rem; min-height: 400px; }
.tm-imgwrap { position: relative; width: 100%; padding-top: 100%; overflow: hidden; margin-bottom: 0.75rem; }
.tm-imgwrap img { position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; border-radius: 8px; }
.tm-meta { text-align: center; margin-bottom: 0.75rem; }
.tm-name { display: block; font-weight: bold; margin-bottom: 0.25rem; }
.colors, .sizes { display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.5rem; }
.qty-control { display: flex; justify-content: center; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem; }
.qty-btn { width: 28px; height: 28px; border-radius: 50%; border: 1px solid #ccc; background: #f9f9f9; cursor: pointer; text-align: center; }
.qty-val { min-width: 24px; text-align: center; }

/* Buttons */
.btn.primary { 
  background: linear-gradient(90deg,#ff5f6d,#ffc371);
  color: #fff;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-weight: bold;
  text-align: center;
  border: none;
  cursor: pointer;
}
.btn.primary:hover { opacity: 0.9; }
.btn.primary.add-to-cart-btn { margin-top: auto; }
</style>
