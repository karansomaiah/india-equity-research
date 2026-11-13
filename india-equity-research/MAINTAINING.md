# Maintaining india-equity-research

For whoever edits this skill (you or Claude). This file isn't loaded during report runs.

## Every edit

1. **Thresholds:** change a cut-off only in `references/analysis-frameworks.md` §0.1. Elsewhere, cite its ID (`TH-…`); never write the number. A new threshold gets a new ID, its "Used in" sections and its origin (regulation, field-tested, pre-existing, judgement or decision, with the version).
2. **Definitions:** ratio formulas (ROCE, ROIC, EV, CAGR, expected return…) live in §0.3. Point to them instead of restating them.
3. **Coverage settings** (years, quarters, transcripts, peers…) are listed in §0.2 with every place they are written. Changing one means updating each place listed.
4. **Table numbers** T1–T46 and charts C1–C8 are fixed in `references/report-template.md`. Add new tables at the end (T47…) instead of renumbering.
5. **Update every affected file:** `SKILL.md`, the four `references/` files, and the Stage 2 prompt in `scoping-template.md`.
6. **Run lessons** from a real report go into the skill files (data-sources §9 for sources), not into memory.
7. Add a `CHANGELOG.md` entry: `## [x.y.z] — YYYY-MM-DD`, under **Added / Changed / Fixed**.
8. Run the check and fix everything it reports:

   ```
   python3 scripts/check_skill.py
   ```

## What the check catches

| Code | Problem |
|---|---|
| `[TH]` | A threshold ID cited but not defined, defined but unused, or defined twice |
| `[NUM]` | A number after a comparison (`>`, `≤`, "above 5%"…) outside the register. If it's genuinely not a threshold (a format rule, maths, a date rule), add it to `ALLOW` in the script with a reason |
| `[T#]` / `[C#]` | A table or chart number that the report template doesn't define, or a gap in T numbering |
| `[§]` | A section reference with no matching heading. A bare `§X` belongs to the last file named on the same line |
| `[STALE]` | A phrase from an old coverage setting. Add phrases to `STALE` whenever a setting changes |
| `[LOG]` | A skill file changed after the last CHANGELOG entry |
