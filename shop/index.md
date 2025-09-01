<section class="shop-section">
  <div class="shop-header">
    <h2>Team Macuga Merchandise</h2>
    <div class="shop-notice">
      <p>Shipping and taxes are calculated by Shopify at checkout. If you want to shop in a different currency or see full details, please visit our Shopify store:</p>
      <a class="btn primary" href="https://teammacuga.myshopify.com" target="_blank" rel="noopener">Visit Shopify Store</a>
    </div>
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
</section>

<style>
/* Section & header */
.shop-section {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}
.shop-header {
  text-align: center;
  margin-bottom: 1.5rem;
}
.shop-header h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

/* Notice styling */
.shop-notice {
  background: #ffe6e6; /* soft pink */
  border: 1px solid #f5c2c7;
  padding: 16px;
  border-radius: 12px;
  margin: 0 auto 2rem;
  max-width: 800px;
  color: #5a1a1a; /* darker for readability */
  font-size: 1rem;
}
.shop-notice p {
  margin: 0 0 .5rem;
}
.shop-notice .btn {
  display: inline-block;
  margin-top: 0.5rem;
  text-decoration: none;
  padding: 0.5rem 1rem;
  background: #c91f1f;
  color: #fff;
  border-radius: 8px;
  transition: 0.2s;
}
.shop-notice .btn:hover {
  background: #a71b1b;
}

/* Carousel adjustments */
.tm-carousel {
  position: relative;
}
.tm-track {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  scroll-behavior: smooth;
  padding-bottom: 1rem;
}
.tm-card {
  flex: 0 0 220px; /* uniform width */
  display: flex;
  flex-direction: column;
  background: #fff;
  border-radius: 12px;
  border: 1px solid #ddd;
  padding: 1rem;
  box-sizing: border-box;
  min-height: 380px; /* uniform height */
  transition: transform 0.2s;
}
.tm-card:hover {
  transform: translateY(-4px);
}
.tm-imgwrap {
  position: relative;
  width: 100%;
  padding-top: 100%; /* square image */
  overflow: hidden;
  margin-bottom: 0.75rem;
}
.tm-imgwrap img {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}
.tm-meta {
  text-align: center;
  margin-bottom: 0.75rem;
}
.tm-name {
  display: block;
  font-weight: bold;
  margin-bottom: 0.25rem;
}
.tm-price {
  color: #c91f1f;
  font-weight: bold;
}

/* Color & size options */
.colors, .sizes {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}
.color-option, .size-option {
  font-size: 0.85rem;
}

/* Quantity & button */
.qty-control {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}
.qty-btn {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1px solid #ccc;
  background: #f9f9f9;
  cursor: pointer;
  font-size: 1.25rem;
  line-height: 1;
  text-align: center;
}
.qty-val {
  min-width: 24px;
  text-align: center;
}
.btn.primary.add-to-cart-btn {
  background: #c91f1f;
  color: #fff;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  text-align: center;
  cursor: pointer;
  font-weight: bold;
}
.btn.primary.add-to-cart-btn:hover {
  background: #a71b1b;
}

/* Arrows */
.tm-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255,255,255,0.8);
  border: none;
  font-size: 2rem;
  padding: 0 0.5rem;
  cursor: pointer;
  border-radius: 50%;
  z-index: 10;
}
.tm-arrow.prev { left: -1rem; }
.tm-arrow.next { right: -1rem; }
.tm-arrow:disabled { opacity: 0.3; cursor: default; }

/* Dots */
.tm-dots {
  text-align: center;
  margin-top: 0.5rem;
}
.tm-dots button {
  background: #ddd;
  border: none;
  width: 10px;
  height: 10px;
  margin: 0 3px;
  border-radius: 50%;
  cursor: pointer;
}
.tm-dots button[aria-current="true"] {
  background: #c91f1f;
}
</style>
