# Changelog: india-equity-research

A new skill, separate from `india-equity-report` (which stays unchanged at v1.1.0), so it can be improved incrementally.

## [0.4.0] — 2026-11-13
Full review: one register for thresholds, error fixes, the rest of the 10-year migration, wiring, and a consistency checker.

### Added
- **analysis-frameworks §0 register.**
  - **§0.1** holds 57 thresholds with IDs (`TH-…`), each with its value, where it is used and its origin. Sections cite the IDs only.
  - **§0.2** lists the coverage settings and every place they are written.
  - **§0.3** has standard definitions: revenue, EBITDA, EBIT, CE, ROCE, IC, ROIC, ROE, net debt, EV, FCF, CAGR, price change, expected return, accumulate zone.
- **report-template §3.0b, ten-year comparability rules:**
  - restate per-share series for splits, bonuses and rights, and adjust NSE CSV closes (they are unadjusted, unlike Tickertape);
  - footnote accounting breaks: Ind AS adoption FY17/FY18, Ind AS 116 from FY20, s.115BAA tax from FY20, Ind AS 117, mergers and demergers;
  - show post-break medians for DCF and moat inputs.
- **Fixed table numbers T21–T46** for every analysis, valuation, catalyst and risk table. They were unnumbered before.
  - **§5:** T21 policy, T22 moat, T23 scorecard, T24 forensic, T25 DuPont, T26 ROIC/WACC, T27 governance, T28 guidance, T29 bulk deals, T30 relative strength, T31 technicals.
  - **§6:** T32 arguments.
  - **§7:** T33 assumptions, T34–T35 SOTP and discount, T36 P/E, T37–T38 DCF, T39 other models, T40 blend, T41–T42 sensitivity, T43 scenarios.
  - **§8:** T44 catalysts, T45 risks, T46 SWOT.
  - Tables that don't apply get a "not applicable" line.
- **Split-verdict rule (§D2):** new investors get one notch lower (BUY→ADD, ADD→HOLD) when the CMP is above the accumulate-zone top or the technical summary is bearish.
- **Rating bands** now use the defined expected return. "Fundamentals weakening" means a Negative Conclusion in report §5.2, §5.4 or §5.6.
- **Stage 1 step 3:** test Tickertape quarterly depth (`count=43`; PAT and EPS vs filings). New brief row; completeness-gate items 17–19 (43 quarters, 40-quarter shareholding, corporate actions).
- **MACD** formula in §B8.
- `scripts/check_skill.py` (consistency checker) and `MAINTAINING.md` (edit checklist).

### Fixed
- **ROCE vs WACC:** the moat test and DCF terminal RONIC compared pre-tax ROCE with post-tax WACC. Both now use ROIC.
- **Definitions:** ROCE had three definitions and EV two; both now follow §0.3. Peers whose Tickertape cash includes insurance investments are n.m. for EV.
- **§G1 DCF grid** (revenue CAGR × fixed WACC) contradicted the WACC × g rule; now points to it. **§G2** rewritten around reverse DCF.
- **Governance:**
  - S.R. Batliboi was listed as "mid-tier"; it is EY's Indian member firm. Audit-firm networks are now named.
  - Auditor tenure is now a check against Companies Act s.139(2) rotation.
  - The independent-director minimum is now LODR Reg 17(1)(b): ⅓ or ½ depending on the chair.
  - Promoter pay now uses LODR Reg 17(6)(e) (₹5 Cr / 2.5% / 5%), replacing "5% of PAT in a small company".
- **Uncomputable technicals:** ADX and Stochastic need highs and lows, which Tickertape doesn't provide; delivery % and F&O had no source. All four removed.
- **Sources:** the 10Y G-Sec is now FBIL everywhere (was "RBI" in three places); forensic checks come from T4/T8/T9/T14 and the AR, not Screener.
- **Off-by-three quarters:** 40 quarters gave only 37 TTM points. T10 now collects 43 quarters, so T11, T13, C5 and C6 have 40.
- **Moat test:** pricing power compared 10-year margins against peers that had no 10-year margin data. It now uses peer annual income (`count=10`) and compares on one EBITDA basis. Narrow now also covers "excess returns only".

### Changed
- **10 years throughout:** the §A2 scorecard (3/5/9-period CAGRs, flags per year, T23), §A3 DuPont (T25), §A4 ROIC/WACC (T26), §E3 capital allocation (T8 cumulative cash flows).
- **Target P/E:** 5-year median primary, 10-year median as the range; peer median only if history isn't comparable.
- **Relative strength:** one period set, 1M/3M/6M/1Y/3Y/5Y vs Nifty 50. Nifty 500 and sector indices dropped (no verified source).
- **Holdings and catalysts:** fund-level MF trend (Trendlyne, behind a login) replaced by aggregate MF % in T14. Catalyst horizon is now 12 months, matching the target.
- **Generic examples:** the risk and catalyst lists drop leftovers from earlier companies (Amazon/Flipkart B2B, defence trials). LinkedIn is labelled secondary.
- **Pointers:** report-template §5 is now a table with each subsection's tables and framework sections. §8 and §9 point to §C1, §I and §D. The Stage 2 prompt, scoping §5 (DCF mandatory) and the cover company types (4) are updated.

## [0.3.4] — 2026-11-13
### Added
- **DCF (FCFF) is now a mandatory valuation model** (analysis-frameworks A5 DCF; report-template §7.2, new tables T21 forecast and T22 EV → equity bridge):
  - **Who runs which model:** operating companies use a consolidated DCF; holdcos value only their standalone businesses (a cross-check to SOTP); groups with a lender exclude FS; lenders / insurers use the residual-income model instead.
  - **Stages:** 5 explicit years plus 5 fade years, anchored to the 10-year history, then terminal value from the value-driver formula, with RONIC tied to the §A1a moat rating.
  - **Guidance weight** follows the §E4 credibility rating.
  - **Mandatory checks:** TV share > 75% flag, implied terminal multiples, explicit CAGR vs 10-year CAGR, reverse DCF.
  - **Sensitivity:** a WACC × g grid is required in §7.4 when DCF carries ≥25% of the blend.
- **SKILL.md** quality check: DCF / residual income must be present.

### Fixed
- **P/B Gordon formula** was `g / (RoE − g)`; corrected to `(ROE − g) / (Ke − g)`. A residual-income model was added for BFSI.

### Changed
- The old DCF stub (3 explicit years + 3–4 fade years) was replaced by the 5 + 5 structure above.

## [0.3.3] — 2026-11-13
Section 5 source gaps closed.

### Changed
- **Guidance track record (analysis-frameworks §E4):**
  - now uses the **last 6 transcripts**, up from 2: checklist row 3, Stage 1 step 6 and completeness-gate item 15;
  - adds a scoring table (verbatim quote, page, actual from T#, Met / Missed / Pending) and thresholds: High ≥75%, Medium 50–74%, Low <50%; fewer than 4 scored items = "insufficient record";
  - tone analysis still uses the latest 2 calls.
- **Bulk / block deals (analysis-frameworks §H1):**
  - one 6-month window; §B3 used to say 90 days;
  - source order: user NSE CSV (new checklist row 15 and data-sources §10 row), then the untested BSE page (try once), then a dated news search;
  - the hard-coded "2025" search phrase is gone;
  - "none found in <sources>" wording, plus a T20 row when only news was searched.

### Added
- **analysis-frameworks §A1a, moat evidence rules (report §5.2):** each moat type needs an indicator from a numbered table, with thresholds. The Wide / Narrow / None rating rule requires ROCE > WACC in ≥7 of 10 years. Management claims must be cited and checked against T16/T18, or labelled "unverified".
- **analysis-frameworks §L, macro & policy impact (report §5.1):**
  - scope: only segments that are ≥5% of revenue or EBITDA;
  - policy-impact table layout;
  - macro values from RBI / MOSPI / FBIL only, and every policy needs an official document (Gazette, PIB, Budget, CBIC, DGTR, regulator circular) — new data-sources §8 row;
  - news can't support a quantified impact, and impact is quantified only through W# arithmetic.
- **report-template §5.1, §5.2, §5.7, §5.8** point to these rules.

## [0.3.2] — 2026-11-13
### Added
- **report-template §4.3 (T18 peers per business):** 1M / 6M / 1Y / 3Y / 5Y % price-change columns.
  - These are price returns, all on the same CMP date; 3Y and 5Y are cumulative, not annualised.
  - A Nifty 50 benchmark row goes at the bottom.
  - Prices come from Tickertape daily data (up to 1 year) and `5y` weekly points ("W").
  - Peers listed for less than the period show "n.a.".
- **SKILL.md Step 6:** the peer list and the scripted pass include price charts for every peer and the Nifty.

## [0.3.1] — 2026-11-13
### Added
- **report-template §3.1:** T6b standalone balance sheet and T8b standalone cash flow statement, 10 years, wide format. They show the holdco items separately: investments in and loans to subsidiaries, dividends received, and capital put into subsidiaries. T5 adds dividend income from subsidiaries as its own line. Suffix numbering keeps T7–T20 unchanged.
- **SKILL.md** completeness-gate item 2 now requires standalone P&L, balance sheet and cash flow for 10 years.
- **data-sources §2:** standalone fallback = Screener standalone page (`SCR-S`). Tickertape `normal` financials are consolidated only.

## [0.3.0] — 2026-11-09
10-year history, wide tables and quarterly charts.

### Changed
- **report-template §3 (Financial Data Pack):**
  - Annual tables T3–T9 now cover **10 financial years**, FY[T-9]–FY[T]. Before, T3 had 3 years, T4/T5/T8/T9 had 5 and T6 had 3–5; T7 adds a 10-year net-debt history.
  - T4 is now a full consolidated income statement and T8 a full consolidated cash flow statement (CFO / CFI / CFF detail, FCF, cumulative 10-year totals).
  - Quarterly tables now cover **40 quarters**: T10 results, T11 P/E history, T13 TTM matrix, T14 shareholding. Before, they had 8–12 quarters.
- **report-template:** new §3.0 wide-format rules:
  - transposed layout, with years as columns oldest → newest;
  - TTM and 9-period CAGR columns;
  - a `Source` row instead of a source column;
  - fixed number formats.
- **report-template:** new quarterly charts C1–C8 for 10 years, as single-series Mermaid `xychart-beta` blocks, generated by script from the table arrays.
- **SKILL.md:** completeness-gate items 1, 2, 3 and 6 now require 10 years. Steps 5, 7 and 8 cover the 40-quarter P/E history, wide tables and charts, including a scripted check that chart values match their tables.
- **scoping-template:** documents checklist adds the FY[T-5] annual report (row 1a); the Stage 2 prompt asks for 10-year tables and charts.
- **data-sources §2 and §3:** how to source 10 years (two ARs, then tagged Tickertape/Screener years) and older shareholding quarters (BSE page).
- **analysis-frameworks:** P/E history is now 40 quarter-ends with 10-year and 5-year medians; TTM matrix has up to 37 rows; older quarter-end prices use Tickertape `max` weekly ("W").

### Unchanged
- The 12×12 month-end close matrix and the peer tables T17/T18 (3-year revenue).

## [0.2.1] — 2026-10-07
Lessons from the BAJAJFINSV Stage 1 run (`BAJAJFINSV/reports/BAJAJFINSV_research_brief.md`).

### Changed
- **data-sources §9:**
  - nsearchives PDFs and BSE filing PDFs (`AnnPdfOpen.aspx`, `xml-data/corpfiling`) **do download** with curl + a browser user-agent + the exchange referer. Only the BSE/NSE APIs are blocked.
  - Screener's "Documents" section is the quickest index of filing URLs.
  - NSE iXBRL integrated filings give segment and P&L data in ₹ lakh.
  - Tickertape search `marketCap` is wrong, so use `stocks/info` only.
  - JS-built IR sites return no links via curl.
  - Some investor decks are in USD.
- **data-sources §10:** the corporate-announcements row now says to try Screener links + curl before asking the user.

## [0.2.0] — 2026-10-07
Lessons from the first full GRASIM Stage 1 → Stage 2 run (`GRASIM/reports/GRASIM_Equity_Report_Oct2026.md`).

### Added
- **data-sources §10 Blocked sources:** BSE API (Access Denied), NSE API (503), nsearchives PDFs (timeout), plus the exact manual-download link for each and a protocol of one prioritised link list to the user.
- **data-sources §11 Always-fetch list:**
  - 2-year NSE daily CSVs (company + listed subsidiaries) and a Nifty CSV;
  - 8 quarterly shareholding PDFs;
  - FBIL 10Y G-Sec;
  - subsidiaries' latest-quarter results;
  - exchange intimations for corporate actions;
  - industry-size sources;
  - overseas peer financials.
  The same items were added as rows 7–14 of the Stage 1 documents checklist.
- **Tickertape:**
  - `stocks/info` `lastPrice` = official close (`quotes.price` = last trade, ❌ for CMP);
  - daily = 1 year only, and weekly points are Monday-dated;
  - the search index is stale for newer listings, so a SID-lookup method and a table of verified SIDs were added;
  - financials and holdings field map.
- **Source fixes:** MarketScreener `/news-broker-research/` page; Trendlyne `/consensus-estimates/` URL pattern; FBIL / RBI WSS for the 10Y G-Sec.
- **Industry and peer sources:** RBI FSR NBFC sizing method; AMAI caustic; DPIIT core index (index only); Lenzing AR; stockanalysis.com for overseas peers.
- **Shareholding:** source rules and the GDR explanation for the FII % gap (Screener excludes GDRs, Tickertape includes them).
- **PDF and number handling:**
  - cite viewer page numbers;
  - use layout-mode extraction for OCR'd results;
  - read xlsx without openpyxl; read HEIC via `sips`;
  - parse Indian digit grouping programmatically (a retyped share count was 10× off).
- **analysis-frameworks — valuation:**
  - recipe for the implied-discount history (holdco discount = 8-quarter median, min/max = bull/bear);
  - net-debt roll-forward for post-quarter dividends;
  - valuing an unlisted subsidiary from a recent deal, with the promoter-pricing "monitor" rule.
- **analysis-frameworks — calculation rules:**
  - restated-EPS TTM rule;
  - subsidiary EBITDA from its results statement (PBT before exceptional + finance + D&A), with an other-income caveat for derived residuals;
  - ROIC for lender groups excludes FS borrowings;
  - weekly-price rule (Monday + 4 days ≤ date);
  - peer-statistics rules: EV/ROCE formulas, n.m. exclusions, same-business-model EV/Sales comps, peer-set revenue share labelling.
- **SKILL.md:**
  - script-generated tables;
  - scripted cross-reference QC check;
  - re-derive the headline prose numbers before delivery.

## [0.1.0] — 2026-10-06
Based on the v2.0 draft (`GRASIM/reports/skill-v2.0-proposed.diff`) and user feedback from 6-Oct-2026.

### Added
- **Two stages.** Stage 1 (scoping) writes `<TICKER>/reports/<TICKER>_research_brief.md` with identifiers, a provisional structure, an inputs inventory, a documents checklist, a peer universe and a **filled-in Stage 2 prompt**. Stage 2 (research & report) consumes the brief. Template: `references/scoping-template.md`.
- **Workings Appendix (W#)** for every calculation, and an **Assumptions Register (A#)** with anchor, range tested and where each assumption is used. The body cites W#/A#, and assumed numbers are labelled `ASSUMED (A#)`.
- Everything from the v2.0 draft: filings-first sourcing, completeness gate, in-house technicals and beta, P/E standard and history, 12×12 month-end matrix, rolling TTM matrix, SOTP rules, lender-consolidation adjustments, sanity ranges, ≥7 peers per business, [DATA]/[ANALYSIS] tags, Conclusion boxes, describe-first order.

### Changed
- **Markdown only.** No .docx output.
- Folder layout is now `<TICKER>/inputs/` and `<TICKER>/reports/`, with extracts in `<TICKER>/inputs/_extracted/`.
