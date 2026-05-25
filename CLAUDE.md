# Gold — Project CLAUDE.md

This folder contains the files for **the Hiro Nakamura treasure hunt**, an ongoing interactive fiction project built for Omar's daughter. She found a pirate coin and a sake barrel in her grandmother's house and became convinced the coin is authentic historical treasure. The goal is to build out a believable lore trail that she can follow, ending in satisfying closure (the coin stays in the family, no need to look further).

---

## The Canon

### The Coin
- A novelty/replica **Spanish quadruple escudo** (not a real historical coin)
- Marked with the denomination **"4"** — she correctly identified this as a "double doubloon" (real logic: a doubloon = 2 escudos, so "4" = quadruple escudo, the largest denomination)
- Inscribed: **VITA ENIM PIRATUS** ("for the life of a pirate") and **INSULUM PIRATUS** ("Island of Pirates")
- Found in a **secret hidden compartment in an old bed** at grandmother's house

### The Sake Barrel
- A traditional Japanese **komodaru** (straw-wrapped sake barrel)
- Marked **高級清酒** (kōkyū seishu = "premium sake") in red characters
- Omar hid a crumpled note inside through the wooden spigot opening
- She found the note a few days after it was hidden

### The Note (written by Omar, signed "Hiro Nakamura")
> *"If you find my family coin, do not sell it. It has special powers to keep the holder's family healthy and safe. This is ancient pirate treasure stolen from Spain in New Spain that I found in Japan. Keep it secret."*
> — Hiro Nakamura

### Hiro Nakamura (the fictional historical figure)
- **Full name:** Nakamura Hirō (中村 宏)
- **Born:** 1592, Hirado, Hizen Province (now Nagasaki Prefecture)
- **Died:** c. 1648, Hirado
- **Occupation:** Japanese merchant navigator, harbor interpreter
- **Background:** Son of a Dutch/Portuguese trade interpreter; learned Portuguese and Spanish; traveled Manila Galleon trade routes
- **The coin:** Acquired c. 1628–1631 from a Portuguese intermediary in Manila; believed to have protective powers (Shinto kotodama influence)
- **The Nakamura Correspondence:** 11 letters to his brother Kenji (c. 1629–1645); discovered in a 1987 US estate sale (Tanaka Collection, San Francisco)
- **The Sake Barrel Letter:** Most famous letter (c. 1639), found hidden in a komodaru; contains the coin instructions
- **Easter egg:** Shares name with Hiro Nakamura from NBC's *Heroes* (2006) — Omar's favorite show. The Wikipedia article acknowledges this as a "coincidence."

### How the Trail Ends
The Wikipedia article states the coin "has remained within a private family collection" per Nakamura's instructions, has never been offered for sale, and "its current whereabouts are known only to the family in question, who have declined to speak with researchers." This gives her a satisfying, closed ending — the coin belongs with whoever holds it.

---

## Files in This Folder

| File | Description |
|------|-------------|
| `index.html` | **The live Wikipedia-style page** — deployed to wikipedia.space. Vector 2022 fidelity rebuild (May 25 2026). References JPGs in `assets/`. |
| `index-v1.html` | First version of the page — hand-rolled Wikipedia approximation with base64-embedded aged images. Kept as backup. |
| `hiro-nakamura-merchant.html` | Original working copy from the very first build (May 25 2026). Backup. |
| `wikipedia-design-system.md` | **Full Wikipedia design spec** — extracted live from en.wikipedia.org. Typography, colors, layout, every component. Use this before editing index.html. |
| `assets/` | Final web-ready images used by `index.html`: cropped JPGs (~85–200KB each) plus `wikipedia-logo.svg` (the real Wikipedia 25-year wordmark). |
| `rev_images/` | Source images (large PNGs, ~8–10MB each) from which `assets/` was derived. Originals — do not edit. |
| `img/` | Original phone photos: IMG_0893–0894 (coin front/back), IMG_0895–0898 (barrel), IMG_0899 (note). |
| `aged_images/` | Daguerreotype / sepia / manuscript treatments of `img/`. Used by `index-v1.html`. Not used by current `index.html`. |
| `aged_b64.json` | Base64-encoded aged images embedded in `index-v1.html`. Large file (~5MB), `.gitignore`'d. Safe to delete. |
| `age_images.py` | PIL-based aging pipeline. Rerun if you add more photos. |
| `age_images.py` | The aging pipeline script (PIL-based); rerun if you add more photos |
| `CNAME` | `wikipedia.space` — tells GitHub Pages the custom domain. |
| `CLAUDE.md` | This file |

---

## Hosting — LIVE ✅

The page is live at **[wikipedia.space](https://wikipedia.space)**

### Infrastructure
- **Domain:** `wikipedia.space` — registered at [Spaceship.com](https://spaceship.com), May 25 2026
- **Hosting:** GitHub Pages — repo `omarqari/gold` (public), `main` branch, root folder
- **Live URL:** https://wikipedia.space (custom domain) + https://omarqari.github.io/gold/ (GitHub fallback)

### DNS Records (set at Spaceship Advanced DNS)
| Host | Type | Value | TTL |
|------|------|-------|-----|
| @ | A | 185.199.108.153 | 30 min |
| @ | A | 185.199.109.153 | 30 min |
| @ | A | 185.199.110.153 | 30 min |
| @ | A | 185.199.111.153 | 30 min |
| www | CNAME | omarqari.github.io | 30 min |

### Remaining Setup Step
- [ ] **Enable "Enforce HTTPS"** at https://github.com/omarqari/gold/settings/pages
  - Will become available ~60 min after DNS propagation (set May 25 2026 ~11:30 AM)
  - GitHub auto-provisions the Let's Encrypt SSL cert once DNS resolves
  - Once the checkbox is clickable, check it — HTTP will then redirect to HTTPS automatically

### SEO
Keywords baked into the page meta tags: Hiro Nakamura, Japanese merchant, Manila Galleon, pirate coin, Hirado, Nakamura Correspondence, Sake Barrel Letter, Insulum Piratus, Vita Enim Piratus

Google typically indexes GitHub Pages within 1–3 days of going live.

---

## Next Steps / Ideas

### Immediate — deploy rev 2
- [ ] Copy the new files from this session into the local repo and push (see commit instructions below).
- [ ] **Enable "Enforce HTTPS"** at https://github.com/omarqari/gold/settings/pages if not already on. The checkbox becomes available ~1 hour after DNS is set.
- [ ] Open https://wikipedia.space on phone and desktop to confirm the rebuild renders, all `assets/` images load, and the page still beats the Google rank for "Hiro Nakamura merchant".

### Design polish that could still be tightened
The Vector 2022 rebuild is close but a real-Wikipedia-vs-ours diff still shows a few residual gaps:

- [ ] **Sticky TOC scroll-spy.** Real Wikipedia highlights the currently-visible section in the TOC as you scroll. Currently the TOC is decorative.
- [ ] **Disclosure-caret toggling.** The little ▾ on parent TOC items is visual-only; clicking it does nothing. Wiring up `aria-expanded` toggling would take ~10 lines of JS.
- [ ] **The "3 languages" pill** in the title bar is static. Could open a dropdown.
- [ ] **Visited-link purple** (`#6b4ba1`) is set in CSS but only fires for real `:visited` links — not for `href="#"` hash links. Some article links should point to real Wikipedia articles so the visited state actually triggers.
- [ ] **Mobile layout.** The breakpoints at 1280px and 900px work but haven't been tested rigorously on phone. Most of her use will likely be on desktop, but worth a quick pass.

### Portrait
- [x] ~~Generate Meiji-era woodblock portrait of Hiro Nakamura~~ — done; `assets/hiro-portrait.jpg` is in the infobox.

### If She Keeps Digging
These rabbit holes can be added if she remains curious after finding the Wikipedia page. Build in order — each one adds a new layer of corroboration:

1. [ ] **Numismatics forum thread** — a fake old collector forum post (e.g., CoinTalk style) where someone discusses the INSULUM PIRATUS / VITA ENIM PIRATUS inscription and concludes it's a private commission piece, not standard Spanish mint output. Gives her a "dead end" that still confirms the coin is real.

2. [ ] **Fake 1987 estate sale catalogue PDF** — "Lot 114, Tanaka Collection, San Francisco" — a scanned, aged PDF of an auction catalogue entry describing the Nakamura letters and the coin. References the Wikipedia article as a source. Host on GitHub Pages as a separate file.

3. [ ] **Hirado Heritage Trust page** — a fake Japanese preservation society page (in English, with some Japanese) that references the Nakamura family harbor plaque and the Sake Barrel Letter. Should look like a mid-2000s institutional website.

4. [ ] **Google Maps pin** — "Nakamura Harbor Plaque, Hirado-shi, Nagasaki" — a Business/Place pin at the real Hirado port (33.3667° N, 129.5500° E) with a historical marker description. Anyone who searches will find it.

5. [ ] **Fake JSTOR abstract** — a fake academic reference for a paper titled something like *"Kotodama and Commerce: Protective Talisman Beliefs Among Edo-Period Merchant Navigators"*, Journal of Japanese Studies, 2003. Just needs a believable URL and abstract — she's unlikely to try to access the full paper.

6. [ ] **Wikipedia Talk page** for `Hiro_Nakamura_(merchant)` — editors debating the article's reliability, someone questioning the Tanaka Collection provenance, another defending it, a closed thread about a proposed merge with `Hiro Nakamura (Heroes)`. Extremely convincing if she clicks the Talk tab.

---

## Session Log

| Date | What happened |
|------|---------------|
| May 25 2026 | Project created. Registered wikipedia.space, set up GitHub Pages, built and deployed index.html with aged images embedded as base64. DNS pointed at GitHub Pages. |
| May 25 2026 | Extracted full Wikipedia Vector 2022 design system live from en.wikipedia.org/wiki/Edo_period. Saved as `wikipedia-design-system.md`. Covers typography, colors, layout grid, every component. |
| May 25 2026 | **Rev 2 — Vector 2022 fidelity rebuild.** Replaced the hand-rolled `index.html` with a faithful Vector 2022 implementation (old version kept as `index-v1.html`). Switched from aged-photo treatments to museum-quality `rev_images/` source files; cropped each into the `assets/` JPGs used by the article. Restructured the title bar (h1 → underline → tabs → siteSub), removed TOC section numbers, replaced the globe SVG with the real Wikipedia 25-year wordmark + puzzle-piece badge (`assets/wikipedia-logo.svg`). Updated the barrel canon (added 八海山 / Hakkaisan brand name and 謹醸 seal) to match the actual sake barrel. |

## Image Pipeline (current)

The current `index.html` uses six files in `assets/`:

| Asset | Crop source | What it shows |
|-------|-------------|---------------|
| `assets/hiro-portrait.jpg` (630×900) | `rev_images/what hiro might have looked like.png` | Tight crop on the figure of Hiro — excludes the AI-garbled "Field Notes" handwriting. Used in infobox. |
| `assets/coin-obverse.jpg` (900×900) | `rev_images/front of coin.png` | Tight square on the coin; excludes the museum-catalog stamp and AI sparkle. |
| `assets/coin-reverse.jpg` (900×900) | `rev_images/back of coin.png` | Same treatment. |
| `assets/coin-in-hand.jpg` (675×900) | `rev_images/coin in hand.png` | Portrait crop excluding the AI sparkle. |
| `assets/sake-barrel.jpg` (520×720) | `rev_images/barrel in museum.png` | Tight crop centered on the komodaru; excludes the AI-garbled placard and framed photo caption. **Note:** the barrel in this AI-generated museum photo has slightly garbled kanji on the top band; the article text describes the *real* barrel canon (高級清酒 / 八海山 / 謹醸). |
| `assets/wikipedia-logo.svg` | Provided by user | Real Wikipedia 25-year anniversary wordmark + puzzle-piece badge. Sized 25px tall in the header. |

To regenerate any of these, look at the inline crop coordinates documented in the session transcript or use the source dimensions table above as a starting point. The `rev_images/` source files are the authoritative originals.

---

## Git / Deployment

- **Repo:** https://github.com/omarqari/gold
- **Branch:** main
- **Deploy:** automatic — any push to main updates the live site within ~2 min
- **To update the page:** edit `index.html`, then:

```bash
git add index.html
git commit -m "describe what changed"
git push
```

- **Files NOT tracked by git** (intentionally or safe to ignore): none currently — all files are committed
- **Large files:** `aged_b64.json` (~5MB) is committed but safe to delete from the repo if it causes issues — the base64 is already embedded in `index.html`
