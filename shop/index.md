---
title: Shop
layout: default
---

<section class="container shop-page">

  <div class="cardish shop-hero" style="padding: clamp(16px, 2.2vw, 24px); margin-bottom: 2rem;">
    <h2 class="section-title" style="color: var(--ink);">Team Macuga Merchandise</h2>
    <p class="lead">Gear up and show your support — all merch ships directly from our Shopify store.</p>
    <div class="mission-actions">
      <a class="btn primary" href="https://teammacuga.myshopify.com" target="_blank" rel="noopener" style="color:#fff;">Visit Full Store →</a>
    </div>
  </div>

  <div id="shop-grid" class="shop-grid">
    <p class="muted" id="shop-loading">Loading products…</p>
  </div>

</section>

<style>
.shop-page { max-width: 1100px; }

.shop-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1.25rem;
  margin-bottom: 2rem;
}

.product-card {
  background: #fff;
  border: 1px solid rgba(11,18,32,.10);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 12px 28px rgba(0,0,0,.08);
  display: flex;
  flex-direction: column;
  transition: transform .15s ease, box-shadow .15s ease;
  text-decoration: none;
  color: var(--ink);
}
.product-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 36px rgba(0,0,0,.13);
}
.product-card-img {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  background: #f5f5f5;
  display: block;
}
.product-card-body {
  padding: .85rem 1rem 1rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}
.product-card-title {
  font-weight: 700;
  font-size: .95rem;
  margin: 0 0 .35rem;
  color: var(--ink);
  line-height: 1.3;
}
.product-card-price {
  font-size: .9rem;
  color: #555;
  margin-bottom: .75rem;
}
.product-card-btn {
  margin-top: auto;
  display: inline-block;
  background: linear-gradient(90deg, #ff5f6d, #ffc371);
  color: #fff !important;
  border-radius: 8px;
  padding: .5rem 1rem;
  font-weight: bold;
  text-align: center;
  font-size: .9rem;
  text-decoration: none;
}
.product-card-btn:hover { opacity: .9; }

.shop-error {
  background: #fff;
  border: 1px solid rgba(11,18,32,.10);
  border-radius: 14px;
  padding: 2rem;
  text-align: center;
  color: #555;
}
</style>

<script>
(function () {
  const SHOP_DOMAIN = 'teammacuga.myshopify.com';
  const STOREFRONT_TOKEN = 'eef519f85fdb5723cecc121a46860746';
  const grid = document.getElementById('shop-grid');

  const query = `{
    products(first: 12) {
      edges {
        node {
          title
          handle
          priceRange {
            minVariantPrice { amount currencyCode }
          }
          images(first: 1) {
            edges { node { url altText } }
          }
        }
      }
    }
  }`;

  fetch(`https://${SHOP_DOMAIN}/api/2024-01/graphql.json`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Shopify-Storefront-Access-Token': STOREFRONT_TOKEN
    },
    body: JSON.stringify({ query })
  })
  .then(r => r.json())
  .then(data => {
    const products = data?.data?.products?.edges;
    if (!products?.length) throw new Error('No products');

    grid.innerHTML = '';
    products.forEach(({ node: p }) => {
      const img = p.images.edges[0]?.node;
      const price = parseFloat(p.priceRange.minVariantPrice.amount).toFixed(2);
      const currency = p.priceRange.minVariantPrice.currencyCode;
      const url = `https://${SHOP_DOMAIN}/products/${p.handle}`;

      const card = document.createElement('a');
      card.className = 'product-card';
      card.href = url;
      card.target = '_blank';
      card.rel = 'noopener';
      card.innerHTML = `
        ${img
          ? `<img class="product-card-img" src="${img.url}" alt="${img.altText || p.title}">`
          : `<div class="product-card-img placeholder">👕</div>`}
        <div class="product-card-body">
          <div class="product-card-title">${p.title}</div>
          <div class="product-card-price">From ${currency} $${price}</div>
          <span class="product-card-btn">Shop Now →</span>
        </div>
      `;
      grid.appendChild(card);
    });
  })
  .catch(() => {
    grid.innerHTML = `
      <div class="shop-error">
        <p>Couldn't load products right now.</p>
        <a class="btn primary" href="https://${SHOP_DOMAIN}" target="_blank" rel="noopener" style="color:#fff; margin-top:.75rem; display:inline-block;">Browse the Full Store →</a>
      </div>`;
  });
})();
</script>