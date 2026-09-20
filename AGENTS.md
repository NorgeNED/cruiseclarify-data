# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is
This is a **data-only** repository (the `CruiseClarify — Real All-In Cruise Costs`
open dataset), not an application. There is **no** backend/frontend, no build
system, and **no lint/test/build framework**. "Development" here means editing and
validating the dataset files:

- `cruise-costs.json` — full-fidelity source of truth (nested; keeps every tier,
  range, and provenance note). Treat this as the SSOT.
- `cruise-costs.csv`, `cruise-packages.csv`, `cruise-gratuities-tiers.csv` — flat,
  derived views. CSVs are **UTF-8 with a BOM**, so read them with encoding
  `utf-8-sig` (not plain `utf-8`) or the first key/header will be corrupted.

### Validating changes (there is no test runner)
Validate ad hoc with Python 3.12 (`json` + `csv` from stdlib). Useful invariants:
- `cruise-costs.json` must parse, and its `line_count` field must equal the number
  of entries in `lines`.
- Every `key` in `cruise-costs.csv` should exist in the JSON `lines` object.
- Blank CSV cells mean "not applicable", never "unknown"; `0` means "included / no
  extra cost". Do not confuse the two when editing.

### The only "service": Hugging Face sync (optional, maintainer-only)
`.github/workflows/sync-huggingface.yml` mirrors the data files to the
`CruiseClarify/cruise-costs` Hugging Face dataset on pushes to `main`. It requires
an `HF_TOKEN` repo secret (HF **write** token) and exits with an error if it is
unset. This is a publishing step — do **not** run an actual `hf upload` from a
cloud agent (it would push to the live public dataset). The CLI used is
`huggingface_hub[cli]` (installed by the update script).

### Environment gotcha
The `hf` / `huggingface-cli` executables install to `~/.local/bin`, which is not on
`PATH` by default. Prefix with `export PATH="$HOME/.local/bin:$PATH"` before using
them.
