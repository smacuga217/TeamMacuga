<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shop</title>
  <style>
    /* Notice Bar */
    .notice {
      background: #f5f5f5;
      text-align: center;
      padding: 0.75rem;
      margin-top: 60px; /* so it sits below navbar */
      border-bottom: 1px solid #ddd;
      font-weight: 500;
    }

    /* Container */
    .container { 
      max-width: 1200px; 
      margin: 2rem auto; 
      padding: 0 1rem; 
    }

    .shop-header {
      text-align: center;
      margin-bottom: 2rem;
    }

    .shop-header h1 {
      font-size: 2rem;
      margin-bottom: 0.5rem;
    }

    /* Sorting + Filtering */
    .controls { 
      display: flex; 
      justify-content: flex-end; 
      margin-bottom: 1.5rem; 
      gap: 1rem;
    }
    .controls select { 
      padding: 0.5rem; 
      border: 1px solid #ccc; 
      border-radius: 6px; 
    }

    /* Product Grid */
    .product-grid { 
      display: grid; 
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); 
      gap: 1.5rem; 
    }

    /* Product Card */
    .tm-card { 
      background: #fff; 
      border: 1px solid #eee; 
      border-radius: 10px; 
      padding: 1rem; 
      display: flex; 
      flex-direction: column; 
      box-shadow: 0 2px 5px rgba(0,0,0,0.05); 
      transition: transform 0.2s ease; 
    }
    .tm-card:hover { transform: translateY(-3px); }
    .tm-card img { 
      max-height: 220px; 
      object-fit: contain; 
      margin-bottom: 1rem; 
    }
    .tm-name { 
      font-size: 1.1rem; 
      font-weight: 600; 
      margin-bottom: 0.25rem; 
    }
    .tm-price { 
      font-weight: bold; 
      margin-bottom: 0.75rem; 
    }

    /* Variant dropdowns */
    .variant-select {
      margin-bottom: 0.75rem;
    }
    .variant-select label {
      display: block;
      font-size: 0.85rem;
      margin-bottom: 0.25rem;
      font-weight: 500;
    }
    .variant-select select {
      width: 100%;
      padding: 0.4rem;
      border: 1px solid #ccc;
      border-radius: 6px;
    }

    /* Quantity */
    .qty { 
      display: flex; 
      align-items: center; 
      margin-bottom: 0.75rem; 
    }
    .qty button { 
      width: 28px; height: 28px; 
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
      background: linear-gradient(90deg,#c8102e,#001f54); /* red → navy */
      color: #fff;
      border-radius: 8px;
      padding: 0.6rem 1rem;
      font-weight: bold;
      text-align: center;
      border: none;
      cursor: pointer;
      transition: opacity 0.2s ease;
    }
    .btn.primary:hover { opacity: 0.9; }
    .btn.primary.add-to-cart-btn { margin-top: auto; }
  </style>
</head>
<body>

  <!-- Notice -->
  <div class="notice">
    Free shipping on orders over $100!
  </div>

  <div class="container">
    <div class="shop-header">
      <h1>Shop Team Macuga</h1>
      <a class="btn primary" href="https://teammacuga.myshopify.com" target="_blank" rel="noopener">
        Visit Shopify Store
      </a>
    </div>

    <!-- Controls -->
    <div class="controls">
      <select id="sortSelect">
        <option value="default">Sort By</option>
        <option value="low-high">Price: Low to High</option>
        <option value="high-low">Price: High to Low</option>
      </select>
    </div>

    <!-- Product Grid -->
    <div class="product-grid" id="productGrid">
      {% for product in site.data.products %}
      <div class="tm-card" data-price="{{ product.price }}" data-product-id="{{ product.id }}" data-variant-ids='{{ product.variants | jsonify }}'>
        <img src="{{ product.image }}" alt="{{ product.name }}">
        <h3 class="tm-name">{{ product.name }}</h3>
        <p class="tm-price">${{ product.price }}</p>

        <!-- Color dropdown -->
        {% if product.colors %}
        <div class="variant-select">
          <label for="color-{{ product.id }}">Color</label>
          <select id="color-{{ product.id }}" name="color-{{ product.id }}">
            {% for color in product.colors %}
              <option value="{{ color }}">{{ color }}</option>
            {% endfor %}
          </select>
        </div>
        {% endif %}

        <!-- Size dropdown -->
        {% if product.sizes %}
        <div class="variant-select">
          <label for="size-{{ product.id }}">Size</label>
          <select id="size-{{ product.id }}" name="size-{{ product.id }}">
            {% for size in product.sizes %}
              <option value="{{ size }}">{{ size }}</option>
            {% endfor %}
          </select>
        </div>
        {% endif %}

        <!-- Quantity -->
        <div class="qty">
          <button class="qty-decrease">-</button>
          <span class="qty-val">1</span>
          <button class="qty-increase">+</button>
        </div>

        <!-- Add to Cart -->
        <button class="btn primary add-to-cart-btn">
          Add to Cart – ${{ product.price }}
        </button>
      </div>
      {% endfor %}
    </div>
  </div>

  <script>
    // Sorting
    const grid = document.getElementById('productGrid');
    const sortSelect = document.getElementById('sortSelect');
    sortSelect.addEventListener('change', e=>{
      const cards = [...grid.children];
      if(e.target.value === 'low-high'){
        cards.sort((a,b)=>parseFloat(a.dataset.price)-parseFloat(b.dataset.price));
      } else if(e.target.value === 'high-low'){
        cards.sort((a,b)=>parseFloat(b.dataset.price)-parseFloat(a.dataset.price));
      }
      cards.forEach(c=>grid.appendChild(c));
    });

    // Quantity controls
    document.querySelectorAll('.tm-card').forEach(card=>{
      const qtyVal = card.querySelector('.qty-val');
      card.querySelector('.qty-decrease').addEventListener('click',()=>{
        let val = parseInt(qtyVal.textContent,10);
        if(val>1){ qtyVal.textContent = val-1; }
      });
      card.querySelector('.qty-increase').addEventListener('click',()=>{
        let val = parseInt(qtyVal.textContent,10);
        qtyVal.textContent = val+1;
      });
    });
  </script>
</body>
</html>
