<div class="shop-notice">
  <p>Shipping and taxes are calculated by Shopify at checkout. If there are any issues or you want to shop in a different currency, please visit our Shopify store:</p>
  <a class="btn primary" href="https://teammacuga.myshopify.com" target="_blank" rel="noopener">Visit Shopify Store</a>
</div>

<div id="merch-carousel" class="tm-carousel" data-carousel>
  <button class="tm-arrow prev" aria-label="Previous" data-prev>‹</button>

  <div class="tm-track" data-track tabindex="0">
    {% for product in site.products limit:12 %}
      <article class="tm-card" 
               data-product-id="{{ product.id }}" 
               data-price="{{ product.price }}"
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
            {% if product.price %}<span class="tm-price">${{ product.price }}</span>{% endif %}
          </div>
        </a>

        {% if product.colors %}
          <div class="colors">
            {% for color in product.colors %}
              <label class="color-option">
                <input type="radio" name="color-{{ product.id }}" value="{{ color }}" {% if forloop.first %}checked{% endif %}>
                {{ color }}
              </label>
            {% endfor %}
          </div>
        {% endif %}

        {% if product.sizes %}
          <div class="sizes">
            {% for size in product.sizes %}
              <label class="size-option">
                <input type="radio" name="size-{{ product.id }}" value="{{ size }}" {% if forloop.first %}checked{% endif %}>
                {{ size }}
              </label>
            {% endfor %}
          </div>
        {% endif %}

        <div class="qty-control" data-qty>
          <button type="button" class="qty-btn" data-qty-dec>−</button>
          <span class="qty-val" aria-live="polite">1</span>
          <button type="button" class="qty-btn" data-qty-inc>+</button>
        </div>

        <button class="btn primary add-to-cart-btn">
          Add to cart
        </button>

      </article>
    {% endfor %}
  </div>

  <button class="tm-arrow next" aria-label="Next" data-next>›</button>
  <div class="tm-dots" data-dots aria-label="Carousel pagination"></div>
</div>

<script>
(function(){
  const root  = document.getElementById('merch-carousel');
  if(!root) return;
  const track = root.querySelector('[data-track]');
  const prev  = root.querySelector('[data-prev]');
  const next  = root.querySelector('[data-next]');
  const dotsWrap = root.querySelector('[data-dots]');

  function pageWidth(){ return track.clientWidth; }
  function maxScroll(){ return track.scrollWidth - track.clientWidth; }
  function pages(){ return Math.max(1, Math.ceil(track.scrollWidth / pageWidth())); }
  function currentPage(){ return Math.round(track.scrollLeft / pageWidth()); }
  function goTo(page){
    const clamped = Math.max(0, Math.min(page, pages()-1));
    track.scrollTo({ left: clamped * pageWidth(), behavior:'smooth' });
  }
  function update(){
    const p = currentPage(), total = pages();
    prev.disabled = (track.scrollLeft <= 0);
    next.disabled = (track.scrollLeft >= maxScroll() - 1);
    dotsWrap.innerHTML = '';
    for(let i=0;i<total;i++){
      const b = document.createElement('button');
      if(i===p) b.setAttribute('aria-current','true');
      b.addEventListener('click', ()=>goTo(i));
      dotsWrap.appendChild(b);
    }
  }
  prev.addEventListener('click', ()=>goTo(currentPage()-1));
  next.addEventListener('click', ()=>goTo(currentPage()+1));
  track.addEventListener('scroll', ()=>{ window.requestAnimationFrame(update); }, { passive:true });
  window.addEventListener('resize', update);
  update();

  // Quantity stepper
  root.querySelectorAll('.qty-control').forEach(qtyWrap=>{
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

  // Add-to-cart per product with variant support
  root.querySelectorAll('.add-to-cart-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      const card = btn.closest('.tm-card');
      const productId = card.dataset.productId;
      const qty = parseInt(card.querySelector('.qty-val').textContent||'1',10);
      const selectedColor = card.querySelector('input[name="color-'+productId+'"]:checked')?.value;
      const selectedSize = card.querySelector('input[name="size-'+productId+'"]:checked')?.value;
      const price = card.dataset.price;
      const title = card.querySelector('.tm-name').textContent;
      const img = card.querySelector('img')?.src;

      // Get correct variant ID
      const variantIds = JSON.parse(card.dataset.variantIds || '{}');
      const variantKey = `${selectedColor}|${selectedSize}`;
      const variantId = variantIds[variantKey] || productId;

      window.dispatchEvent(new CustomEvent('tm:add', { detail:{
        id: variantId,
        qty,
        price,
        title,
        color: selectedColor,
        size: selectedSize,
        img
      }}));
    });
  });
})();
</script>

<style>
.shop-notice{
  background:#fdf4f4; border:1px solid #f5c2c7; padding:12px 16px; border-radius:12px; margin-bottom:1rem;
}
.shop-notice p{ margin:0 0 .5rem; font-size:.95rem; }
.shop-notice .btn{ display:inline-block; }
</style>
