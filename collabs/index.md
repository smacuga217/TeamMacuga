---
layout: default
title: Team Macuga Collabs
permalink: /collabs/
---

<section class="container merch-index">
  <h1>Team Macuga Collabs</h1>
  <div class="grid">
    {% for product in site.products %}
      {% if product.category contains "collab" or product.category == "collab" %}
      <article class="product-card">
        <a class="card-link"
           href="{{ product.external_url }}"
           target="_blank" rel="noopener">
          <img src="{{ product.featured_image | relative_url }}" alt="{{ product.title }}">
          {% if product.badge %}<span class="pill">{{ product.badge }}</span>{% endif %}
          <h3>{{ product.title }}</h3>
          {% if product.price %}<p class="price">${{ product.price }}</p>{% endif %}
        </a>
      </article>
      {% endif %}
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
    .merch-index .grid { grid-template-columns: 1fr; }
  }
</style>
