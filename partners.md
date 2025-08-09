---
layout: default
title: Our Partners
nav: partners
---
<section>
  <h2 class="section-title">Collaborations</h2>
  <div class="grid">
  {%- for c in site.data.collabs -%}
    <article class="card" style="display:flex;flex-direction:column;gap:10px">
      <div style="display:flex;align-items:center;gap:12px">
        <img src="{{ c.logo | relative_url }}" alt="{{ c.name }} logo" style="height:40px;max-width:140px;object-fit:contain;background:#fff;padding:6px;border-radius:8px;">
        <div>
          <h3 style="margin:0">{{ c.name }}</h3>
          <p class="tiny" style="margin:2px 0 0;color:var(--muted)">{{ c.person }} — {{ c.role }}</p>
        </div>
      </div>
      <p style="margin:4px 0 0">{{ c.description }}</p>
      {%- if c.product -%}<p class="tiny" style="margin:0;color:var(--muted)">Product: {{ c.product }}</p>{%- endif -%}
      <div style="margin-top:8px">
        <a class="btn primary" href="{{ c.link }}" target="_blank" rel="noopener">{{ c.cta | default: "Learn more" }}</a>
        {%- if c.hashtag -%}<span class="pill" style="margin-left:8px">{{ c.hashtag }}</span>{%- endif -%}
      </div>
    </article>
  {%- endfor -%}
  </div>
</section>
