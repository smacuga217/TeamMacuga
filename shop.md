---
layout: default
title: Shop
permalink: /shop/
---

<section class="container">
  <h1>Shop</h1>
  <div class="tabs" role="tablist" aria-label="Shop tabs">
    <button class="tab active" data-tab="merch" aria-selected="true">Team Macuga Merch</button>
    <button class="tab" data-tab="collabs" aria-selected="false">Collabs</button>
  </div>

  <div id="tab-merch" class="tabpanel show" role="tabpanel">
    <div class="grid cards-2">
      <article class="card product"><img alt="Classic Tee" src="{{ '/assets/img/placeholders/1x1.svg' | relative_url }}"><h3>Classic Tee</h3><p>$28</p><a class="pill" href="#">Buy</a></article>
      <article class="card product"><img alt="Hoodie" src="{{ '/assets/img/placeholders/1x1.svg' | relative_url }}"><h3>Hoodie</h3><p>$55</p><a class="pill" href="#">Buy</a></article>
    </div>
  </div>

  <div id="tab-collabs" class="tabpanel" role="tabpanel" hidden>
    <div class="grid cards-2">
      <article class="card product"><img alt="Pit Viper × Lauren" src="{{ '/assets/img/placeholders/1x1.svg' | relative_url }}"><h3>Pit Viper × Lauren</h3><p>Dropping soon</p><a class="pill" href="#">Details</a></article>
      <article class="card product"><img alt="Collab 2" src="{{ '/assets/img/placeholders/1x1.svg' | relative_url }}"><h3>Collab 2</h3><p>Soon</p><a class="pill" href="#">Details</a></article>
    </div>
  </div>
</section>

<script>
document.querySelectorAll('.tabs .tab').forEach(btn=>{
  btn.addEventListener('click',()=>{
    document.querySelectorAll('.tabs .tab').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const id = btn.dataset.tab;
    document.querySelectorAll('.tabpanel').forEach(p=>{
      const show = p.id === 'tab-'+id;
      p.toggleAttribute('hidden', !show);
      p.classList.toggle('show', show);
    });
  });
});
</script>
