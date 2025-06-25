# Styling Options for Web Component Mode

## Use Swiper’s CSS variables

Swiper provides CSS variables to customise its appearance from outside the component, for example:

```css
swiper-container {
  --swiper-navigation-color: #000;
  --swiper-pagination-color: #ff5722;
  --swiper-theme-color: #2196f3;
  --swiper-navigation-size: 24px;
  --swiper-pagination-bullet-size: 10px;
}
```

These override styles inside the Shadow DOM.

## Style slide content via global CSS

You can style inside each <swiper-slide> if you treat it like a normal HTML element:

```html
<swiper-slide>
  <div class="card">
    <h3>Slide Title</h3>
    <p>Content here</p>
  </div>
</swiper-slide>
```

```css
.card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

This works because you’re styling your own HTML inside the slide, not the Shadow DOM.

## Don't try to style .swiper-slide directly

This won't work:

```css
swiper-slide {
  padding: 20px; /* this style won't apply */
}
```

But this will work if you target children inside:

```css
swiper-slide > div {
  padding: 20px;
}
```
