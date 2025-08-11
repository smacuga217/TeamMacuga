---
layout: default
title: Shop
permalink: /shop/
---

<section class="container merch-index">
  <h1>Shop</h1>

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

  <div class="grid" id="products">
    {% for product in site.products %}
    <article class="product-card" data-cat="{{ product.category }}" data-price="{{ product.price }}">
      {% if product.external_url %}
        <a class="card-link" href="{{ product.external_url }}" target="_blank" rel="noopener">
      {% else %}
        <a class="card-link" href="{{ product.url | relative_url }}">
      {% endif %}
          <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          {% if product.badge %}
            <span class="pill {% if product.category == 'collab' or product.category contains 'collab' %}collab-badge{% endif %}">
              {{ product.badge }}
            </span>
          {% endif %}
          <h3>{{ product.title }}</h3>
          {% if product.price %}
            <p class="price">${{ product.price }}</p>
          {% endif %}
        </a>
    </article>
    {% endfor %}
  </div>
</section>

<style>
  .merch-index .grid {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 1.25rem;
  }
  @media (max-width: 960px) {
    .merch-index .grid { grid-template-columns: repeat(2,1fr); }
  }
  @media (max-width: 640px) {
    .merch-index
