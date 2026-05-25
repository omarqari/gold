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
| `index.html` | **The live Wikipedia-style page** — deployed to wikipedia.space. Fully self-contained with all aged images embedded as base64. |
| `hiro-nakamura-merchant.html` | Original working copy (same content as index.html, kept as backup) |
| `img/` | Original photos: IMG_0893–0894 (coin front/back), IMG_0895–0898 (barrel), IMG_0899 (note) |
| `aged_images/` | Processed aged versions: daguerreotype (coins), sepia documentary (barrel), manuscript (note) |
| `aged_b64.json` | Base64-encoded aged images used to embed in HTML — large file (~5MB), safe to delete |
| `age_images.py` | The PIL-based aging pipeline script; rerun if you add more photos |
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

### SEO
Keywords baked into the page meta tags: Hiro Nakamura, Japanese merchant, Manila Galleon, pirate coin, Hirado, Nakamura Correspondence, Sake Barrel Letter, Insulum Piratus, Vita Enim Piratus

Google typically indexes GitHub Pages within 1–3 days of going live.

---

## Next Steps / Ideas

### Immediate (do today)
- [ ] Enable "Enforce HTTPS" in GitHub Pages settings (see above — wait ~1 hour after DNS set)
- [ ] Verify the page loads correctly at https://wikipedia.space
- [ ] Check that images render properly (all embedded as base64, should work offline too)

### If She Keeps Digging
These rabbit holes can be added if she remains curious after finding the Wikipedia page:

- [ ] **Hirado Heritage Trust page** — a fake preservation society page that references the Nakamura family and the Sake Barrel Letter
- [ ] **Numismatics forum thread** — a fake old forum post where a collector discusses the INSULUM PIRATUS / VITA ENIM PIRATUS inscription and concludes it's a private commission piece, not standard Spanish mint
- [ ] **Fake 1987 estate sale catalogue** — "Lot 114, Tanaka Collection, San Francisco" — a scanned PDF of an auction catalogue entry describing the Nakamura letters
- [ ] **Google Maps pin** — "Nakamura Harbor Plaque, Hirado" — a pin at the real Hirado port with a fake historical marker description
- [ ] **Woodblock print image** — a Meiji-era style woodblock portrait of Hiro Nakamura (generate via image AI, e.g. Nanobanana/Gemini). Prompt written, image not yet generated. Would replace the placeholder in the Wikipedia infobox.

### Content Improvements
- [ ] Add the woodblock print portrait to the Wikipedia page infobox (currently no portrait — historically plausible but a portrait would add authenticity)
- [ ] Consider adding a second "external link" in the article to a fake academic reference (e.g., a fake JSTOR abstract)

---

## Git / Deployment

- **Repo:** https://github.com/omarqari/gold
- **Branch:** main
- **Deploy:** automatic — any push to main updates the live site within ~2 min
- **To update the page:** edit `index.html`, then `git add index.html && git commit -m "update" && git push`
