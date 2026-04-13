```html
<section class="shop-section">
  <div style="max-width: 600px; margin: 3rem auto; padding: 0 1rem; text-align: center;">
    <h2 style="font-size: 2rem; margin-bottom: 1rem; color: #333;">Team Macuga Merchandise</h2>
    <p style="font-size: 1rem; color: #555; line-height: 1.7; margin-bottom: 2rem;">
      Browse and purchase our full range of merch — apparel, accessories, and more — directly on our Shopify store.
    </p>

    <a class="btn primary hero-btn" href="https://teammacuga.myshopify.com" target="_blank" rel="noopener">
      Shop now →
    </a>

    <p style="font-size: 0.85rem; color: #888; margin-top: 1.5rem;">
      Shipping and taxes calculated at checkout &nbsp;·&nbsp; Multiple currencies supported
    </p>
  </div>
</section>

<style>
.shop-section { max-width: 1200px; margin: 2rem auto; padding: 0 1rem; }
.btn.primary {
  display: inline-block;
  background: linear-gradient(90deg, #ff5f6d, #ffc371);
  color: #fff;
  border-radius: 8px;
  padding: 0.75rem 2rem;
  font-weight: bold;
  text-align: center;
  border: none;
  cursor: pointer;
  text-decoration: none;
  font-size: 1rem;
}
.btn.primary:hover { opacity: 0.9; }
</style>
```

That's everything — paste this in place of the entire existing file contents. If `.btn.primary` is already defined elsewhere in your site's CSS, you can safely delete the `<style>` block here to avoid duplication.