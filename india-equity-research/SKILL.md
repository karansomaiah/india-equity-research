---
name: india-equity-research
description: Filings-first, two-stage equity research for NSE/BSE-listed Indian companies. Stage 1 (scoping) produces a research brief plus a ready-to-run Stage 2 prompt; Stage 2 produces the full Markdown report with numbered data tables, an Assumptions Register and a Workings Appendix. Load ONLY when the user explicitly names this skill ("india-equity-research"), or runs a Stage 1/Stage 2 prompt that names it. Do not auto-trigger on generic stock-analysis requests.
---

# India Equity Research (two-stage, filings-first)

This skill produces research reports for NSE/BSE stocks in **two stages**:

| Stage | Trigger | Output |
|---|---|---|
| **1 · Scoping** | "Scope <company>", "prepare research brief for <company>", or any report request where no brief exists yet | `<TICKER>/reports/<TICKER>_research_brief.md`, containing the scoping facts, a documents checklist and a **filled-in Stage 2 prompt** |
| **2 · Research & report** | The Stage 2 prompt from the brief (or "run stage 2 for <TICKER>") | `<TICKER>/reports/<TICKER>_Equity_Report_<Mon><YYYY>.md` |

**Core principles**
1. **Filings are the source of truth.** Use the annual report, results filings and transcripts in `<TICKER>/inputs/` or on BSE/NSE first. Use aggregators only for speed and cross-checks.
2. **Complete the data before writing.** If a required number is missing, stop and ask the user, naming the exact document and line item. Never estimate it silently or leave it out.
3. **Be explicit, never implicit.** Every calculation and every assumed number appears in the **Workings Appendix** (W1…Wn) and the **Assumptions Register** (A1…An). The body of the report cites them, e.g. "₹3,308 (W5, A2)".
4. **Separate data from opinion.** Sections are tagged [DATA] or [ANALYSIS].
5. **Describe first, argue last.** Business and financials come first; arguments, valuation and verdict come at the end.
6. **Conclude with numbers.** Every [ANALYSIS] section ends with a numeric Conclusion box.

**Output is Markdown only.** Do not create .docx, .pdf or other formats unless the user explicitly asks.

**Folder layout** (relative to the project root / working directory):
```
<TICKER>/
  inputs/            ← filings the user downloads (annual reports, results, transcripts, presentations,
                       subsidiary reports). Ignore urls*.txt, .zip, .rar, audio.
    _extracted/      ← skill-written data extracts with page references
  reports/           ← research brief, reports, prompts
```
If the user's files are elsewhere (e.g. `inputs/<TICKER>/`), say so and ask before moving anything.

Read before starting either stage:
- `references/data-sources.md`: source tiers, verified endpoints, pitfalls
- `references/analysis-frameworks.md`: **§0 register** (every threshold, coverage setting and standard definition), then computation rules, valuation, technicals, matrices, workings format
- `references/scoping-template.md`: Stage 1 brief and the Stage 2 prompt template
- `references/report-template.md`: Stage 2 section order and tables

---

## STAGE 1 · SCOPING (light: ~10–20 tool calls, no deep analysis)

Goal: collect the company-specific facts that the Stage 2 prompt needs, and tell the user what to download.

1. **Identify the company.**
   - Resolve the NSE ticker, BSE code and Tickertape SID (slug suffix, e.g. `grasim-industries-GRAS` → `GRAS`), plus the company IR URL.
   - If the name is ambiguous, ask the user before going further.
2. **Get the latest price.** Fetch the latest close from the Tickertape price API (data-sources §1) and record the date.
3. **Test quarterly depth.** Call Tickertape `financials/income/<SID>/interim/normal?count=43`.
   - **Pass:** 43 quarters come back and PAT and EPS for the latest 4 quarters match the results filings. (Revenue won't match: Tickertape includes other income.)
   - **Fail:** add the older results filings needed for the 43-quarter T10 to the documents checklist (row 2). Each filing gives the current and year-ago quarter.
   - Record the result in the brief.
4. **Classify the company:**
   - Operating company
   - Holding company / conglomerate (owns listed subsidiaries or material listed investments): SOTP applies
   - BFSI
   - Group that consolidates a lender or insurer: analysis-frameworks A6 applies
5. **Map the structure:**
   - Reportable segments (from the latest results filing segment note).
   - Listed subsidiaries and listed investments: name, ticker, approximate stake.
   - Material unlisted subsidiaries.
   - In Stage 1 these are **provisional** and come from the latest results filing, presentation or shareholding filings. Stage 2 verifies them against the annual report.
6. **Inventory `<TICKER>/inputs/`.**
   - List every document, its period, type, page count, and whether its text can be extracted (`pypdf`).
   - Flag scanned PDFs.
7. **Build the documents checklist.** Mark each required document as present or missing, and give a download URL for each missing one:
   - Latest annual report
   - Last 4 quarterly results filings (plus older ones if the step 3 test failed)
   - Last 6 earnings-call transcripts (guidance track record; tone uses the latest 2)
   - Latest investor presentation
   - Annual reports of listed subsidiaries
   - Subsidiary financials (only if material)
   - **Always-fetch items** (data-sources §11). These can't be fetched automatically (§10), so list them with exact URLs and filenames:
     - NSE daily-close CSVs for the last 2 years (company + each listed subsidiary) and a Nifty 50 CSV;
     - 8 quarterly shareholding-pattern PDFs;
     - NSE bulk & block deals for the last 6 months (CSV);
     - the 10Y G-Sec benchmark (FBIL);
     - each listed subsidiary's latest-quarter results;
     - exchange intimations for every pending or recent corporate action named in the results notes;
     - an industry-size source per business;
     - overseas peer financials if fewer than 7 Indian peers exist.
8. **Propose a peer universe** to be confirmed in Stage 2:
   - Holding-company peers, if a holdco.
   - For each business or segment: an industry label and ≥7 candidate listed peers. If fewer exist, list them all.
9. **Record known issues.** If a prior report exists in `<TICKER>/reports/`, list the issues already found in it (wrong stakes, stale data, gaps), so Stage 2 does not repeat them.
10. **Write the brief.**
   - Write `<TICKER>/reports/<TICKER>_research_brief.md` following `references/scoping-template.md`. Its last section is the **filled-in Stage 2 prompt**.
11. **Report back to the user in chat:**
   - A ≤10-line summary.
   - The list of missing documents.
   - The Stage 2 prompt, in a code block.
   - Ask the user to add the missing documents and then run the prompt.

Stage 1 must **not** value the company or give a rating.

---

## STAGE 2 · RESEARCH & REPORT

Prerequisite: `<TICKER>/reports/<TICKER>_research_brief.md` must exist. If it doesn't, run Stage 1 first.

### Step 1: Load the brief, refresh the price
Load the brief. Fetch CMP from the Tickertape price API, falling back to Google Finance card → 5Paisa. **Never** use Screener's displayed price or Yahoo Finance for CMP. If the latest close is older than TH-DQ-8 (analysis-frameworks §0.1), flag it.

### Step 2: Extract from filings
- Extract text from `<TICKER>/inputs/` with `pypdf`.
  - Scanned subsidiary volumes: use the parent annual report's Form AOC-1 instead.
  - Otherwise, OCR only the needed pages with `ocrmypdf`.
- Write `<TICKER>/inputs/_extracted/<TICKER>_<FY>_extract.md` with page references, e.g. `[Source: <doc> PDF p.N]`.
  - **Cite viewer page numbers** (pypdf index + 1, labelled "PDF p.N") in the brief, extract and report alike; mixing 0-based and 1-based numbering caused errors in the GRASIM run.
  - For scanned or OCR'd results pages, use `extract_text(extraction_mode="layout")` on that page.
- Parse share counts and other Indian-grouped numbers programmatically (strip commas) and cross-check value = shares × price against the company's reported fair value (data-sources §2, PDF notes).

### Step 3: Fetch the remaining data by tier
Follow `references/data-sources.md`, using the Tier 1 source wherever one exists.

| Data | Tier 1 | Tier 2 / cross-check |
|---|---|---|
| P&L, BS, CF (consolidated + standalone) | Annual report / results filings | Tickertape financials API, Screener |
| Quarterly P&L, EPS | Results filings | Tickertape (as reported), Screener (restated) |
| Segments | Segment note, investor presentation | — |
| Holdings (shares held) | Annual report investments note + later allotments | Subsidiary's BSE shareholding pattern |
| Share count | Annual report share-capital note | Tickertape `balTcso` |
| Prices, index | Tickertape `stocks/info` (close) + 1Y daily chart; older dates from user's NSE / niftyindices CSVs | Tickertape weekly (label "W") |
| Technicals, beta, returns | **Computed in-house** | — |
| Shareholding | Shareholding-pattern PDFs (user-supplied, latest 8 quarters); older quarters for the 40-quarter T14 from the BSE shareholding pages | Tickertape `stocks/holdings` (pledge), Screener |
| Commentary, guidance | Transcripts (last 6) | Summaries (mark as secondary) |
| Bulk & block deals | User-supplied NSE CSV (window TH-FLOW-1) | BSE bulk-deals page (untested), dated news (analysis-frameworks §H1) |
| Analyst actions | MarketScreener (dated, named) | Trendlyne (average) |
| Peers | Tickertape API, peer filings | Screener peers |
| Industry size / market share | Annual report MD&A, industry bodies, IBEF | Approved news |
| Macro, policy | RBI / DBIE, MOSPI, FBIL; official policy documents (Gazette, PIB, Budget, CBIC, DGTR, regulators) | TradingEconomics; approved news to explain a policy only (analysis-frameworks §L) |
| News | NSE/BSE announcements | ET, Moneycontrol, Mint, CNBC-TV18, NDTV Profit |

### Step 4: Completeness gate (mandatory; do not write until it passes)

| # | Required item | Where to find it |
|---|---|---|
| 1 | Consolidated P&L and cash flow, 10 years, incl. PAT to owners vs NCI | Latest annual report + the FY[T-5] annual report (5-year highlights + audited statements); fill remaining years from Tickertape/Screener with source tags (data-sources §2) |
| 2 | Standalone P&L, balance sheet and cash flow, 10 years | Same two annual reports → Standalone Financial Highlights + standalone audited statements; remaining years from Screener standalone (data-sources §2) |
| 3 | Consolidated balance sheet, 10 years (audited layout, incl. NCI, leases, policyholder liabilities) | Annual report / Q4 results → Statement of Assets & Liabilities |
| 4 | Cash + bank + liquid current investments | Same statement → current assets |
| 5 | Gross/net debt: consolidated, excl. financial services, standalone, latest quarter | Annual report Financial Highlights; latest concall |
| 6 | Segment revenue / EBITDA / capital employed, 10 years (or all years available, with the gap in T20) | Segment notes / presentations |
| 7 | Shares outstanding (incl. treasury / partly paid) | Annual report → share-capital note |
| 8 | Shares held in each listed subsidiary / investment (+ later changes) | Annual report → investments note; BSE shareholding |
| 9 | Beta (computed), 10Y G-Sec | Price API; FBIL |
| 10 | Contingent liabilities (standalone + consolidated) | Annual report notes |
| 11 | Auditors, tenure / rotation, opinion, KAMs | Board's report, auditor's report |
| 12 | Board composition, audit committee meetings | Corporate governance report |
| 13 | Promoter holding & pledge | BSE shareholding pattern |
| 14 | Material RPTs; MD remuneration ratio | Board's report, RPT note |
| 15 | Guidance from the last 6 transcripts, scored against actuals (analysis-frameworks §E4) | Transcripts; Screener Documents links + curl |
| 16 | Peers ≥7 per business (+ holdco peers), with market share & 3-year revenue | Step 6 |
| 17 | Quarterly results, 43 quarters (T10) | Results filings; Tickertape if the Stage 1 test passed (data-sources §2) |
| 18 | Shareholding, 40 quarters (latest 8 from PDFs) | Shareholding PDFs; BSE shareholding page (data-sources §3) |
| 19 | Corporate actions in the 10-year window (splits, bonuses, rights) | Exchange announcements, AR share-capital note (report-template §3.0b) |

**Gate rules:**
- **Two attempts, then ask.** After two failed attempts at an item (different sources or searches), **stop and ask the user**, naming the document and line item (e.g. "FY26 Annual Report → Consolidated Balance Sheet → Cash and cash equivalents").
- **Anomaly rule.** If a value breaks a sanity range (analysis-frameworks §J), re-fetch it from a second source. Report both values and say which one is used and why. **Never** exclude a value silently.
- **Restatements.** Use the restated value and footnote the original.
- **User-approved gaps.** If the user says to proceed without an item, record it in the Data Gaps table with its estimated impact.
- **Blocked sources.** BSE/NSE APIs and some data sites block automated fetches (data-sources §10).
  - Don't burn attempts on them. Send the user **one prioritised link list** (item, exact URL, suggested filename; Priority 1 = affects valuation or a template table) and wait.
  - Ingest the files the user adds (CSV, PDF, XLSX, HEIC screenshots). Re-run the affected calculations, then record whatever is still missing in Data Gaps.

### Step 5: Computations
All computations go in the **Workings Appendix**, in the format of analysis-frameworks §K:
- Corporate-action adjustment of per-share series and NSE-CSV prices; accounting-break footnotes (report-template §3.0b).
- P/E (TTM) = CMP ÷ TTM basic EPS from filings, plus a P/E history at the last 40 quarter-ends and the latest date, with 10-year and 5-year medians.
- Market cap = CMP × annual-report share count.
- Stake values = shares held × CMP.
- 20/50/200-DMA, RSI(14), MACD(12,26,9), beta (TH-COC-2), returns 1M–5Y vs Nifty 50 (analysis-frameworks §B6, §B8).
- Rolling 12×12 month-end close matrix; rolling TTM financials matrix (40 quarter-ends; T10's 3 lead-in quarters complete the first windows).
- 10-year CAGRs (9 growth periods, FY[T-9] → FY[T]) for the CAGR column of the annual tables.
- Ratios and the financial-health scorecard, DuPont, ROIC/WACC (10 years each), moat indicators, guidance score, net debt.
- Every valuation model: DCF with its checks and reverse DCF (or residual income for lenders / insurers), P/E, SOTP and break-even discount for holdcos, the blend, sensitivities, scenarios, expected return and accumulate zone.
- Use the definitions in analysis-frameworks §0.3 for every ratio, for the company and its peers.

### Step 6: Peers
- **Holdcos:** ≥7 Indian holdco peers.
- **Each business:** ≥7 listed peers where they exist; if fewer exist, list them all and say "only N".
- **For every peer:** CMP, market cap, P/E, P/B, EV/EBITDA, ROE, ROCE, 3 years of revenue, 1M / 6M / 1Y / 3Y / 5Y price change (report-template §4.3), market share (with source).
- **Valuation link:** every multiple used in valuation must be anchored in these tables or in the company's own history (Assumptions Register).
- **Mechanics:**
  - Resolve SIDs first; the Tickertape search index misses newer listings (data-sources §1).
  - Pull `stocks/info` + annual income + balance sheet + price charts (`duration=1y` daily, `duration=5y` weekly) for every peer and the Nifty 50 in one scripted pass.
  - Apply the median-exclusion and market-share rules in analysis-frameworks "Peer statistics".

### Step 7: Write the report
Write it in Markdown, following `references/report-template.md`.
- Use the fixed table numbers T1–T46 in report-template; write a "not applicable" line for tables that don't apply.
- Generate data-heavy tables (P/E history, 12×12 matrix, TTM matrix, shareholding, peer tables, scorecard, DuPont, ROIC/WACC, DCF, discount history, sensitivity grids) **from the computation outputs with a script**. Then fill them into a hand-written template. Don't retype numbers.
- Annual tables (T3–T9, incl. standalone T5, T6b, T8b) use the **wide format** in report-template §3.0: one row per line item, 10 year columns oldest → newest, a `Source` row. Never split a table by years.
- Generate the quarterly charts C1–C8 (Mermaid `xychart-beta`, 40 quarters, one series each) with the same script, from the same arrays as T10/T11/T13/T14.

### Step 8: Quality check (mandatory)
- [ ] CMP is a real ₹ number with a date, from Tickertape / Google Finance / 5Paisa. No formulas.
- [ ] Completeness gate passed, or each gap is user-approved and listed in Data Gaps.
- [ ] Every number has a source tag (per table where one source fills the table, otherwise per cell or row).
- [ ] Every figure quoted in prose appears in a numbered table (T#) or a working (W#).
- [ ] **Every calculated figure has a working W#.** Every assumed or estimated number is labelled `ASSUMED` with an A# entry: value, anchor, source, range tested.
- [ ] Stakes = shares × price; market cap = CMP × annual-report shares.
- [ ] Section order follows the template. [DATA] sections contain no opinion words. Every [ANALYSIS] section ends with a Conclusion box.
- [ ] Summary ≤6 bullets and ≤150 words.
- [ ] Annual tables cover 10 years in one wide table each, with a `Source` row; quarterly tables cover 40 quarters; charts C1–C8 are present, cite their table, and their values match it (scripted check).
- [ ] Per-share series and NSE prices are adjusted for corporate actions; accounting breaks are footnoted (report-template §3.0b).
- [ ] Ratios use the analysis-frameworks §0.3 definitions; every threshold applied matches §0.1.
- [ ] Present: P/E history, 12×12 matrix, peer tables, T21–T31 analysis tables, DCF (T37–T38, with reverse DCF and checks) or residual-income model for lenders / insurers, scenario table, split verdict, disclaimer, Sources, Data Gaps, Assumptions Register, Workings Appendix.
- [ ] Only a `.md` file was written, at `<TICKER>/reports/`. A ≤150-word summary is pasted in chat.
- [ ] **Scripted cross-reference check:**
  - every T#, W# and A# cited in the text is defined, and W# numbers are not reused across sections;
  - summary bullet and word count;
  - opinion-word scan of [DATA] sections;
  - every [ANALYSIS] section (including Key Arguments) ends with a Conclusion box.
- [ ] **Re-derive the headline figures** quoted in prose (sensitivities, relative returns, % moves) from the computation outputs. In the GRASIM run, several prose numbers drifted from the tables before this check.

**Self-score (deliver only at 5/5):**

| Code | Dimension | Pass criteria |
|---|---|---|
| D1 | Sourcing | Filings first; gate passed |
| D2 | Structure | Template order; numbered tables; Conclusion boxes; ≥7 peers |
| D3 | Explicitness | 100% sourced; every calculation in W#; every assumption in A# |
| D4 | Actionability | ₹ entry/exit/tranche/stop levels for both investor types |
| D5 | Output | `.md` in `<TICKER>/reports/`; chat summary |

---

## Hallucination prevention

1. No made-up figures. Every number comes from a filing or a fetched page, or is computed in a W# working.
2. No silent assumptions. Anything not taken directly from a source is either a W# calculation or an A# assumption.
3. No invented consensus. Use only named, dated broker calls, or the Trendlyne aggregate.
4. Ask instead of guessing (completeness gate).
5. No target price without a model whose inputs are in A# and whose arithmetic is in W#.
6. No Screener or Yahoo prices for CMP. No third-party technical snippets; compute technicals in-house.

## Tone & style

- Be clear and concise rather than polished: short sentences, no filler.
- Compelling observations go in **Key Arguments**, after the business and financials have been described.
- [DATA] sections contain numbers and changes only.
- The verdict gives separate guidance for existing holders and new investors, with ₹ levels.
