<div class="notice-bar">
  <p>Welcome to the Team Macuga Shop! Support our journey by grabbing some gear 🏔️</p>
  <a class="btn primary" href="https://teammacuga.myshopify.com" target="_blank" rel="noopener">
    Visit Shopify Store
  </a>
</div>

<div class="shop-controls">
  <label>Filter by Category:
    <select id="category-filter">
      <option value="all">All</option>
      <option value="shirts">Shirts</option>
      <option value="hoodies">Hoodies</option>
      <option value="hats">Hats</option>
    </select>
  </label>

  <label>Sort by Price:
    <select id="price-sort">
      <option value="default">Default</option>
      <option value="low">Low to High</option>
      <option value="high">High to Low</option>
    </select>
  </label>
</div>

<div class="product-grid" id="product-grid">
  {% for product in site.data.products %}
  <div class="tm-card"
       data-category="{{ product.category }}"
       data-price="{{ product.price }}"
       data-product-id="{{ product.id }}"
       data-variant-ids='{{ product.variants | jsonify }}'>

    <img src="{{ product.image }}" alt="{{ product.name }}">
    <div class="tm-name">{{ product.name }}</div>

    <label>Color:
      <select class="color-select">
        {% for color in product.colors %}
          <option value="{{ color }}">{{ color }}</option>
        {% endfor %}
      </select>
    </label>

    <label>Size:
      <select class="size-select">
        {% for size in product.sizes %}
          <option value="{{ size }}">{{ size }}</option>
        {% endfor %}
      </select>
    </label>

    <div class="qty-selector">
      <button class="qty-minus">-</button>
      <span class="qty-val">1</span>
      <button class="qty-plus">+</button>
    </div>

    <button class="btn primary add-to-cart-btn">
      Add to cart – ${{ product.price }}
    </button>
  </div>
  {% endfor %}
</div>

<style>
/* Notice bar */
.notice-bar {
  background: #f8f8f8;
  padding: 1rem;
  margin-bottom: 1rem;
  text-align: center;
  border-bottom: 1px solid #ddd;
}
.notice-bar p {
  margin: 0 0 .5rem 0;
  font-size: 1.1rem;
}

/* Shop controls (sticky) */
.shop-controls {
  position: sticky;
  top: 60px; /* adjust based on navbar height */
  z-index: 20;
  background: #fff;
  padding: .75rem 1rem;
  border-bottom: 1px solid #ddd;
  display: flex;
  gap: 1rem;
  justify-content: center;
  align-items: center;
}
.shop-controls label {
  font-weight: 600;
  font-size: .9rem;
}
.shop-controls select {
  margin-left: .5rem;
  padding: .3rem .5rem;
  border-radius: 6px;
  border: 1px solid #ccc;
}

/* Product grid */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(250px,1fr));
  gap: 1.5rem;
  padding: 1rem;
}

/* Product card */
.tm-card {
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: .75rem;
  background: #fff;
  transition: box-shadow .2s ease;
}
.tm-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,.08);
}
.tm-card img {
  max-width: 100%;
  border-radius: 8px;
  object-fit: cover;
}
.tm-name {
  font-weight: bold;
  font-size: 1rem;
}

/* Dropdowns */
.tm-card label {
  font-size: .85rem;
  font-weight: 500;
  display: block;
}
.tm-card select {
  width: 100%;
  margin-top: .25rem;
  padding: .4rem;
  border-radius: 6px;
  border: 1px solid #ccc;
}

/* Quantity selector */
.qty-selector {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: .5rem;
}
.qty-selector button {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1px solid #ccc;
  background: #f9f9f9;
  cursor: pointer;
  text-align: center;
}
.qty-val {
  min-width: 24px;
  text-align: center;
}

/* Buttons */
.btn.primary { 
  background: linear-gradient(90deg,#ff5f6d,#002147);
  color: #fff;
  border-radius: 8px;
  padding: 0.6rem 1rem;
  font-weight: bold;
  text-align: center;
  border: none;
  cursor: pointer;
  transition: opacity .2s ease;
}
.btn.primary:hover { opacity: 0.9; }
.btn.primary.add-to-cart-btn { margin-top: auto; }
</style>

<script>
// Filter + Sort
const grid = document.getElementById("product-grid");
const categoryFilter = document.getElementById("category-filter");
const priceSort = document.getElementById("price-sort");

categoryFilter.addEventListener("change", filterAndSort);
priceSort.addEventListener("change", filterAndSort);

function filterAndSort() {
  let cards = [...grid.children];
  const category = categoryFilter.value;
  const sort = priceSort.value;

  cards.forEach(card => {
    if (category === "all" || card.dataset.category === category) {
      card.style.display = "";
    } else {
      card.style.display = "none";
    }
  });

  if (sort !== "default") {
    cards.sort((a, b) => {
      let pa = parseFloat(a.dataset.price), pb = parseFloat(b.dataset.price);
      return sort === "low" ? pa - pb : pb - pa;
    });
    cards.forEach(card => grid.appendChild(card));
  }
}

// Quantity selector
document.querySelectorAll(".qty-selector").forEach(qtyBox => {
  let val = qtyBox.querySelector(".qty-val");
  qtyBox.querySelector(".qty-plus").addEventListener("click", () => {
    val.textContent = parseInt(val.textContent) + 1;
  });
  qtyBox.querySelector(".qty-minus").addEventListener("click", () => {
    let n = parseInt(val.textContent);
    if (n > 1) val.textContent = n - 1;
  });
});
</script>
