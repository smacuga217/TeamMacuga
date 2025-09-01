---
layout: default
title: Shop
---

<!-- Notice Bar -->
<div class="notice-bar">
  <p>Free shipping on all orders over $50!</p>
</div>

<!-- Page Title -->
<h1 class="shop-title">Shop Our Collection</h1>

<!-- Filter + Sort Controls -->
<div class="controls">
  <label for="category-filter">Filter by:</label>
  <select id="category-filter">
    <option value="all">All</option>
    <option value="hoodies">Hoodies</option>
    <option value="hats">Hats</option>
    <option value="tees">Tees</option>
  </select>

  <label for="sort-filter">Sort by:</label>
  <select id="sort-filter">
    <option value="default">Default</option>
    <option value="low-high">Price: Low to High</option>
    <option value="high-low">Price: High to Low</option>
  </select>
</div>

<!-- Product Grid -->
<div class="product-grid" id="product-grid">
  {% for product in site.products %}
  <div class="tm-card"
       data-category="{{ product.category | downcase }}"
       data-price="{{ product.price }}"
       data-product-id="{{ product.id }}"
       data-variant-ids='{{ product.variants | jsonify }}'>

    <img src="{{ product.image }}" alt="{{ product.title }}">
    <div class="tm-name">{{ product.title }}</div>

    <!-- Color Dropdown -->
    {% if product.colors %}
    <label>Color:
      <select class="color-select">
        {% for color in product.colors %}
        <option value="{{ color }}">{{ color }}</option>
        {% endfor %}
      </select>
    </label>
    {% endif %}

    <!-- Size Dropdown -->
    {% if product.sizes %}
    <label>Size:
      <select class="size-select">
        {% for size in product.sizes %}
        <option value="{{ size }}">{{ size }}</option>
        {% endfor %}
      </select>
    </label>
    {% endif %}

    <!-- Quantity Selector -->
    <div class="qty-selector">
      <button class="qty-minus">-</button>
      <span class="qty-val">1</span>
      <button class="qty-plus">+</button>
    </div>

    <!-- Add to Cart -->
    <button class="btn primary add-to-cart-btn">
      Add to Cart – ${{ product.price }}
    </button>
  </div>
  {% endfor %}
</div>

<style>
/* Notice Bar */
.notice-bar {
  background: #111;
  color: #fff;
  padding: 0.5rem;
  text-align: center;
  margin-bottom: 1rem;
}

/* Title */
.shop-title {
  font-size: 2rem;
  text-align: center;
  margin: 1rem 0 2rem;
}

/* Controls */
.controls {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}
.controls label {
  font-weight: bold;
  margin-right: 0.5rem;
}

/* Product Grid */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1.5rem;
}
.tm-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 10px;
  background: #fff;
  min-height: 360px;
}
.tm-card img {
  max-width: 100%;
  max-height: 200px;
  object-fit: contain;
  margin-bottom: 0.75rem;
}
.tm-name {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  text-align: center;
}
.tm-card label {
  font-size: 0.85rem;
  margin: 0.25rem 0;
}

/* Quantity Selector */
.qty-selector {
  display: flex;
  align-items: center;
  margin: 0.5rem 0;
}
.qty-minus, .qty-plus {
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
  background: linear-gradient(90deg, #b30000, #001f5c); /* red → navy */
  color: #fff;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-weight: bold;
  text-align: center;
  border: none;
  cursor: pointer;
  margin-top: auto;
}
.btn.primary:hover { opacity: 0.9; }
</style>

<script>
// Filtering and Sorting
const categoryFilter = document.getElementById("category-filter");
const sortFilter = document.getElementById("sort-filter");
const grid = document.getElementById("product-grid");

function applyFilters() {
  const category = categoryFilter.value;
  const products = [...grid.children];

  products.forEach(p => {
    p.style.display = (category === "all" || p.dataset.category === category) ? "flex" : "none";
  });

  if (sortFilter.value === "low-high") {
    products.sort((a,b) => a.dataset.price - b.dataset.price);
  } else if (sortFilter.value === "high-low") {
    products.sort((a,b) => b.dataset.price - a.dataset.price);
  }

  products.forEach(p => grid.appendChild(p));
}

categoryFilter.addEventListener("change", applyFilters);
sortFilter.addEventListener("change", applyFilters);

// Quantity buttons
document.querySelectorAll(".qty-minus").forEach(btn => {
  btn.addEventListener("click", e => {
    const val = e.target.nextElementSibling;
    let num = parseInt(val.textContent);
    if (num > 1) val.textContent = num - 1;
  });
});
document.querySelectorAll(".qty-plus").forEach(btn => {
  btn.addEventListener("click", e => {
    const val = e.target.previousElementSibling;
    let num = parseInt(val.textContent);
    val.textContent = num + 1;
  });
});
</script>
