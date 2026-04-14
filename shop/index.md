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

  <div class="shop-carousel-wrap">
    <button class="carousel-arrow left" id="shop-prev" aria-label="Previous">&#8249;</button>
    <div class="shop-carousel" id="shop-carousel">
      <div class="shop-carousel-track" id="shop-track">
        <p class="muted" style="padding:1rem;">Loading products…</p>
      </div>
    </div>
    <button class="carousel-arrow right" id="shop-next" aria-label="Next">&#8250;</button>
  </div>

</section>

<style>
.shop-page { max-width: 1100px; }

.shop-carousel-wrap {
  position: relative;
  display: flex;
  align-items: center;
  gap: .5rem;
  margin-bottom: 2rem;
}

.shop-carousel {
  overflow: hidden;
  flex: 1;
}

.shop-carousel-track {
  display: flex;
  gap: 1rem;
  transition: transform .35s ease;
}

.carousel-arrow {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid rgba(11,18,32,.15);
  background: #fff;
  font-size: 1.4rem;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0,0,0,.08);
  transition: opacity .15s;
  color: var(--ink);
}
.carousel-arrow:hover { opacity: .7; }
.carousel-arrow:disabled { opacity: .25; cursor: default; }

.product-card {
  flex: 0 0 200px;
  background: #fff;
  border: 1px solid rgba(11,18,32,.10);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0,0,0,.07);
  display: flex;
  flex-direction: column;
  transition: transform .15s ease, box-shadow .15s ease;
  text-decoration: none;
  color: var(--ink);
}
.product-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 28px rgba(0,0,0,.12);
}
.product-card-img {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  background: #f5f5f5;
  display: block;
}
.product-card-body {
  padding: .75rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}
.product-card-title {
  font-weight: 700;
  font-size: .85rem;
  margin: 0 0 .25rem;
  color: var(--ink);
  line-height: 1.3;
}
.product-card-price {
  font-size: .8rem;
  color: #555;
  margin-bottom: .6rem;
}
.product-card-btn {
  margin-top: auto;
  display: inline-block;
  background: linear-gradient(90deg, #ff5f6d, #ffc371);
  color: #fff !important;
  border-radius: 8px;
  padding: .4rem .75rem;
  font-weight: bold;
  text-align: center;
  font-size: .8rem;
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

@media (max-width: 600px) {
  .product-card { flex: 0 0 160px; }
}
</style>

<script>
(function () {
  const SHOP_DOMAIN = 'teammacuga.myshopify.com';
  const STOREFRONT_TOKEN = 'eef519f85fdb5723cecc121a46860746';
  const track = document.getElementById('shop-track');
  const prevBtn = document.getElementById('shop-prev');
  const nextBtn = document.getElementById('shop-next');

  let current = 0;
  let cardWidth = 216;
  let visibleCount = 4;

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

    track.innerHTML = '';
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
          : `<div class="product-card-img" style="display:flex;align-items:center;justify-content:center;font-size:2rem;color:#ccc;">👕</div>`}
        <div class="product-card-body">
          <div class="product-card-title">${p.title}</div>
          <div class="product-card-price">From ${currency} $${price}</div>
          <span class="product-card-btn">Shop Now →</span>
        </div>
      `;
      track.appendChild(card);
    });

    const total = products.length;

    function getVisible() {
      return window.innerWidth < 600 ? 2 : window.innerWidth < 900 ? 3 : 4;
    }

    function updateCarousel() {
      visibleCount = getVisible();
      const firstCard = track.querySelector('.product-card');
      if (!firstCard) return;
      cardWidth = firstCard.offsetWidth + 16;
      const maxOffset = Math.max(0, total - visibleCount);
      current = Math.min(current, maxOffset);
      track.style.transform = `translateX(-${current * cardWidth}px)`;
      prevBtn.disabled = current === 0;
      nextBtn.disabled = current >= maxOffset;
    }

    prevBtn.addEventListener('click', () => { current--; updateCarousel(); });
    nextBtn.addEventListener('click', () => { current++; updateCarousel(); });
    window.addEventListener('resize', updateCarousel);

    setTimeout(updateCarousel, 50);
  })
  .catch(() => {
    track.innerHTML = `
      <div class="shop-error">
        <p>Couldn't load products right now.</p>
        <a class="btn primary" href="https://${SHOP_DOMAIN}" target="_blank" rel="noopener" style="color:#fff; margin-top:.75rem; display:inline-block;">Browse the Full Store →</a>
      </div>`;
  });
})();
</script>