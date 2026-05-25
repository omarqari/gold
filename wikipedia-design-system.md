# Wikipedia Design System
## A Product-Designer's Replication Guide
*Extracted live from en.wikipedia.org/wiki/Edo_period — May 2026*
*Skin: Vector 2022 (skin-vector-2022)*

---

## 1. Design Philosophy

Wikipedia's Vector 2022 skin is a **content-first, editorial** design system. Its principles:

- **Typography drives hierarchy** — size and weight do all the heavy lifting; colour is almost entirely absent from headings
- **Extreme restraint** — two font families, five background colours, four text colours; nothing decorative
- **Borders, not boxes** — separation is achieved with 1px `#a2a9b1` lines, never with coloured backgrounds on headings
- **Left-anchored reading column** — content lives in a fixed-width column (~916px), flanked by navigation sidebars
- **Serifed titles, sans-serif body** — the famous heading font is Linux Libertine (web-safe fallback: Georgia → Times → Source Serif 4)

---

## 2. Color Palette

Every colour on Wikipedia. No exceptions.

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Body text** | `#202122` | `rgb(32, 33, 34)` | All paragraph text, default text |
| **Heading text** | `#101418` | `rgb(16, 20, 24)` | h1, h2, h3, h4 |
| **Secondary text** | `#404244` | `rgb(64, 66, 68)` | Muted UI labels |
| **Tertiary text** | `#54595d` | `rgb(84, 89, 93)` | Footer, captions secondary |
| **Link blue** | `#3366cc` | `rgb(51, 102, 204)` | All hyperlinks |
| **Page background** | `#f8f9fa` | `rgb(248, 249, 250)` | `<body>`, infobox bg, sidebar bg, figure bg |
| **White** | `#ffffff` | `rgb(255, 255, 255)` | Header/nav bar, image bg, left sidebar, content pane |
| **Border grey** | `#a2a9b1` | `rgb(162, 169, 177)` | All divider lines, infobox borders, sidebar borders, navbox borders |
| **Subtle border** | `#eaecf0` | `rgb(234, 236, 240)` | Light UI borders |
| **Black** | `#000000` | `rgb(0, 0, 0)` | Image borders only |
| **Navbox title bg** | `#ccccff` | `rgb(204, 204, 255)` | Navbox title row background |
| **Navbox group bg** | `#ddddff` | `rgb(221, 221, 255)` | Navbox group label background |
| **Navbox body bg** | `#fdfdfd` | `rgb(253, 253, 253)` | Navbox body background |
| **Image border** | `#c8ccd1` | `rgb(200, 204, 209)` | 1px border around thumbnail images |
| **Header bg** | `#ffffff` | `rgb(255, 255, 255)` | Top navigation bar |

---

## 3. Typography

### Font Stacks

```css
/* Heading font (h1, h2 only) */
font-family: "Linux Libertine", Georgia, Times, "Source Serif 4", serif;

/* Everything else */
font-family: sans-serif;
/* (Resolves to system sans — usually Helvetica Neue on Mac, Arial on Windows, Roboto on Android)
```

### Type Scale

| Element | Font Family | Size | Weight | Line-height | Color |
|---------|-------------|------|--------|-------------|-------|
| `h1` (page title) | Linux Libertine / serif | `28.8px` (1.8rem) | `400` normal | `39.6px` (1.375×) | `#101418` |
| `h2` (section) | Linux Libertine / serif | `24px` (1.5rem) | `400` normal | `33px` (1.375×) | `#101418` |
| `h3` (subsection) | sans-serif | `19.2px` (1.2rem) | `700` bold | `30.72px` (1.6×) | `#101418` |
| `h4` | sans-serif | `16px` (1rem) | `700` bold | `25.6px` (1.6×) | `#101418` |
| Body paragraph (`p`) | sans-serif | `16px` | `400` | `26px` (1.625×) | `#202122` |
| Body (`body`) | sans-serif | `16px` | `400` | `normal` | `#202122` |
| Links (`a`) | sans-serif | inherits | `700` bold | inherits | `#3366cc` |
| Figure caption | sans-serif | `14.144px` (~0.885rem) | `400` | inherits | `#202122` |
| Infobox text | sans-serif | `88%` (~14.08px) | `400` | `1.5em` | `#202122` |
| TOC links | sans-serif | `14px` | `400` | inherits | `#3366cc` |
| Navbox text | sans-serif | `88%` (~14.08px) | `400` | `1.5em` | `#202122` |
| Reference list | sans-serif | `14.4px` (0.9rem) | `400` | `23.4px` | `#202122` |
| Superscript refs `sup` | sans-serif | `12.8px` (0.8rem) | `400` | — | `#202122` |
| Footer text | sans-serif | ~`13px` | `400` | — | `#202122` |

### Key typographic details
- **No italic** on body text anywhere by default
- **h2 is NOT bold** — it uses the serif font at normal weight, which gives editorial weight without heaviness
- **h3 and below flip to bold sans-serif** — strong contrast with the light serif h2
- **Links are bold** — this is intentional and critical for scannability
- **Line-height ratio** for body: `26px / 16px = 1.625` — generous for long-form reading

---

## 4. Page Layout & Grid

### Macro Layout (viewport ~1440px wide)

```
┌────────────────────────────────────────────────────────────────────────┐
│  HEADER (.vector-header) — full width, white bg, 66px tall             │
│  [hamburger] [Wikipedia logo] ────────── [search] [user tools]         │
├────────────┬───────────────────────────────────┬───────────────────────┤
│            │                                   │                       │
│ LEFT       │  CONTENT AREA                     │ RIGHT COLUMN          │
│ SIDEBAR    │  .mw-content-container            │ .vector-column-end    │
│ 208px      │  916px                            │ 196px                 │
│            │                                   │                       │
│ [TOC]      │  [Article title h1]               │ [empty / future use]  │
│ [nav menu] │  [Article body]                   │                       │
│            │  [Images float right]             │                       │
│            │  [Infobox float right]            │                       │
│            │  [Section headings h2…]           │                       │
│            │  [Navboxes]                       │                       │
│            │  [Categories]                     │                       │
├────────────┴───────────────────────────────────┴───────────────────────┤
│  FOOTER (#footer) — full width                                          │
└────────────────────────────────────────────────────────────────────────┘
```

### Grid CSS (actual computed values)

```css
/* Outer page container */
.mw-page-container {
  max-width: 1596px;
  padding: 0 44px;
  margin: 0 auto; /* centered */
}

/* Content grid (#content / .mw-body) */
#content {
  display: grid;
  grid-template-columns: 916px 196px; /* content | right-col */
  grid-template-areas:
    "titlebar-cx ."
    "titlebar columnEnd"
    "toolbar columnEnd"
    "content columnEnd";
  gap: normal 24px;
  width: 1136px;
}

/* Content area */
#mw-content-text, #bodyContent, .mw-parser-output {
  width: 916px;
  margin-top: 16px;
}

/* Left sidebar */
.vector-column-start {
  width: 208px; /* fixed */
}
```

### Content column max effective width
- **916px** is the reading column width at standard desktop
- At very wide screens (> 1596px) the page container stops growing — content stays centered
- Left sidebar: **208px** | Gap: **24px** | Content: **916px** | Right col: **196px** = 1136px total (+ page padding)

---

## 5. Header & Navigation Bar

```css
.vector-header {
  background-color: #ffffff;
  height: 66px;
  /* no border-bottom — separation is implied by content starting */
}
```

- Full-width white bar, 66px tall
- Contains: hamburger menu, Wikipedia logo (wordmark), search box, user account links
- Logo: "Wikipedia" wordmark in Linux Libertine (same font as headings)
- Search box: rounded, collapses on narrow viewports

---

## 6. Left Sidebar (Table of Contents)

The TOC lives in the left column and scrolls with the page (sticky pinned).

```css
.vector-toc {
  font-size: 14px;
  font-family: sans-serif;
  color: #202122;
  background: transparent;
  /* no border, no background */
}

.vector-toc-contents {
  list-style: none;
  padding: 0;
  margin: 0;
}

.vector-toc-link {
  color: #3366cc;
  text-decoration: none;
  font-size: 14px;
  font-weight: 400;
}

/* Section label (e.g., "1.2") */
.vector-toc-numb {
  /* small, muted, display inline before title */
}
```

- TOC heading ("Contents") uses `.vector-pinnable-header-label`
- Hierarchy shown by indentation, not by colour or weight difference
- No bullets — `list-style: none`
- Links are the standard blue `#3366cc`

---

## 7. Article Title (h1)

```css
#firstHeading .mw-page-title-main {
  font-family: "Linux Libertine", Georgia, Times, "Source Serif 4", serif;
  font-size: 28.8px;    /* 1.8rem */
  font-weight: 400;     /* NOT bold */
  line-height: 39.6px;  /* 1.375 ratio */
  color: #101418;
  margin: 0;
  padding: 0;
}
```

**Critical detail:** The title is NOT bold. The serif font provides gravitas at normal weight.

---

## 8. Section Headings (h2, h3, h4)

### h2 — Section heading

```css
/* Wrapper div handles the border */
.mw-heading2 {
  border-bottom: 1px solid #a2a9b1;
  padding-bottom: 4px;       /* ~4.08px */
  margin-bottom: 6px;
  color: #101418;
}

/* The actual <h2> tag */
.mw-heading2 h2 {
  font-family: "Linux Libertine", Georgia, Times, "Source Serif 4", serif;
  font-size: 24px;      /* 1.5rem */
  font-weight: 400;     /* normal weight! */
  line-height: 33px;
  color: #101418;
  margin: 0 0 6px;
  /* no border on h2 itself — border is on the wrapper .mw-heading2 */
}
```

### h3 — Subsection heading

```css
.mw-heading3 h3 {
  font-family: sans-serif;
  font-size: 19.2px;    /* 1.2rem */
  font-weight: 700;
  line-height: 30.72px; /* 1.6 ratio */
  color: #101418;
  margin: 0 0 4.8px;
  /* NO border-bottom on h3 */
}
```

### h4 — Sub-subsection

```css
h4 {
  font-family: sans-serif;
  font-size: 16px;      /* same as body */
  font-weight: 700;
  line-height: 25.6px;
  color: #101418;
  margin: 0 0 4px;
}
```

**Key pattern:** h2 → serif/light with bottom border. h3 → sans/bold, no border. h4 → sans/bold/body-size, no border.

---

## 9. Body Paragraphs

```css
.mw-parser-output p {
  font-family: sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 26px;    /* 1.625 — generous */
  color: #202122;
  margin: 8px 0 16px;   /* top: 8px, bottom: 16px */
  padding: 0;
}
```

---

## 10. Links

```css
.mw-parser-output a {
  color: #3366cc;
  font-weight: 700;        /* bold — important for scannability */
  text-decoration: none;   /* no underline by default */
}

.mw-parser-output a:hover {
  text-decoration: underline;  /* underline appears on hover */
}

/* External links get a small arrow icon via CSS ::after */
.external {
  /* background-image: external link icon */
}
```

---

## 11. Infobox

The infobox is a right-floating table. Wikipedia uses two parallel infobox systems:

### Standard (desktop Vector skin) Infobox

```css
.infobox {
  border: 1px solid #a2a9b1;
  color: black;
  padding: 0.2em;              /* ~3.2px */
  font-size: 88%;              /* ~14.08px at 16px base */
  line-height: 1.5em;
  border-spacing: 3px;
  margin: 0.5em 0;
  /* NOTE: float:right is set inline on the table element */
  /* typical: float: right; clear: right; margin: 0.5em 0 1em 1em; */
  background-color: #f8f9fa;
}

/* Caption = the bold title at the top of the infobox */
.infobox caption,
.infobox .infobox-above,
.infobox .infobox-title {
  font-size: 125%;     /* 125% of 88% = 110% of base = ~17.6px */
  font-weight: bold;
  text-align: center;
  padding: 0.2em;
}

/* Label column (left, grey) */
.infobox th,
.infobox-label {
  vertical-align: top;
  text-align: left;
  background-color: #eaecf0;   /* light grey — common pattern */
  padding: 7px 10px;
  font-weight: bold;
}

/* Data column (right) */
.infobox td,
.infobox-data {
  vertical-align: top;
  text-align: left;
  border-bottom: 1px solid #a2a9b1;
  padding: 7px 10px;
}

/* Full-width rows (images, subheadings) */
.infobox .infobox-header,
.infobox .infobox-subheader,
.infobox .infobox-image,
.infobox .infobox-full-data,
.infobox .infobox-below {
  text-align: center;
}
```

### Infobox HTML Structure (person biography)

```html
<table class="infobox biography vcard">
  <caption class="infobox-title fn">Hiro Nakamura</caption>
  <tbody>
    <!-- Optional portrait image row -->
    <tr>
      <td class="infobox-image" colspan="2">
        <img src="portrait.jpg" width="220">
        <div class="infobox-caption">Caption text</div>
      </td>
    </tr>
    <!-- Data rows -->
    <tr>
      <th class="infobox-label">Born</th>
      <td class="infobox-data">1592, Hirado</td>
    </tr>
    <tr>
      <th class="infobox-label">Died</th>
      <td class="infobox-data">c. 1648 (aged ~55)</td>
    </tr>
    <tr>
      <th class="infobox-label">Occupation</th>
      <td class="infobox-data">Merchant navigator</td>
    </tr>
    <!-- Subheader row -->
    <tr>
      <th class="infobox-header" colspan="2">Known for</th>
    </tr>
    <tr>
      <td class="infobox-full-data" colspan="2">The Sake Barrel Letter</td>
    </tr>
  </tbody>
</table>
```

**Positioning:** `float: right; clear: right; margin: 0.5em 0 1em 1em;` — standard right float with left margin to push body text away.

---

## 12. Thumbnail Images (figures)

```css
/* The <figure> wrapper */
figure.mw-default-size {
  display: table;         /* critical — makes it shrink-wrap */
  float: right;
  clear: right;
  margin: 8px 0 20.8px 22.4px;   /* top right bottom left */
  background-color: #f8f9fa;
  text-align: center;
  width: 259px;           /* = image width + 2×3px margin + 2×1px border = 250+9 */
}

/* The image itself */
figure img {
  display: block;
  border: 1px solid #c8ccd1;
  padding: 0;
  margin: 3px;
  background-color: #ffffff;
  width: 250px;           /* default thumb width */
}

/* Caption */
figcaption {
  font-size: 14.144px;   /* ~0.885rem */
  font-weight: 400;
  font-style: normal;    /* NOT italic — common misconception */
  color: #202122;
  background-color: #f8f9fa;
  padding: 0 6px 6px;
  text-align: left;      /* left-aligned despite figure being centered */
  display: table-caption;
  caption-side: bottom;
}
```

**Key:** `display: table` on the figure is what makes the caption width match the image width exactly.

---

## 13. Wikitable (data tables)

```css
.wikitable {
  font-size: 16px;
  background-color: #f8f9fa;
  border: 1px solid #a2a9b1;
  border-collapse: collapse;
  margin: -8px 0 16px;  /* negative top margin to sit flush with preceding content */
}

.wikitable th {
  background-color: #eaecf0;
  font-weight: bold;
  border: 1px solid #a2a9b1;
  padding: 4px 8px;     /* approx */
  text-align: center;
}

.wikitable td {
  border: 1px solid #a2a9b1;
  padding: 4px 8px;
  vertical-align: top;
}
```

---

## 14. Navbox (bottom navigation templates)

```css
.mw-parser-output .navbox {
  box-sizing: border-box;
  border: 1px solid #a2a9b1;
  width: 100%;
  clear: both;
  font-size: 88%;          /* ~14.08px */
  text-align: center;
  padding: 1px;
  margin: 1em auto 0;
  background-color: #fdfdfd;
  color: inherit;
}

/* Title bar (dark blue/purple header row) */
.navbox-title {
  font-weight: bold;
  font-size: 14.08px;
  background-color: #ccccff;   /* light periwinkle */
  color: #202122;
  padding: 3.52px 14.08px;
  text-align: center;
}

/* Group labels (left column labels) */
.navbox-group {
  font-weight: bold;
  background-color: #ddddff;   /* slightly lighter periwinkle */
  padding: 0.25em 1em;
  line-height: 1.5em;
  text-align: right;           /* right-aligned! */
  white-space: nowrap;
}

/* List cells (alternating) */
.navbox-list {
  font-size: 14.08px;
  text-align: left;
}

.navbox-list-odd  { background-color: #f7f8ff; }
.navbox-list-even { background-color: #f0f0ff; }
```

---

## 15. Reference Superscripts & Reference List

```css
/* Inline superscript citation [1] */
sup.reference {
  font-size: 12.8px;   /* 0.8rem */
  vertical-align: super;
  line-height: 1;
}

sup.reference a {
  color: #3366cc;
  font-weight: 400;    /* NOT bold unlike regular links */
  text-decoration: none;
}

/* Reference list (at bottom of article) */
.mw-references-wrap ol.references {
  font-size: 14.4px;   /* 0.9rem */
  line-height: 23.4px;
  margin: 4.32px 0 7.2px 46.08px;  /* indented list */
  color: #202122;
}

.mw-references-wrap ol.references li {
  font-size: 14.4px;
  margin-bottom: 1.44px;
}
```

---

## 16. Ambox (Article Notice Banners)

These are the coloured warning boxes (e.g., "This article needs citations").

```css
.ambox {
  /* Full-width box, sits above the article body */
  width: 100%;  /* ~732px in content column */
  background-color: #f8f9fa;
  border: 1px solid #a2a9b1;
  /* Left-side coloured stripe added via border-left on inner cell */
}

/* Common ambox types */
.ambox-content   { border-left: 10px solid #f28500; }  /* orange — content issues */
.ambox-style     { border-left: 10px solid #f4c430; }  /* yellow — style issues */
.ambox-notice    { border-left: 10px solid #3366cc; }  /* blue — general notice */
.ambox-serious   { border-left: 10px solid #b32424; }  /* red — serious issues */
```

---

## 17. Categories Box

```css
#catlinks {
  /* Sits at very bottom of article, above footer */
  font-size: 14px;
  border-top: 1px solid #a2a9b1;
  padding: 5px 0;
  color: #202122;
}

#catlinks a {
  color: #3366cc;
}

/* "Categories:" label */
#catlinks .mw-normal-catlinks::before {
  content: "";  /* actual label is in the <a> tag */
}
```

HTML structure:
```html
<div id="catlinks">
  <div id="mw-normal-catlinks">
    <a href="/wiki/Help:Category">Categories</a>:
    <ul>
      <li><a href="/wiki/Category:Edo_period">Edo period</a></li>
      <li><a href="/wiki/Category:History_of_Japan">History of Japan</a></li>
    </ul>
  </div>
</div>
```

---

## 18. Footer

```css
#footer {
  /* Three child lists */
  /* #footer-info — "Last edited on…" metadata */
  /* #footer-places — Privacy policy, About Wikipedia, etc. */
  /* #footer-icons.noprint — Wikimedia logo icons */
}

#footer-info li,
#footer-places li {
  display: inline; /* horizontal list */
  font-size: ~13px;
  color: #54595d;  /* muted text */
}
```

---

## 19. Complete CSS Variables Reference

Wikipedia uses both hardcoded hex values and CSS custom properties. The key ones:

```css
:root {
  --color-base:                      #202122;
  --color-base-fixed:                #202122;
  --color-emphasized:                #101418;
  --color-subtle:                    #54595d;
  --color-placeholder:               #72777d;
  --color-disabled:                  #a2a9b1;
  --color-inverted:                  #ffffff;
  --color-link:                      #3366cc;
  --color-link-visited:              #6b4ba1;  /* purple — visited links */
  --color-link-red:                  #d33;     /* red links = missing articles */

  --background-color-base:           #ffffff;
  --background-color-interactive:    #eaecf0;
  --background-color-interactive-subtle: #f8f9fa;
  --background-color-neutral:        #eaecf0;
  --background-color-neutral-subtle: #f8f9fa;

  --border-color-base:               #a2a9b1;
  --border-color-muted:              #c8ccd1;
  --border-color-subtle:             #eaecf0;
}
```

---

## 20. Replication Checklist

To make an HTML page pass as Wikipedia, these are the non-negotiable details:

- [ ] **Font stack:** `"Linux Libertine", Georgia, Times, "Source Serif 4", serif` for h1 and h2
- [ ] **h1 weight is 400** (not bold) — this is the single most-spotted mistake
- [ ] **h2 weight is 400** (not bold) — same
- [ ] **h3 is 700 bold sans-serif** (switch from serif to sans at h3)
- [ ] **Section divider:** `border-bottom: 1px solid #a2a9b1` on the `.mw-heading2` wrapper div, NOT on the h2 tag
- [ ] **Body text:** 16px, sans-serif, `#202122`, line-height 26px
- [ ] **Links are bold** (`font-weight: 700`) in body text — this is often missed
- [ ] **Body background:** `#f8f9fa` — off-white, not pure white
- [ ] **Content pane background:** transparent (the white comes from the header/sidebars)
- [ ] **Infobox:** `float: right; clear: right; margin: 0.5em 0 1em 1em`; 1px `#a2a9b1` border; 88% font-size; `background: #f8f9fa`
- [ ] **Figure/thumb:** `display: table` wrapper, `margin: 3px` on img, 1px `#c8ccd1` border on img
- [ ] **Caption NOT italic** — common mistake, Wikipedia captions are normal weight/style
- [ ] **Reference superscripts NOT bold** — unlike regular links
- [ ] **Visited links:** `#6b4ba1` purple
- [ ] **Red links** (missing articles): `#d33` red
- [ ] **Page title area:** `#101418` (slightly off-black, not pure `#202122`)
- [ ] **No decorative colors** — resist adding any blues/greens/greys to headings
- [ ] **Navbox title bg:** `#ccccff` (periwinkle) — not blue, not grey

---

## 21. Minimal HTML Template

```html
<!DOCTYPE html>
<html class="skin-vector skin-vector-2022" lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <title>Article Title - Wikipedia</title>
  <style>
    /* === RESET === */
    * { box-sizing: border-box; }
    body {
      font-family: sans-serif;
      font-size: 16px;
      color: #202122;
      background-color: #f8f9fa;
      margin: 0;
      padding: 0;
    }

    /* === LAYOUT === */
    .mw-page-container {
      max-width: 1596px;
      margin: 0 auto;
      padding: 0 44px;
    }
    #content {
      display: grid;
      grid-template-columns: 1fr;  /* simplified: no sidebar */
      max-width: 960px;
    }
    .mw-parser-output {
      max-width: 916px;
      margin-top: 16px;
    }

    /* === TITLE === */
    #firstHeading {
      font-family: "Linux Libertine", Georgia, Times, "Source Serif 4", serif;
      font-size: 1.8rem;     /* 28.8px */
      font-weight: 400;
      line-height: 1.375;
      color: #101418;
      margin: 0;
      padding: 0 0 4px;
      border-bottom: 1px solid #a2a9b1;
    }

    /* === SECTION HEADINGS === */
    .mw-heading2 {
      border-bottom: 1px solid #a2a9b1;
      padding-bottom: 4px;
      margin-bottom: 6px;
    }
    .mw-heading2 h2 {
      font-family: "Linux Libertine", Georgia, Times, "Source Serif 4", serif;
      font-size: 1.5rem;     /* 24px */
      font-weight: 400;
      color: #101418;
      margin: 24px 0 0;
      padding: 0;
    }
    .mw-heading3 h3 {
      font-family: sans-serif;
      font-size: 1.2rem;     /* 19.2px */
      font-weight: 700;
      color: #101418;
      margin: 16px 0 4px;
    }
    .mw-heading4 h4 {
      font-family: sans-serif;
      font-size: 1rem;
      font-weight: 700;
      color: #101418;
      margin: 12px 0 4px;
    }

    /* === BODY TEXT === */
    .mw-parser-output p {
      font-size: 16px;
      line-height: 26px;
      margin: 8px 0 16px;
    }

    /* === LINKS === */
    .mw-parser-output a {
      color: #3366cc;
      font-weight: 700;
      text-decoration: none;
    }
    .mw-parser-output a:hover { text-decoration: underline; }
    .mw-parser-output a:visited { color: #6b4ba1; }
    .new { color: #d33; }  /* red link = missing article */

    /* === INFOBOX === */
    .infobox {
      float: right;
      clear: right;
      margin: 0.5em 0 1em 1em;
      border: 1px solid #a2a9b1;
      background-color: #f8f9fa;
      font-size: 88%;
      line-height: 1.5em;
      border-spacing: 3px;
      padding: 0.2em;
    }
    .infobox caption,
    .infobox-above {
      font-size: 125%;
      font-weight: bold;
      text-align: center;
      padding: 0.2em;
    }
    .infobox th, .infobox-label {
      vertical-align: top;
      text-align: left;
      padding: 7px 10px;
      font-weight: bold;
      background-color: #eaecf0;
    }
    .infobox td, .infobox-data {
      vertical-align: top;
      text-align: left;
      padding: 7px 10px;
      border-bottom: 1px solid #a2a9b1;
    }
    .infobox-image, .infobox-full-data,
    .infobox-header, .infobox-below { text-align: center; }

    /* === FIGURES / THUMBNAILS === */
    figure.thumb, figure.mw-default-size {
      display: table;
      float: right;
      clear: right;
      margin: 8px 0 21px 22px;
      background-color: #f8f9fa;
      text-align: center;
    }
    figure.thumb img {
      display: block;
      border: 1px solid #c8ccd1;
      margin: 3px;
      background-color: #ffffff;
    }
    figcaption {
      display: table-caption;
      caption-side: bottom;
      font-size: 0.875rem;  /* ~14px */
      font-weight: 400;
      font-style: normal;   /* NOT italic */
      padding: 0 6px 6px;
      text-align: left;
    }

    /* === REFERENCES === */
    sup.reference a {
      color: #3366cc;
      font-weight: 400;  /* NOT bold */
      font-size: 0.8rem;
    }
    .mw-references-wrap ol {
      font-size: 0.9rem;
      line-height: 1.625;
      margin-left: 2.9em;
    }

    /* === NAVBOX === */
    .navbox {
      border: 1px solid #a2a9b1;
      width: 100%;
      clear: both;
      font-size: 88%;
      text-align: center;
      padding: 1px;
      margin: 1em auto 0;
      background-color: #fdfdfd;
    }
    .navbox-title {
      background-color: #ccccff;
      font-weight: bold;
      padding: 0.25em 1em;
    }
    .navbox-group {
      background-color: #ddddff;
      font-weight: bold;
      padding: 0.25em 1em;
      text-align: right;
      white-space: nowrap;
    }

    /* === CATEGORIES === */
    #catlinks {
      border-top: 1px solid #a2a9b1;
      padding: 5px 0;
      font-size: 14px;
      clear: both;
      margin-top: 1em;
    }
    #catlinks a { color: #3366cc; }
    #catlinks ul {
      display: inline;
      list-style: none;
      padding: 0;
      margin: 0;
    }
    #catlinks li { display: inline; }
    #catlinks li::after { content: " · "; }
    #catlinks li:last-child::after { content: ""; }
  </style>
</head>
<body>
  <div class="mw-page-container">
    <main id="content">
      <h1 id="firstHeading">
        <span class="mw-page-title-main">Article Title</span>
      </h1>
      <div id="bodyContent">
        <div class="mw-parser-output">
          <!-- Infobox (right-floated) -->
          <table class="infobox biography vcard">
            <caption class="infobox-title">Person Name</caption>
            <tbody>
              <tr><td class="infobox-image" colspan="2"><img src="portrait.jpg" width="220"></td></tr>
              <tr><th class="infobox-label">Born</th><td class="infobox-data">Date, Place</td></tr>
              <tr><th class="infobox-label">Died</th><td class="infobox-data">Date</td></tr>
            </tbody>
          </table>

          <!-- Article text -->
          <p><b>Article Title</b> is a...</p>

          <!-- Section -->
          <div class="mw-heading mw-heading2">
            <h2>Section Name</h2>
          </div>
          <p>Content...</p>

          <!-- Thumbnail image -->
          <figure class="mw-default-size">
            <a href="#"><img src="image.jpg" width="250" height="300"></a>
            <figcaption>Caption text here.</figcaption>
          </figure>

          <!-- References heading -->
          <div class="mw-heading mw-heading2"><h2>References</h2></div>
          <div class="mw-references-wrap">
            <ol class="references">
              <li id="cite_note-1">↑ Source text here.</li>
            </ol>
          </div>

          <!-- Categories -->
          <div id="catlinks">
            <div id="mw-normal-catlinks">
              <a href="#">Categories</a>:
              <ul>
                <li><a href="#">Category Name</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</body>
</html>
```

---

*End of Wikipedia Design System document. All values extracted live from en.wikipedia.org using the Vector 2022 skin at 1440px viewport width.*
