# India Equity Research Report Template (india-equity-research, Stage 2)

**Order: describe → analyse → argue → value → decide.**

- Number every table. **Table numbers T1–T46 are fixed** (list below each section). Where a table doesn't apply, write one line, e.g. "T34–T35: not applicable (operating company)", so the numbers stay stable. Prose must cite tables ("see T4") rather than quote numbers that appear in no table.
- Thresholds come from analysis-frameworks §0.1 and definitions (ROCE, ROIC, EV, CAGR, expected return…) from §0.3. Never restate a threshold number in the report rules; cite its ID.
- Tag each section **[DATA]** (facts only, no adjectives or opinion) or **[ANALYSIS]** (ends with a Conclusion box, per analysis-frameworks §K).
- Use a table-level source line when one source fills the whole table; otherwise tag each cell or row. Wide annual tables use a `Source` row instead (§3.0).
- Every calculated number cites its working (W#); every assumed number is marked `ASSUMED (A#)`. Both live in §12.
- Number every chart C1…Cn. Each chart plots a numbered table and cites it.
- **Historical coverage is 10 years:** 10 financial years in annual tables and 40 quarters in quarterly tables and charts. Annual tables use the **wide format** in §3.0.
- Output: Markdown only, `<TICKER>/reports/<TICKER>_Equity_Report_<Mon><YYYY>.md`. Charts are Mermaid blocks inside it, not image files.

---

## COVER

```
[COMPANY NAME] (NSE: [TICKER] | BSE: [CODE] | [website])
EQUITY RESEARCH REPORT · [Month Year] · FOR INFORMATIONAL USE ONLY
Company type: [Operating / Holding company / BFSI / Group that consolidates a lender (A6)]
```

```
📊 PRICE SNAPSHOT (as of [DATE], NSE close)
  CMP:         ₹[x]          Prev. Close: ₹[x]
  52W High:    ₹[x]          52W Low:     ₹[x]
  Market Cap:  ₹[x] Cr  (CMP × [N] Cr shares, annual report share-capital note)
  P/E (TTM):   [x]x     (CMP ÷ TTM basic EPS ₹[x] from filings)
  Source:      Tickertape price API, [timestamp]
```

```
VERDICT: [RATING] (Existing) / [RATING] (New investors)
🎯 12M Base ₹[x]–₹[x] | Bull ₹[x] | Bear ₹[x]
📍 Accumulate ₹[x]–₹[x]   🛑 Stop-loss ₹[x] ([basis, e.g. weekly close below computed 200-DMA])
```

---

## 1. SUMMARY [DATA + verdict]

At most 6 bullets and 150 words. No persuasion here; the reasoning comes later.

- What the company is (one line)
- Price vs value: CMP, base value, upside %
- The 2 most important numbers (with table refs)
- Main risk (one line, with a number)
- Next catalyst + date
- Rating

---

## 2. BUSINESS BREAKDOWN [DATA]

### 2.1 What each business does

**T1: Business map**

| Business / Segment | What it does | Legal form (division / subsidiary %) | Revenue FY[T] | EBITDA FY[T] | Margin | YoY rev | Capital employed | % of group revenue |
| ------------------ | ------------ | ------------------------------------ | ------------- | ------------ | ------ | ------- | ---------------- | ------------------ |

### 2.2 Ownership structure (holding companies only)

**T2: Stakes held**

| Holding | Shares held | % | Source (AR page / filing) | CMP | Value (₹ Cr) | Per parent share (₹) |
| ------- | ----------- | - | ------------------------- | --- | ------------- | --------------------- |

Include every quoted and unquoted investment from the annual report investments note.

### 2.3 Segment history

**T3: Segment revenue, EBITDA & capital employed, FY[T-9]–FY[T]** (wide format, §3.0; from the segment notes; derived lines labelled "derived"). If the company resegmented, show the restated basis where a filing gives one, mark the break with a footnote, and list the years with no segment data in T20.

---

## 3. FINANCIAL DATA PACK [DATA]

All figures come from filings (annual report / results). Aggregators fill only the years that filings don't cover, and only with a source tag (see "Source" row below); differences on overlapping years go in T15.

**Coverage: 10 years** (analysis-frameworks §0.2). Annual tables cover the last 10 completed financial years, FY[T-9] … FY[T]. T10 collects the last **43 quarters** (the first 3 only feed TTM), so every quarterly series and chart has **40 points**, ending with the latest reported quarter.

### 3.0 Wide-format rules (mandatory for every annual table: T3, T4–T9 incl. T6b and T8b)

All 10 years must fit in **one** table. Never split a table by years or drop years to save width.

- **Layout: transposed.** One row per line item, one column per year, oldest on the left → newest on the right. After the year columns come `TTM <Mon-YY>` (P&L only) and `CAGR` (flow items only).
- **CAGR column** = FY[T-9] → FY[T], i.e. **9 growth periods** (10 data points). Header it `CAGR FY[T-9]–[T]`. Show "n.m." when the start or end value is ≤ 0.
- **Headers are short:** `FY17`, `FY18` … `FY26`, `TTM Sep-26`. Use no other text in year headers.
- **Units go in the table title** (e.g. "₹ Cr"), never in cells. ₹ Cr values are whole numbers with commas; %, ratios and days take 1 decimal; EPS/DPS take 2 decimals.
- **Right-align numeric columns** (`---:`). Keep line-item labels to ≤ 28 characters, and define abbreviations once under the table.
- **No source column.** The last row of every annual table is `Source`, with one tag per year column (e.g. `AR26`, `AR21`, `TT`, `SCR`, `QR`). Explain any cell-level exception in a footnote.
- **Missing value = "—"** with a footnote, plus a row in T20. Never leave a cell blank or fill it with an estimate.
- **Restated years:** use the restated value and footnote the original.

### 3.0b Ten-year comparability rules (mandatory)

- **Corporate actions.** Restate every per-share series (EPS, DPS, BVPS, share count, P/E inputs) to today's share base for each split, bonus or rights issue in the window. NSE CSV closes are **unadjusted**, while Tickertape prices are adjusted; adjust NSE closes before mixing the two. List each action (date, ratio, factor) in one W#.
- **Accounting breaks.** In every affected table, footnote each change of basis inside the window:
  - **Ind AS adoption:** FY17 for Phase I companies, FY18 for Phase II; earlier years may be Indian GAAP. Prefer the Ind AS comparative column in the next year's annual report.
  - **Ind AS 116 (leases) from FY20:** EBITDA rises and lease liabilities appear, so earlier margins aren't comparable.
  - **New corporate tax regime (s.115BAA, 25.17%) from FY20**, if the company opted in: the effective tax rate breaks.
  - **Ind AS 117 (insurance contracts)** where a subsidiary or JV adopted it.
  - **Mergers, demergers, resegmentation:** use restated comparatives where a filing gives them.
- **Medians and CAGRs across a break.** For margins and tax rates used in the moat test or the DCF, show the 10-year figure and the post-break figure, and say which one is used (A#).

Example layout (T4, abridged):

```
**T4: Consolidated income statement, FY17–FY26 + TTM (₹ Cr)**

| Line item          |  FY17 |  FY18 |  …  |  FY26 | TTM Sep-26 | CAGR FY17–26 |
| ------------------ | ----: | ----: | --: | ----: | ---------: | -----------: |
| Revenue from ops   |       |       |     |       |            |              |
| EBITDA             |       |       |     |       |            |              |
| EBITDA margin %    |       |       |     |       |            |          —   |
| PAT to owners      |       |       |     |       |            |              |
| EPS (basic, ₹)     |       |       |     |       |            |              |
| Source             |  AR21 |  AR21 |  …  |  AR26 |  QR Q2FY27 |          W#  |
```

### 3.1 Annual tables (10 years, wide format)

| Table                                                                    | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **T4** Consolidated income statement, FY[T-9]–FY[T] + TTM         | Revenue from ops, Other income, Total income; Cost of materials / COGS, Employee cost, Other expenses; **EBITDA** (company definition) and margin; Depreciation; EBIT; Finance cost; Exceptional items; Share of JV/associate profit; PBT; Tax and effective tax rate; **PAT total, PAT to NCI, PAT to owners**; EPS (basic); DPS; payout %; YoY revenue and PAT growth                                                                                                                                                                                |
| **T5** Standalone income statement, FY[T-9]–FY[T]                 | Same lines as T4, minus the NCI and JV/associate lines; show dividend income from subsidiaries as its own line                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **T6** Consolidated balance sheet (audited layout), FY[T-9]–FY[T] | Owners' equity, **NCI**, borrowings (separately: excl. financial services / financial services), lease liabilities, policyholder liabilities (if any), other liabilities; fixed assets incl. CWIP, goodwill, investments, loans (financing business), **cash + bank + liquid investments**, other assets; book value per share                                                                                                                                                                                                                         |
| **T6b** Standalone balance sheet (audited layout), FY[T-9]–FY[T] | Equity; borrowings; lease liabilities; other liabilities; fixed assets incl. CWIP; **investments in subsidiaries / JVs / associates** (at cost); other investments (quoted, at fair value); **loans to subsidiaries / group companies**; cash + bank + liquid investments; other assets; book value per share |
| **T7** Net debt, FY[T-9]–FY[T] + latest quarter                   | Gross debt, cash + liquid investments, net debt: consolidated, excl. financial services, standalone                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **T8** Consolidated cash flow statement, FY[T-9]–FY[T]            | **CFO:** PBT, D&A, other non-cash adjustments, working-capital change, taxes paid, **CFO before and after** financing-business loans. **CFI:** capex (incl. CWIP), acquisitions / investments in subsidiaries, net purchase of investments, interest and dividend received, CFI total. **CFF:** net borrowings, interest paid, dividends paid, equity raised / buyback, lease payments, CFF total. Net change in cash; closing cash. **FCF** = CFO (before financing-business loans) − capex; cumulative 10-year CFO, capex and FCF |
| **T8b** Standalone cash flow statement, FY[T-9]–FY[T] | Same layout as T8, minus the financing-business lines. Show separately: **dividends received from subsidiaries / associates**, **investments in and loans to subsidiaries** (infusions and repayments), and the parent's own dividend paid. FCF = CFO − capex; cumulative 10-year totals |
| **T9** Ratios, FY[T-9]–FY[T]                                      | Debtor / inventory / payable days, CCC, ROCE, ROIC, ROE, net debt/EBITDA, interest cover, CFO/PAT, asset turnover. Definitions: analysis-frameworks §0.3                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### 3.2 Quarterly tables & charts (40 quarters)

Quarterly series are **charted** for the full 10 years (C1–C8). Their data tables use a **long format**: one row per quarter, oldest → newest, so they stay narrow.

| Table                                                   | Content                                                                                                                                                                                                       |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **T10** Quarterly results, last 43 quarters       | Quarter (e.g. `Q4FY16`), Revenue, EBITDA, margin, interest, PAT (owners), EPS (basic, adjusted per §3.0b), source tag. Mark the first 3 rows "lead-in (TTM only)"                                                                                                           |
| **T11** TTM P/E history, 40 quarter-ends + latest | Quarter-end price (adjusted; "C"/"W" label per analysis-frameworks §B9), TTM EPS, P/E; plus the 10-year and 5-year median P/E                                                                                     |
| **T13** Rolling TTM financials matrix             | Per analysis-frameworks §B9: one row per quarter-end, 40 rows                                                                                                        |
| **T14** Shareholding, 40 quarters                 | Promoter, pledge %, FII, DII, public, shareholder count; MF % for the latest 8 quarters. The latest 8 quarters come from the shareholding PDFs (full detail); older quarters need only the Promoter / FII / DII / public % (data-sources §3) |

**Charts C1–C8**, placed directly above the table they plot:

| Chart        | Series (one per chart)                            | Type | Plots |
| ------------ | ------------------------------------------------- | ---- | ----- |
| **C1** | Revenue from ops (₹ Cr)                          | bar  | T10   |
| **C2** | EBITDA (₹ Cr)                                    | bar  | T10   |
| **C3** | EBITDA margin (%)                                 | line | T10   |
| **C4** | PAT to owners (₹ Cr)                             | bar  | T10   |
| **C5** | TTM EPS (₹)                                      | line | T13   |
| **C6** | TTM P/E (x); the 10-year median goes in the title | line | T11   |
| **C7** | Promoter holding (%)                              | line | T14   |
| **C8** | FII + DII holding (%)                             | line | T14   |

**Chart rules**

- **Format: Mermaid `xychart-beta`** in a fenced `mermaid` block, so the report stays a single `.md` file. It renders on GitHub, in Obsidian, and in VS Code with a Mermaid extension. Use no image files.
- **One series per chart.** Mermaid xycharts have no legend, so a multi-series chart can't be read; and never use two y-axes. The title names the series, unit, period and source table.
- **Generate charts with a script** from the same arrays that build the table (SKILL Step 7). Never retype values.
- **X-axis:** the last 40 quarters (T10 without its 3 lead-in rows), labelled `Q3FY17` … `Q2FY27`, oldest → newest.
- **Y-axis:** state the range explicitly. Bars start at 0 (or at the series minimum when it's negative). Lines may start near the data's minimum.
- **Missing quarters:** never plot 0 for a missing value. Start the chart at the first available quarter and say so in the title (e.g. "Q1FY20–Q2FY27"); record the gap in T20.
- **Size:** set `width: 1400` and `height: 380` in the block config so 40 labels fit.
- Below each chart, write **one factual line** (e.g. "10-year revenue CAGR x% (W#); peak ₹x Cr in Q#FY##"). No interpretation.

Template:

````
**C1: Quarterly revenue from operations (₹ Cr), Q3FY17–Q2FY27 · plots T10**

```mermaid
---
config:
  xyChart:
    width: 1400
    height: 380
---
xychart-beta
    title "Revenue from operations, ₹ Cr (T10)"
    x-axis ["Q3FY17", "Q4FY17", "…", "Q2FY27"]
    y-axis "₹ Cr" 0 --> [max rounded up]
    bar [v1, v2, …, v40]
```
````

### 3.3 Other tables

| Table                                               | Content                                                                                                                                                               |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **T12** Rolling 12×12 month-end close matrix | Per analysis-frameworks §B9 (a 2-year recent-trend view; its window does not change)                                                                                 |
| **T15** Source reconciliation                 | Key items where filing vs Screener vs Tickertape differ, with the reason. Include every year that came from an aggregator, checked against an overlapping filing year |

Each table and chart gets **one line of factual description** (what changed, by how much). No interpretation here.

---

## 4. INDUSTRY & PEERS [DATA]

### 4.1 Industry size per business

**T16**

| Business | Industry size (₹ Cr) | Growth | Company market share | Source |
| -------- | --------------------- | ------ | -------------------- | ------ |

### 4.2 Holding-company peers (holdcos only; ≥7)

**T17**

| Company | CMP | M-Cap | P/E | P/B | Implied holdco discount (if published) | ROE | Revenue FY[T-2] | FY[T-1] | FY[T] |
| ------- | --- | ----- | --- | --- | -------------------------------------- | --- | --------------- | ------- | ----- |

### 4.3 Peers per business (≥7 each where they exist)

**T18a, T18b…** (one table per business)

| Company | CMP | M-Cap | P/E | EV/EBITDA | P/B | ROE | ROCE | Revenue FY[T-2] | FY[T-1] | FY[T] | 1M % | 6M % | 1Y % | 3Y % | 5Y % | Market share % | Share source |
| ------- | --: | ----: | --: | --------: | --: | --: | ---: | --------------: | ------: | ----: | ---: | ---: | ---: | ---: | ---: | -------------: | ------------ |

If fewer than 7 peers exist, list them all and state "only N listed peers".

**Price-change columns (1M / 6M / 1Y / 3Y / 5Y %).** These are price returns, not total returns.
- Formula: close on the CMP date ÷ close on the last trading day on or before (CMP date − 1, 6, 12, 36, 60 months) − 1.
- 3Y and 5Y are **cumulative %, not annualised**.
- Use the same CMP date for every peer. Add a **Nifty 50** row at the bottom on the same dates as the benchmark.
- Sources (data-sources §1): 1M / 6M / 1Y use the Tickertape daily series (`duration=1y`); 3Y / 5Y use Tickertape `duration=5y` weekly points under the week-selection rule in analysis-frameworks §B9. Label 3Y / 5Y cells "W" unless an NSE CSV close was used.
- A peer listed for less than the period shows "n.a. (listed Mon-YY)".
- Calculate in one scripted pass and show the formula once as a W#.

---

## 5. ANALYSIS [ANALYSIS]

Each subsection is at most 2 short paragraphs plus its table(s), and ends with a **Conclusion box** (analysis-frameworks §K).

| § | Topic | Table(s) | Rules (analysis-frameworks) |
| - | ----- | -------- | --------------------------- |
| 5.1 | Macro & policy | **T21** policy impact | §L |
| 5.2 | Business quality & moat | **T22** moat indicators | §A1, §A1a |
| 5.3 | Growth runway / market size | uses T16 | §F |
| 5.4 | Earnings quality & forensic checks | **T23** financial-health scorecard (10 years), **T24** forensic flags; contingent liabilities, auditor opinion and KAMs from the AR | §A2, §C2 |
| 5.5 | DuPont (consolidated; standalone too for holdcos) | **T25** (10 years) | §A3 |
| 5.6 | ROIC vs WACC (with the computed beta) | **T26** (10 years) | §A4, §A6 |
| 5.7 | Management & governance | **T27** governance checklist, **T28** guidance track record (last 6 calls); tone from the latest 2 calls with transcript page refs; capital allocation over 10 years | §E1–§E5 |
| 5.8 | Institutional flows | uses T14 (incl. MF %); **T29** bulk & block deals | §H |
| 5.9 | Relative strength | **T30** (1M–5Y vs Nifty 50) | §B6 |
| 5.10 | Technicals | **T31** DMA / RSI / MACD / beta, support & resistance, technical summary | §B1–§B8 |

---

## 6. KEY ARGUMENTS [ANALYSIS]

This is where compelling observations, channel checks and "why now" belong. Every argument must cite a table. Ends with a Conclusion box.

**T32: Bull vs bear arguments**

| Bull arguments | Evidence (table ref) | Bear arguments | Evidence (table ref) |
| -------------- | -------------------- | -------------- | -------------------- |

> **Key Insight** callout: the single most important observation, with its numbers.

---

## 7. VALUATION [ANALYSIS]

**7.1 Key assumptions (T33):** the A# entries that drive value most (the full register is in §12.1).

**7.2 Models** (rules in analysis-frameworks §A5; at least TH-VAL-2 methods):

| Table | Model | Applies to |
| ----- | ----- | ---------- |
| **T34** | SOTP | Holdcos |
| **T35** | Implied holdco-discount history, break-even discount | Holdcos |
| **T36** | P/E: target P/E = own 5-year median (T11), 10-year median as the range; peer median (T18) only if history isn't comparable | All |
| **T37** | DCF forecast (FCFF), **mandatory**. Holdcos: standalone businesses only, as a cross-check to SOTP. Lenders / insurers: residual-income forecast instead | All |
| **T38** | DCF EV → equity bridge and checks (residual-income value build for lenders / insurers) | All |
| **T39** | Other models as relevant: EV/EBITDA, P/B, EV/Sales | As relevant |

**T37: DCF forecast (₹ Cr)**, wide format (§3.0): columns FY[T] (actual) · FY[T+1]–FY[T+5] (explicit) · FY[T+6]–FY[T+10] (fade) · Terminal.

| Line item | FY[T] A | FY[T+1] | … | FY[T+5] | FY[T+6] | … | FY[T+10] | Terminal |
| --------- | ------: | ------: | -: | ------: | ------: | -: | -------: | -------: |
| Revenue growth % | | | | | | | | g |
| Revenue | | | | | | | | |
| EBITDA margin % | | | | | | | | |
| EBIT × (1 − t) | | | | | | | | NOPAT |
| + D&A − capex − ΔNWC | | | | | | | | reinvestment = g ÷ RONIC |
| FCFF | | | | | | | | |
| Discount factor | | | | | | | | |
| PV of FCFF | | | | | | | | PV of TV |

The driver rows cite their A#; the 10-year (and post-break, §3.0b) median of each driver from T4, T8 and T9 is shown under the table for comparison.

**T38: EV → equity bridge**: sum of PV(FCFF), PV(TV), EV, then the (EV − market cap) bridge items of analysis-frameworks §0.3, = equity, ÷ shares = ₹/share. Then the checks: TV % of EV (TH-DCF-4); implied terminal EV/EBITDA and P/E vs T11 / T18; explicit CAGR vs the 9-period actual (TH-DCF-5); **reverse-DCF growth implied by the CMP**.

**7.3 Blended target & consensus (T40).** Show the blend and justify the weights (A#). List named, dated broker targets (MarketScreener) and the Trendlyne average, for context only.

**7.4 Sensitivity (T41, T42).** Two 2-variable tables (e.g. holdco discount × key subsidiary price; EPS × P/E). If DCF carries TH-DCF-7 of the blend or more, one of them is WACC × terminal g (TH-DCF-6).

**7.5 Scenarios (T43)**

| Scenario | Value | Probability | Key assumptions (refs to Assumptions Register) |
| -------- | ----- | ----------- | ---------------------------------------------- |

Then the probability-weighted value, the **expected return** and the **accumulate zone** (both defined in analysis-frameworks §0.3), and the margin of safety (§G2).

---

## 8. CATALYSTS, RISKS, SWOT [ANALYSIS]

- **T44: Catalyst calendar** (analysis-frameworks §I; TH-CAT-1): date, event, bull / bear impact, probability.
- **T45: Risk matrix** (§C1 categories), ranked CRITICAL / HIGH / MEDIUM / LOW, evidence = table refs.
- **T46: SWOT**, each point citing a table.

---

## 9. INVESTMENT VERDICT

Ratings follow analysis-frameworks §D: bands from the expected return (§D1), and the split rule for new investors (§D2). If the forensic flags in T24 reach TH-FOR-1, put the ⚠️ FORENSIC ALERT callout here.

**Existing holders: [RATING].** 4–5 bullets with ₹ levels and stop-loss.
**New investors: [RATING].** Entry zone (= accumulate zone), tranches, hard stop, horizon. If the rating is a notch below the existing-holder rating, say which §D2 condition applied.
A 1-paragraph thesis summary.

---

## 10. DISCLAIMER

*This report is for informational and educational purposes only. It synthesises company filings and public market data and does not constitute investment advice or a SEBI-registered research report. Projections and targets are estimates, not guarantees. Consult a SEBI-registered investment adviser before investing.*

---

## 11. DATA SOURCES & DATA GAPS

**T19: Sources**

| Source | Document / URL | Pages / fields used | Date |
| ------ | -------------- | ------------------- | ---- |

**T20: Data gaps & reconciliations**

| Item | Status (missing / conflicting / user-approved gap) | Values seen | Value used | Impact |
| ---- | -------------------------------------------------- | ----------- | ---------- | ------ |

---

## 12. APPENDIX: ASSUMPTIONS REGISTER & WORKINGS

### 12.1 Assumptions Register (A1…An)

Use the format in analysis-frameworks §K. Include every assumed or estimated input: multiples, discounts, growth, margins, EPS estimates, ERP, scenario probabilities, proxies, and any figure taken as-is from management guidance.

### 12.2 Workings (W1…Wn)

Use the format in analysis-frameworks §K, grouped as follows:

- **Data pack:** market cap, share count, corporate-action adjustment factors (§3.0b), TTM EPS, net debt, CFO before financing loans, derived segment figures
- **Ratios:** margins, CAGRs, financial-health scorecard, DuPont, working-capital days, CFO/PAT, accruals, moat indicators, guidance score
- **ROIC / WACC:** NOPAT, invested capital, Ke (beta), Kd, weights, economic profit
- **Technicals:** DMA, RSI, MACD, beta, returns (state the data points and dates used)
- **Valuation:** each model line by line, the DCF checks and reverse DCF, the blend, break-even discount, sensitivity grid formulas
- **Scenarios:** inputs per scenario, probability-weighted value, expected return, accumulate zone
