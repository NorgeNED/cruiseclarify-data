---
license: cc-by-4.0
language:
  - en
pretty_name: Real All-In Cruise Costs
tags:
  - cruise
  - travel
  - pricing
  - cruise-lines
  - tourism
size_categories:
  - n<1K
configs:
  - config_name: costs
    data_files: cruise-costs.csv
  - config_name: packages
    data_files: cruise-packages.csv
  - config_name: gratuities-tiers
    data_files: cruise-gratuities-tiers.csv
---

# Real All-In Cruise Costs — by CruiseClarify

> ### 📅 This is a dated snapshot — verified **June 2026**
> Cruise prices change constantly. Every figure here is a **point-in-time value, not
> live data**, accurate as of **June 2026**. The next quarterly refresh is due
> **September 2026** — after that, treat this copy as **historical**.
>
> **If you are reading or reusing this a quarter or more after June 2026, the numbers
> will have drifted.** Always pull the current version before quoting or republishing:
> - **Live figures:** https://cruiseclarify.com
> - **Latest dataset:** https://github.com/NorgeNED/cruiseclarify-data
>
> And confirm the current price with the cruise line before presenting any figure as today's price.

A clean, structured dataset of what cruise guests **actually pay** on board —
gratuities, Wi-Fi, drinks packages, specialty dining and surcharges — across 37
cruise lines, normalized to a single comparable basis.

Most published cruise figures are list prices buried in marketing pages or locked
inside calculators. This dataset is the opposite: one tidy table, every figure on
the same footing, sourced and dated, free to reuse with credit.

**Maintained by [CruiseClarify](https://cruiseclarify.com)** — independent cruise
cost research. Refreshed quarterly.

## What's in it

- **37 cruise lines** — mainstream, premium, premium-plus, luxury/all-inclusive,
  expedition, and UK/EU/Australian market variants.
- **Basis:** every monetary figure is **per person, per day, in the line's native
  currency** (USD unless the `currency` field says otherwise) — and reflects *what
  the guest actually pays*, not the headline list price.
- **Fields per line:** segment, currency, all-inclusive flag, how the drinks package
  works (`package_treatment`), gratuities, Wi-Fi (headline + range), whether drinking
  is covered by the fare (`drinks_included`), drinks-package price and service charge,
  specialty-dining range, onboard surcharge, and the verification date.

## Files

| File | Grain | What it is |
|------|-------|------------|
| `cruise-costs.csv`            | one row per line    | Flattened headline figures — opens in Excel / Numbers / Google Sheets. |
| `cruise-packages.csv`         | one row per package | Every drinks package, bundle, upgrade and credit, with `type` and `covers_*` flags so bundles are never confused with standalone drinks packages. |
| `cruise-gratuities-tiers.csv` | one row per cabin tier | Daily gratuities by cabin grade (standard, suite, Grills, Haven, Yacht Club…). |
| `cruise-costs.json`           | nested              | Full-fidelity structured data — keeps every tier, range, and source note. |

`cruise-costs.csv` is the quick-look table; the package and tier tables hold the
finer grain that doesn't fit one-row-per-line; `cruise-costs.json` is the complete
record (everything above plus the provenance notes behind each figure).

All CSVs are **UTF-8** (with a byte-order mark, so Excel renders € and £ correctly);
the JSON is plain UTF-8.

## A few definitions

- **`package_treatment`** — how a line's drinks package behaves:
  `drinks_only` (covers drinks alone), `bundle` (genuinely covers Wi-Fi /
  gratuities / dining too), `premium_fare` (near-inclusive fare; package is a drinks
  upgrade), `prepaid_credit` (Virgin's Bar Tab), `no_package` (Disney). Blank where a
  line isn't individually modeled in the calculator — its drinks story is still fully
  given by `drinks_included`, `drinks_package_offered` and `drinks_package_per_day`.
- **Blank cells** mean *not applicable / not separately tracked* — never "unknown."
  Examples: no `wifi_range` when a line has a single Wi-Fi price; no
  `drinks_package_*` when no package is sold; no specialty-dining figures for a few
  expedition lines we don't track venue-by-venue.
- **Wi-Fi headline** — the cheapest *unlimited* plan usable for general browsing;
  social-media-only tiers are excluded.
- **Service charge** — `drinks_service_pct` is the % added to a drinks package;
  `drinks_service_in_price` says whether that's already inside the quoted price.
- **`drinks_price_confidence`** — `verified` = a sourced figure; `approximate` = a
  ballpark (vague/unsourced basis — treat as indicative, not exact); blank = no priced
  package (all-inclusive, no package, or a credit model). So a number is never mistaken
  for solid when it isn't.
- **`drinks_included`** — is drinking covered by the fare itself? `yes` (all-inclusive
  lines), `partial` (some drinks included, e.g. wine/beer with meals), or `no` (you
  pay per drink or buy a package). This is separate from `drinks_package_offered`,
  which only says whether a paid add-on package is *sold*.
- **`dining_included`** — are the ship's restaurants covered by the fare? `yes`
  (specialty cover then reads `$0`), `partial` (most dining included, some venues
  charge), or `no` (specialty restaurants carry the cover charge shown in
  `specialty_dining_*`).
- **Included items read `$0`.** When an item is covered by the fare, its `*_included`
  flag is `yes` and its per-day figure is `0` — meaning *no extra cost*, not missing
  data. All-inclusive lines therefore show `0` across the cost columns. A **blank**
  cell means *not applicable* (e.g. no Wi-Fi price range, or no named package), never
  "unknown."

## Currency note

Figures are in each line's home-market currency (USD, GBP, EUR or AUD — see the
`currency` field). They are **not** converted to a single currency, because the
prices are set and charged in those currencies. Convert at your own rate if needed.

## Licence

**[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)**
— see `LICENSE`.

You may use, share, adapt and build on this data, including commercially, **as long
as you credit CruiseClarify**. Suggested attribution:

> Cruise cost data by **CruiseClarify** (https://cruiseclarify.com), June 2026 snapshot, CC BY 4.0.

Keeping the **snapshot date** in your attribution protects everyone: it tells *your*
readers how current the figures are, and it stops a June 2026 number being mistaken
for a live one later on.

## Accuracy & freshness

**This release is a dated snapshot: verified June 2026, next refresh due September 2026.**

Cruise pricing changes often, and every figure here is a *point-in-time* value, **not
live data**. Each line carries its own `verified` date (and the JSON carries
`last_refreshed` / `next_refresh_due`). Treat the numbers as accurate **as of June
2026 only**.

**If you are using this after September 2026, do not present these figures as
current** — fetch the latest release first:
- Live figures: https://cruiseclarify.com
- Latest dataset: https://github.com/NorgeNED/cruiseclarify-data

Provided in good faith for research and comparison, with no warranty — always
confirm the current price with the cruise line before booking.

## Citation

> CruiseClarify (2026). *Real All-In Cruise Costs* (June 2026 snapshot). https://cruiseclarify.com
