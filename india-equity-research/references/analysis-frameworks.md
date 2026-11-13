# Analysis Frameworks for India Equity Research

---

## 0. REGISTER: THRESHOLDS, COVERAGE & DEFINITIONS

**Every numeric cut-off lives in §0.1 and nowhere else.** Sections cite the ID (e.g. TH-MOAT-1) instead of repeating the number. To tune a threshold, change it here only, then run `scripts/check_skill.py` (see `MAINTAINING.md`).

### 0.1 Thresholds register

| ID | Rule | Value | Used in | Origin |
|---|---|---|---|---|
| TH-MOAT-1 | Excess returns: share of years with ROIC > WACC | ≥ 70% of years (7 of 10) | §A1a, §A5 DCF | Judgement (v0.3.3) |
| TH-MOAT-2 | Pricing power: share of compared years with EBITDA margin ≥ peer median | ≥ 70% | §A1a | Judgement (v0.3.3) |
| TH-MOAT-3 | Pricing power: 10-year EBITDA-margin range (max − min) | ≤ 10 pp | §A1a | Judgement (v0.3.3) |
| TH-MOAT-4 | Scale: market-share rank | ≤ 3 (top 3) | §A1a | Judgement (v0.3.3) |
| TH-MOAT-5 | Scale: EBITDA margin above peer median | ≥ 3 pp | §A1a | Judgement (v0.3.3) |
| TH-MOAT-6 | Wide moat: other moat types supported, besides excess returns | ≥ 2 | §A1a | Judgement (v0.3.3) |
| TH-GUID-1 | Guidance credibility High | ≥ 75% of scored items met | §E4 | Judgement (v0.3.3) |
| TH-GUID-2 | Guidance credibility Medium (below = Low) | ≥ 50% met | §E4 | Judgement (v0.3.3) |
| TH-GUID-3 | Minimum scored guidance items for a rating | 4 | §E4 | Judgement (v0.3.3) |
| TH-MACRO-1 | Segment materiality for the policy-impact table | ≥ 5% of group revenue or EBITDA | §L | Judgement (v0.3.3) |
| TH-MACRO-2 | Policy look-back | 12 months (plus pending ones with a stated date) | §L | Judgement (v0.3.3) |
| TH-DCF-1 | Terminal growth g: domestic consumption | 5–6% | §A5 DCF | Pre-existing |
| TH-DCF-2 | Terminal growth g: cyclicals / commodities | 4–5% | §A5 DCF | Pre-existing |
| TH-DCF-3 | Terminal growth cap | ≤ 10Y G-Sec yield | §A5 DCF | Judgement (v0.3.4) |
| TH-DCF-4 | Flag: terminal value as % of EV | > 75% | §A5 DCF | Judgement (v0.3.4) |
| TH-DCF-5 | Justify: explicit-period revenue CAGR vs the 9-period actual | > 1.5× | §A5 DCF | Judgement (v0.3.4) |
| TH-DCF-6 | Sensitivity grid steps (WACC × g) | ±100 bp in 50 bp steps (5 × 5) | §A5 DCF, §G1 | Judgement (v0.3.4) |
| TH-DCF-7 | DCF blend weight that makes the WACC × g grid mandatory | ≥ 25% | §A5 DCF, report §7.4 | Judgement (v0.3.4) |
| TH-COC-1 | Equity risk premium | 5.5–6.5%, default 6% | §A4, §A5 DCF | Pre-existing |
| TH-COC-2 | Beta window | 1 year of daily simple returns vs Nifty 50 | §A4, §B8 | Pre-existing |
| TH-FH-1 | Flag: 9-period revenue CAGR, company valued as a growth stock | < 8% | §A2 | Pre-existing (was 3-year) |
| TH-FH-2 | Flag: consecutive quarters of EBITDA-margin decline | 3 | §A2 | Pre-existing |
| TH-FH-3 | Flag: ROE | < 15% | §A2 | Pre-existing |
| TH-FH-4 | Flag: ROCE | < 15% | §A2 | Pre-existing |
| TH-FH-5 | Flag: debt / equity (non-BFSI) | > 1.5x | §A2 | Pre-existing |
| TH-FH-6 | Flag: interest cover | < 3x | §A2 | Pre-existing |
| TH-FH-7 | Flag: CFO / PAT | < 0.8 | §A2 | Pre-existing |
| TH-FH-8 | Flag: accruals ratio | > 5% | §A2 | Pre-existing |
| TH-FOR-1 | Forensic-alert callout: number of forensic flags raised | ≥ 3 | §C2, report §9 | Pre-existing |
| TH-PEER-1 | Exclude from peer medians: P/E | < 0 or > 150x | §A5 Peer statistics | Field-tested (GRASIM) |
| TH-PEER-2 | Exclude from peer medians: EV/EBITDA | > 50x | §A5 Peer statistics | Field-tested (GRASIM) |
| TH-PEER-3 | Exclude from peer medians: ROE anomaly | > 100% | §A5 Peer statistics | Field-tested (GRASIM) |
| TH-PEER-4 | Exclude from peer medians: revenue YoY anomaly | < −70% | §A5 Peer statistics | Field-tested (GRASIM) |
| TH-VAL-1 | Use EV/Sales: PAT negative or PAT margin below | 3% | §A5 EV/Sales | Pre-existing |
| TH-VAL-2 | Minimum valuation methods | 2 (3 for high-conviction reports) | §A5 | Pre-existing |
| TH-VAL-3 | Implied holdco-discount history: quarter-ends | 8 | §A5 SOTP | Field-tested (GRASIM) |
| TH-RATE-1 | BUY: expected 12-month return above | 15% | §D1, §0.3 accumulate zone | Pre-existing |
| TH-RATE-2 | ADD lower bound (ADD = TH-RATE-2 to TH-RATE-1) | 8% | §D1 | Pre-existing |
| TH-RATE-3 | HOLD lower bound (HOLD = TH-RATE-3 to TH-RATE-2) | 0% | §D1 | Pre-existing |
| TH-RATE-4 | REDUCE lower bound (below = SELL) | −5% | §D1 | Pre-existing |
| TH-RATE-5 | New-investor notch-down (split verdict) | 1 notch | §D2 | Decision (v0.4.0) |
| TH-GOV-1 | Independent directors, minimum | ⅓ if the chair is non-executive and not promoter-related; ½ otherwise | §E2 | Regulation: SEBI LODR Reg 17(1)(b) |
| TH-GOV-2 | Audit committee meetings | ≥ 4 a year, ≤ 120 days apart | §E2 | Regulation: SEBI LODR Reg 18(2)(a) |
| TH-GOV-3 | Auditor rotation (listed company) | Individual: one 5-year term; firm: two 5-year terms, then 5-year cooling-off | §E2 | Regulation: Companies Act s.139(2) |
| TH-GOV-4 | Executive promoter-director pay needing a special resolution | > ₹5 Cr or 2.5% of net profit (higher of the two) per person; > 5% of net profit in aggregate | §E2 | Regulation: SEBI LODR Reg 17(6)(e) |
| TH-TECH-1 | RSI(14) overbought | > 70 | §B2 | Pre-existing |
| TH-TECH-2 | RSI(14) oversold | < 30 | §B2 | Pre-existing |
| TH-FLOW-1 | Bulk / block-deal window | 6 months to the CMP date | §H1, §B3 | Decision (v0.3.3) |
| TH-CAT-1 | Catalyst horizon and count | Next 12 months; 3–5 catalysts | §I, §D3 | Decision (v0.4.0) |
| TH-DQ-1 | Re-fetch: P/B | > 50x for any company; > 10x for a lender | §J | Field-tested (GRASIM) |
| TH-DQ-2 | Re-fetch: P/E without a stated reason | < 0 or > 150x | §J | Field-tested (GRASIM) |
| TH-DQ-3 | Re-fetch: ownership % vs shares held ÷ shares outstanding | > 0.5 pp apart | §J | Field-tested (GRASIM) |
| TH-DQ-4 | Re-fetch: market cap vs CMP × shares outstanding | > 2% apart | §J | Field-tested (GRASIM) |
| TH-DQ-5 | Re-fetch: quarterly revenue vs filing revenue from operations | > 1% apart | §J | Field-tested (GRASIM) |
| TH-DQ-6 | Re-fetch: technical level vs in-house computation | > 2% apart | §J | Field-tested (GRASIM) |
| TH-DQ-7 | Re-fetch: any figure, two sources | > 5% apart | §J | Pre-existing |
| TH-DQ-8 | Flag: latest close older than | 3 trading days | SKILL Stage 2 Step 1 | Pre-existing |

### 0.2 Coverage settings

These shape table layouts, so they are written out where they are used. Changing one is a multi-file edit; `scripts/check_skill.py` lists stale phrases afterwards.

| Setting | Value | Written into |
|---|---|---|
| Annual history | 10 financial years, FY[T-9]–FY[T] | report-template §3 (T3–T9, T6b, T8b), T23, T25, T26; SKILL gate items 1–3, 6; data-sources §2; scoping row 1a |
| Quarterly results collected | 43 quarters (the first 3 only feed TTM) | T10; SKILL Stage 1 step 3 and gate item 17; data-sources §2; scoping row 2 |
| Quarterly series shown | 40 points | T11, T13, T14, C1–C8 |
| Shareholding PDFs | Latest 8 quarters (older quarters: BSE summary %) | T14; data-sources §3, §10, §11; scoping row 9 |
| Transcripts | 6 (tone uses the latest 2) | §E4, §E5; SKILL Stage 1 and gate item 15; scoping row 3 |
| NSE daily-price CSV | 2 years | T12; data-sources §10, §11; scoping row 7 |
| Peers | ≥ 7 per business, and ≥ 7 holdco peers | SKILL Step 6; report-template §4; scoping §6 |
| Peer revenue history | 3 years | T17, T18; SKILL gate item 16 |
| Peer price changes | 1M / 6M / 1Y / 3Y / 5Y, plus a Nifty 50 row | T18; SKILL Step 6 |
| Company relative strength | 1M / 3M / 6M / 1Y / 3Y / 5Y vs Nifty 50 | §B6, §B8, T30 |
| 12×12 price matrix | 24 month-ends | T12, §B9 |
| DCF forecast | 5 explicit + 5 fade years + terminal | §A5 DCF, T37 |
| Report summary | ≤ 6 bullets, ≤ 150 words | report-template §1; SKILL Step 8 |

### 0.3 Standard definitions

Use these for the company, its peers and every model. If a source uses a different definition, footnote it.

| Term | Definition |
|---|---|
| Revenue | Revenue from operations, excluding other income. |
| EBITDA | Company-reported definition (state whether it includes other income). Peers on Tickertape: `incEbi`, which **includes** other income; compare on the same basis or footnote it. |
| EBIT | EBITDA − depreciation & amortisation (before exceptional items). |
| Capital employed (CE) | Owners' equity + NCI + gross borrowings + lease liabilities; average of opening and closing. |
| ROCE | EBIT ÷ average CE. **Pre-tax**; never compare it with WACC. Peers on Tickertape: `incPbi` ÷ (`balTeq` + `balTdeb`), year-end not average; footnote it. |
| Invested capital (IC) | CE − cash, bank and liquid investments. A6 groups: exclude financial-services borrowings (§A6). |
| ROIC | NOPAT ÷ average IC, where NOPAT = EBIT × (1 − effective tax rate). **Post-tax: the only return compared with WACC.** |
| ROE | PAT to owners ÷ average owners' equity. |
| Net debt | Gross borrowings − cash, bank and liquid investments. Lease liabilities are shown separately. A6 groups also show it excluding financial services. |
| EV | Market cap + gross borrowings + lease liabilities + NCI (listed subsidiaries at market × NCI %, else book) − cash, bank and liquid investments − non-operating investments (listed at market, unlisted at AR fair value). **Peers (Tickertape approximation):** market cap + `balTdeb` − `balCsti`; mark n.m. where `balCsti` includes insurance or policyholder investments. |
| FCF | CFO (before financing-business loans) − capex (incl. CWIP). |
| CAGR | (end ÷ start)^(1/n) − 1, where n = years between the end points (10 annual data points → n = 9). "n.m." if the start or end value is ≤ 0. |
| Price change | Close on the CMP date ÷ close on the last trading day on or before (CMP date − period) − 1, on corporate-action-adjusted prices (report-template §3.0b). Cumulative, not annualised. |
| Expected return (12M) | (probability-weighted value from report §7.5 + DPS expected over the next 12 months, A#) ÷ CMP − 1. Drives the rating bands (§D1). |
| Accumulate zone | Top = (probability-weighted value + expected 12M DPS) ÷ (1 + TH-RATE-1). Bottom = the nearest computed support below the top (T31). |

---

## A. FUNDAMENTAL ANALYSIS

### A1. Business Quality Assessment (report §5.2)
Evaluate using the 5-factor quality lens; moat claims must pass §A1a:
- **Business model**: Revenue streams, pricing power, entry barriers (moat type: cost/switching/network/intangible)
- **Competitive position**: Market share trend, industry structure (fragmented vs consolidated), barriers to replication
- **Management quality**: See Section E (Management Deep-Dive) — this deserves its own section in the report
- **Capital allocation**: ROE vs ROCE trend, reinvestment rate, dividend history, buybacks, acquisition track record
- **ESG / Governance flags**: SEBI enforcement actions, audit qualifications, related-party transactions

### A1a. Moat evidence rules (report §5.2, T22)
A moat claim is allowed only when a **measurable indicator from a numbered table** backs it. Management claims ("market leader", "strong brand") are quoted as management claims with the transcript or AR page, then checked against T16/T18. If they can't be checked, label them "unverified".

| Moat type | Required indicator (source) | Supports a moat when |
|---|---|---|
| Excess returns (always assess) | ROIC vs WACC, 10 years (T26; today's WACC is the hurdle for every year, A#) | ROIC > WACC in TH-MOAT-1 of the years |
| Pricing power | EBITDA margin, 10 years (T4, C3) vs the peer median for each year with peer data (Tickertape annual income, `count=10`; W#) | Margin ≥ peer median in TH-MOAT-2 of the compared years, **and** the 10-year range is within TH-MOAT-3 |
| Scale / cost | Market-share rank (T16/T18, with source); margin or cost per unit vs peers (T18, AR) | Rank within TH-MOAT-4, or margin above the peer median by TH-MOAT-5 |
| Market-share durability | Share in the earliest vs latest available year (T16 / AR / industry body) | Share flat or rising |
| Switching cost / network / intangible / licence | Only with a filing citation: AR page, transcript page, regulator licence list, patent or brand data | The citation exists and states a fact, not an adjective |

- Assess each business segment separately where T1 shows more than one.
- Compare margins on one basis: company EBITDA and peer `incEbi` differ by other income (§0.3), and margins break at accounting changes (report-template §3.0b).
- **Rating** for the Conclusion box: **Wide** = excess returns plus TH-MOAT-6 other moat types supported; **Narrow** = excess returns supported, with fewer other types; **None** = excess returns not supported. List which indicators passed.
- Sources: data already in T1, T3, T4, T16, T18 and T26, plus peer income data, AR MD&A and transcripts. Don't use any new web source for 5.2, except a regulator's licence list.

### A2. Financial Health Scorecard (report §5.4, T23)
Compute **for each of the 10 years** (wide format) from T4, T6, T8, T9 and T10. Definitions are in §0.3.

| Metric | Formula | Flag if |
|---|---|---|
| Revenue growth | CAGR over 3, 5 and 9 periods (T4) | 9-period CAGR below TH-FH-1, for a company valued as a growth stock |
| EBITDA margin trend | EBITDA ÷ revenue, quarterly (T10) | Declines for TH-FH-2 consecutive quarters |
| PAT margin | PAT ÷ revenue | Below the peer median |
| ROE | §0.3 | Below TH-FH-3 |
| ROCE | §0.3 | Below TH-FH-4 |
| ROIC | §0.3 | Below WACC (T26) |
| Debt / equity | Gross borrowings ÷ owners' equity | Above TH-FH-5 (non-BFSI) |
| Interest cover | EBIT ÷ finance cost | Below TH-FH-6 |
| CFO / PAT | CFO (before financing-business loans) ÷ PAT | Below TH-FH-7 |
| Accruals ratio | (PAT − CFO − CFI) ÷ average net operating assets | Above TH-FH-8 |
| Working-capital days | Debtor + inventory − payable days (T9) | Rising YoY |

- Show the flag count per year, so the 10-year pattern is visible, not just the latest year.
- For holdcos and A6 groups, CFI includes investment purchases and financing-business flows, so the accruals ratio is n.m.; say so.

### A3. DuPont Decomposition (ROE Attribution) (report §5.5, T25)
**Always run a 3-factor DuPont for all 10 years** (wide format). It tells you *why* ROE is high or low, and whether that is sustainable.

```
ROE = Net profit margin × Asset turnover × Equity multiplier
    = (PAT to owners / Revenue) × (Revenue / Average total assets) × (Average total assets / Average owners' equity)
```

| Component | FY[T-9] | … | FY[T] | Median (10Y) |
|---|---:|---:|---:|---:|
| Net profit margin (%) | | | | |
| Asset turnover (x) | | | | |
| Equity multiplier (x) | | | | |
| **ROE (%)** | | | | |

- Consolidated for every company; also standalone for holdcos (standalone PAT ÷ standalone net worth, from T5 and T6b).
- Reading it: ROE rising from margins = quality; from leverage = risk if debt keeps rising; from asset turnover = efficiency, but watch for limits.

### A4. Capital Allocation Quality (ROIC vs WACC) (report §5.6, T26)
The ROIC − WACC spread is the primary value-creation measure. Definitions of ROIC and invested capital are in §0.3.

- Every input comes from the audited balance sheet (SKILL Stage 2 completeness gate, items 3–5). **Never** leave out cash because it was "not fetched"; that triggers the completeness gate.
- NOPAT includes 100% of subsidiaries' profit, so NCI **must** be in invested capital. Leaving it out overstates ROIC (Grasim FY26: 6.3% wrong vs 5.6% correct).
- For groups that consolidate a lender or insurer, also show ROIC **excluding financial services** (§A6).
- **WACC** = Ke × E/V + Kd × (1 − t) × D/V, at market-value weights on the valuation date.
  - Ke = 10Y G-Sec yield (FBIL, data-sources §8) + beta × ERP. ERP per TH-COC-1.
  - Beta: **computed in-house** per TH-COC-2 (§B8). Never assume a value.
  - Kd = finance cost ÷ average gross borrowings (T4, T6).
- One WACC (today's) is the hurdle for all 10 years; record it as an A#.

| Metric | FY[T-9] | … | FY[T] | Median (10Y) |
|---|---:|---:|---:|---:|
| ROIC (%) | | | | |
| WACC (%) | | | | |
| Spread (ROIC − WACC, pp) | | | | |
| Economic profit (₹ Cr) = NOPAT − WACC × average IC | | | | |

ROIC above WACC means reinvestment creates value and can justify a premium; below WACC, growth destroys value and a discount is warranted.

### A5. Valuation (report §7)
**Methods:** at least TH-VAL-2. DCF (or residual income for lenders / insurers) is mandatory; SOTP is mandatory for holdcos.

#### P/E standard (applies to every P/E in the report)
- **P/E (TTM)** = CMP ÷ sum of the last 4 quarters' **basic EPS attributable to owners**, from results filings (use restated values where a later filing restated them).
- Always show a **TTM P/E history table**: the last 40 quarter-ends plus the latest date, with columns Price | TTM EPS | P/E, and the 10-year and 5-year median P/E. The price is the close on (or the last trading day before) each quarter-end. Note that EPS becomes known about 6 weeks after the quarter-end.
- **Use the latest restated value of each quarter.** It is usually the comparative column in the same quarter's filing one year later (e.g. Q2 FY25 EPS 5.86 as first reported → 4.73 in the Q2 FY26 filing).
- If a restatement is disclosed only for the full year and some quarters (GRASIM: Ind AS 117 adoption by a JV), use the restated annual EPS for the year-end TTM. Roll forward as annual − restated year-ago quarter + new quarter (73.28 − 20.93 + 31.64 = 83.99). Footnote that quarterly sums in the TTM matrix differ by the undisclosed amount.
- Website P/Es (Tickertape uses last-FY EPS; Screener uses TTM with its cached price) go in a footnote only.
- Forward P/E uses FY(T+1) and FY(T+2) estimates. Name the source: own model, or a dated broker estimate.

#### P/E Re-rating (T36)
- TTM EPS per the P/E standard; forward EPS from the own model (inputs in the Assumptions Register) or dated broker estimates.
- Target price = forward EPS × target P/E.
- **Target P/E:** the own **5-year median** TTM P/E (T11) is the primary anchor. Show the **10-year median** next to it; the bull and bear P/E span the two medians. Use the peer median (T18) instead only when the company's history isn't comparable (e.g. a demerger or a business-mix change), and say why (A#).

#### EV/EBITDA (T39)
- EV per §0.3.
- Target price = (target EV/EBITDA × forward EBITDA − (EV − market cap)) ÷ shares outstanding, where (EV − market cap) is the bridge of debt, leases, NCI, cash and investments from §0.3, at the latest balance-sheet date.
- The multiple comes from the peer table (median, inter-quartile range) or the company's own history. Record it in the Assumptions Register.

#### Peer statistics (field-tested)
- **Peer EV, EV/EBITDA and ROCE** use the Tickertape approximations in §0.3 (EV/EBITDA on last-FY `incEbi`). Show the formulas once as a W#.
- **Exclude from medians, and say so:**
  - P/E per TH-PEER-1;
  - EV/EBITDA per TH-PEER-2 (depressed EBITDA);
  - EV/EBITDA and ROCE for lenders (use P/B, P/E, ROE);
  - anomalies: ROE per TH-PEER-3, revenue YoY per TH-PEER-4 (GRASIM run: JSW Dulux ex-Akzo, Shankara, Chemplast).
  - Don't drop them from the table; mark them n.m.
- **EV/Sales** for loss-making new businesses: pick comparables with the **same business model**. B2B trading platforms (revenue = GMV) compare to distributors (Redington ~0.3x), not to marketplaces (IndiaMART ~3.7x).
- **Market share:** use industry share only where an approved source gives industry size; for paints, flag company revenue ÷ industry as an upper bound. Otherwise compute "peer-set revenue share" (company revenue ÷ table total), label it plainly, and never call it market share.
- **Overseas peers** (when Indian peers are fewer than 7): include their multiples (local currency is fine for ratios) and 3-year revenue; mark them Tier 2.

#### DCF (FCFF): mandatory for operating companies and for holdcos' own businesses (T37, T38)
**Where it applies**
- **Operating company:** DCF of the consolidated business.
- **Holding company:** DCF of the **standalone operating businesses only**, as a cross-check to SOTP step 3. Listed stakes stay at market value; a group-level DCF would count them twice.
- **Lenders / insurers:** no FCFF DCF, because debt is raw material. Use the residual-income model in "P/B (for BFSI stocks)" in T37–T38 instead, and say so in report §7.
- **Groups that consolidate a lender (A6):** run the DCF excluding financial services, and add the FS stake at market value in the equity bridge.

**Structure** (coverage: §0.2)

| Stage | Years | Drivers |
|---|---|---|
| 1 · Explicit | FY[T+1]–FY[T+5] | Revenue growth, EBITDA margin, capex / revenue, NWC / revenue, tax rate. Each is an A#, anchored to the 10-year history (T4, T8, T9: median and range), industry growth (T16) and guidance (§E4). Use post-break figures where report-template §3.0b applies |
| 2 · Fade | FY[T+6]–FY[T+10] | Growth fades linearly to terminal g; margin fades to the 10-year median unless §A1a rates the moat Wide |
| 3 · Terminal | FY[T+11] onward | Value-driver formula, below |

- **Guidance weight:** use management guidance as-is only when §E4 rates credibility High. At Medium, take the midpoint of guidance and the 10-year median. At Low or "insufficient record", ignore guidance.
- **FCFF** = EBIT × (1 − t) + D&A − capex − ΔNWC. Use post-Ind AS 116 EBITDA and treat lease liabilities as debt in the bridge.
- **Discount rate:** WACC from §A4 (the same W# as report §5.6). Discount from the valuation date (CMP date), year-end convention; state the fractional first period in the W#.
- **Terminal value** = NOPAT(T+11) × (1 − g ÷ RONIC) ÷ (WACC − g)
  - g (A#): TH-DCF-1 for domestic consumption, TH-DCF-2 for cyclicals / commodities, never above TH-DCF-3.
  - RONIC (return on new invested capital, A#): equal to WACC if §A1a rates the moat **None**; at most the 10-year median ROIC (T26) if **Narrow** or **Wide**.
- **Equity bridge (T38):** EV (sum of discounted FCFF + discounted TV) − (EV − market cap) bridge items from §0.3 at the latest balance-sheet date (T6/T7) = equity value; ÷ AR share count = value per share.

**Mandatory checks** (show each in the W# and in T38):
- TV as % of EV; flag it per TH-DCF-4 and explain in the Conclusion box.
- Implied terminal-year EV/EBITDA and P/E vs the 10-year P/E median (T11) and peer medians (T18).
- Explicit-period revenue CAGR vs the 9-period actual CAGR (T4); justify per TH-DCF-5 with an A# anchored to guidance or T16.
- **Reverse DCF:** solve for the Stage 1 revenue CAGR (other drivers unchanged) that makes value = CMP, and compare it with the 9-period actual CAGR (§G2).
- **Sensitivity:** WACC × terminal g grid per TH-DCF-6. It is one of the two report §7.4 tables whenever DCF carries TH-DCF-7 of the blend.

#### P/B (for BFSI stocks) (T37–T39)
- Target price = target P/B × latest book value per share.
- Target P/B (Gordon) = (ROE − g) ÷ (Ke − g). ROE = sustainable ROE (A#, anchored to the 10-year ROE in T9); g = sustainable growth = ROE × (1 − payout); Ke from §A4.
- **Residual-income model** (replaces DCF for lenders / insurers, in T37–T38): value = BVPS₀ + Σ (ROEₜ − Ke) × BVPSₜ₋₁ ÷ (1 + Ke)ᵗ over 10 years + terminal (ROE − Ke) × BVPS₁₀ ÷ ((Ke − g) × (1 + Ke)¹⁰). Use the same stage structure and guidance-weight rules as the DCF.

#### EV/Sales (for high-growth, low-profit companies) (T39)
- Use when PAT is negative or the PAT margin is below TH-VAL-1. Compare against the 3- and 9-period revenue CAGRs (T23).
- Benchmark against listed peers; flag a premium to peers that higher growth doesn't justify.

#### SOTP (mandatory for holding companies / conglomerates) (T34, T35)
1. **Listed stakes**: value = shares held (annual report investments note + any later allotment) × CMP of that company on the same date. **Include every quoted investment**, not just subsidiaries (e.g. Grasim → UltraTech, ABCap, Hindalco, Vodafone Idea, ABFRL, ABLBL).
2. **Unquoted investments**: fair value from the annual report (FVTOCI note) or a peer multiple. State which.
3. **Own businesses (segments)**: EV/EBITDA or EV/Sales from the ≥7-peer table for that business, applied to segment EBITDA or revenue from the segment note. If a segment is loss-making, use EV/Sales from peers or invested capital (cumulative capex from the annual report). Label the choice.
4. **Less: standalone net debt** (annual report "Net Debt" or results; update with the latest concall figure and say which date).
5. **Holdco discount**: apply to listed stakes (and optionally to unquoted investments) only. It must be anchored to (a) the company's own **implied discount history** (compute it at each of the last TH-VAL-3 quarter-ends using the break-even formula; T35) and/or (b) dated broker SOTP discounts. State the range and the chosen value in the Assumptions Register.
6. **Per share** = SOTP equity ÷ shares outstanding from the annual report share-capital note (not a website market cap ÷ price).
7. **Break-even (implied) discount** d* solves: Market Cap = (1 − d*) × Listed stakes + Standalone EV − Net debt. Report d* under ≥2 standalone-value assumptions (base, and loss-making segments at zero) to show how sensitive it is.
8. **Implied-discount history: field-tested recipe (GRASIM Oct-26)**
   - **Listed value at each quarter-end:** main subsidiaries = shares held × exact quarter-end close (NSE CSV or Tickertape daily). Other quoted investments come from the company's quarterly investor presentation (standalone "Vodafone Idea", "Other Investments" lines). Don't rebuild them from adjusted price series, because demergers and splits distort those.
   - **Standalone net debt** at each quarter-end: presentation line "Net Debt / (Surplus)".
   - **Standalone operating value:** hold today's peer multiples constant and apply them to the last reported FY segment EBITDA (TTM for the latest quarter). Keep other standalone items constant. Record all of this as one A# entry.
   - **Holdco discount used in SOTP** = median of the quarter-end d* values; min and max = bull and bear. Compare it with today's d*. If today's is narrower than the median, the stock is rich against its own history.
   - **Two variants:** (A) new or loss-making businesses at invested capital; (B) at zero. Report both medians.
9. **Net debt date roll-forward:** start from the latest reported standalone net debt. Subtract dividends received from subsidiaries whose record date has passed (shares held × DPS) and add the parent's own dividend paid. Ignore other unreported cash flows and label the result ASSUMED.
10. **Unlisted subsidiary with a recent equity deal:**
    - Value it from the **transaction**: price per share × shares held, or the disclosed deal EV less net debt if the net debt is known.
    - If a promoter-group entity subscribed at a much lower price than a third-party investor (or the third party's price is undisclosed), flag it under governance as "monitor"; don't call it a red flag without both prices.
    - Large pending acquisitions (EV, capacity, turnover, closing date) belong in catalysts and risks, not in the base SOTP.

**Blended target (T40):** weight the methods by relevance and justify the weights (A#). If DCF carries TH-DCF-7 of the blend or more, the WACC × g grid is mandatory.
**Upside / downside:** always show the % move from CMP to target, and the expected return per §0.3.

### A6. Conglomerates that consolidate a lender or insurer
- **EBITDA**: use company-reported EBITDA. Aggregator "operating profit" sits before the NBFC's interest cost and overstates EBITDA.
- **Debt**: report gross and net debt **excluding financial-services borrowings** (shown in the annual report Financial Highlights) alongside consolidated debt.
- **Cash flow**: consolidated CFO includes "Loans of financing business". Show CFO before and after this line, and treat negative CFO as structural, not an earnings-quality flag.
- **ROE / DuPont**: show it for the consolidated entity and for the parent's own businesses (standalone PAT ÷ standalone net worth).
- **Derived segment economics**: when a loss-making business is not disclosed separately, derive it as (segment EBITDA − listed subsidiary's reported EBITDA). Label it "derived" and show the working (e.g. Grasim Building Materials 16,364 − UltraTech consolidated 17,598 = −1,234 Cr paints + B2B, FY26).
  - Check the subsidiary's EBITDA definition. UltraTech's includes other income (₹577.51 Cr FY26), so the derived loss may be overstated by up to that amount; state the bound in Data Gaps.
  - For TTM, take the subsidiary's quarterly EBITDA from its own results statement (PBT before exceptional + finance + D&A), not from a "+x% YoY" phrase in the parent's presentation.
  - For revenue-only businesses inside a segment, use run-rate = latest quarter × 4 (A#) when annual revenue is not disclosed.
- **ROIC for lender groups**: invested capital = owners' equity + NCI + debt **excluding FS borrowings** + leases − cash/bank/liquid investments. Exclude FS borrowings because the FS segment's EBITDA is already after its interest cost; including them understates ROIC (Grasim FY26: 3.4% vs 6.5%). Also show ROIC excluding FS on segment capital employed (segment assets − segment liabilities).
- **Cash flow**: show CFO before "Loans of financing business" **and** before "Investment of life-insurance policyholders"; report CFO-before-loans ÷ EBITDA as the cash-conversion check.

---

## B. TECHNICAL ANALYSIS

### B1. Trend Analysis
- **Primary trend**: Above/below 200-DMA? (Bullish/Bearish structural)
- **Intermediate trend**: Above/below 50-DMA?
- **Short-term**: Price vs 20-DMA
- **Golden/Death Cross**: 50-DMA crossing above/below 200-DMA — flag if recently occurred

### B2. Momentum Indicators
- **RSI (14)**: above TH-TECH-1 = overbought (caution for fresh entry; check divergence); below TH-TECH-2 = oversold (possible reversal; look for bullish divergence); in between = neutral.
  - **Divergence:** price makes a new high but RSI makes a lower high = bearish divergence (significant warning).
- **MACD (12, 26, 9)**: bullish crossover (MACD above signal) vs bearish; histogram expanding or contracting. Formula in §B8.
- **Not used:** ADX and Stochastic need daily highs and lows, and the Tickertape price API returns closes and volume only.

### B3. Volume
- Volume trend from the Tickertape `v` field: rising volume on up-days vs down-days (rising on up-days = accumulation).
- **Bulk / block deals:** see §H1 (window TH-FLOW-1).
- **Not used:** delivery % and F&O data (open interest, put/call ratio, max pain). There is no verified source; add them only after a source is field-tested.

### B4. Support & Resistance (T31)
- Identify key levels: 52-week high, 52-week low, prior swing highs/lows, round numbers
- Fibonacci retracement levels from the most recent major swing: 23.6%, 38.2%, 50%, 61.8%
- State: "Strong support at ₹X (200-DMA + Fib 61.8%), resistance at ₹Y"

### B5. Chart Patterns (only if clearly identifiable from fetched data — never force)
- Continuation: Cup & Handle, Bull Flag, Ascending Triangle
- Reversal: Head & Shoulders (bearish), Inverse H&S (bullish), Double Bottom/Top

### B6. Relative Strength vs Index (report §5.9, T30)
- **Periods:** 1M, 3M, 6M, 1Y, 3Y, 5Y (§0.2), each a price change per §0.3, on the same CMP date.
- **Benchmark:** Nifty 50 only (Tickertape `.NSEI`; the niftyindices CSV as a cross-check). Broad-market and sector indices are not used until a source is verified.
- **T30 columns:** period · stock % · Nifty 50 % · difference (pp).
- 1M–1Y come from the Tickertape daily series; 3Y and 5Y from `duration=5y` weekly points under the §B9 week rule, labelled "W".
- State it as: "+[X]% over 12M vs Nifty 50's +[Y]%: [out/under]performed by [Z] pp."

### B7. Technical Summary
Rate: **Bullish / Cautiously Bullish / Neutral / Cautiously Bearish / Bearish**, in T31.
Provide: entry zone, stop-loss, and technical target (separately from the fundamental target). The rating feeds the split verdict (§D2).

### B8. In-house computation (mandatory: do not use third-party technical snippets)
From the daily closes (Tickertape price API, `duration=1y`; at least 200 points for the 200-DMA):
- SMA(n) = mean of the last n closes, for n = 20, 50, 200.
- RSI(14), Wilder: average gain/loss over the first 14 changes, then avg = (prev × 13 + current) / 14; RSI = 100 − 100 / (1 + avgGain / avgLoss).
- MACD = EMA(12) − EMA(26); signal = EMA(9) of MACD; histogram = MACD − signal. EMA(n): α = 2 / (n + 1), seeded with the SMA of the first n values.
- Beta per TH-COC-2: cov(r_stock, r_nifty) / var(r_nifty) on daily simple returns over matching dates.
- Returns over the §B6 periods vs Nifty 50, using the same dates.
- Print the computation date and the number of data points.

### B9. Rolling trend matrices
**Price matrix (12×12, month-end close):**
- Rows are 12-month windows; each row shifts one month back. Row 1 = the window ending in the latest complete month, Row 2 = the window ending one month earlier, and so on (12 rows).
- Each row has 12 columns of month-end closes, oldest to newest within that window, and a 13th column for the window return = last ÷ first − 1.
- Use the last trading-day close of each month.
  - Tickertape daily covers 1 year. For older months use the **user-supplied NSE daily CSV** (data-sources §10), labelled "C".
  - Only if no CSV exists, use Tickertape weekly points. These are dated the Monday of the week but carry that week's last close, so take the last week whose **Monday + 4 days ≤ month-end** and label it "W". The naive "last point ≤ date" picks a week ending after the date.
  - Validate one value against the annual report "Share Price" at 31-Mar (GRASIM 2,611.15 Mar-25; 2,557.70 Mar-26).
- The same rule applies to quarter-end prices in the P/E history and the implied-discount history. The 10-year P/E history reaches past the 2-year NSE CSV, so older quarter-ends use Tickertape `duration=max` weekly points, labelled "W".
- **Adjustment:** Tickertape prices are adjusted for corporate actions; NSE CSV closes are not. Adjust NSE closes (report-template §3.0b) before mixing the two series.

**Financials matrix (rolling 4 quarters):**
- Rows are TTM windows ending at each of the last 40 quarter-ends (T10 holds 43 quarters, so every row has 4 quarters), oldest → newest.
- Columns: Revenue, EBITDA, PAT (owners), EPS (all TTM), plus the YoY change of TTM revenue and TTM EPS.

---

## C. RISK FRAMEWORK

### C1. Risk Categories (report §8, T45; address every one that applies)
1. **Earnings quality**: accruals, receivables growing faster than revenue, audit qualifications (T23, T24)
2. **Balance sheet**: debt trajectory, interest-cover trend, off-balance-sheet liabilities (T6, T7, T9)
3. **Regulatory / compliance**: SEBI actions, sector regulator, pending litigation (exchange announcements, AR contingent liabilities)
4. **Governance / promoter**: pledging, related-party transactions, promoter selling (T14, T27, T29)
5. **Currency**: import or export exposure by currency (AR MD&A, segment note)
6. **Commodity**: input-cost exposure (AR MD&A, T4 cost lines)
7. **Competition**: new entrants, pricing pressure, substitutes (T16, T18)
8. **Execution**: new-business ramp-up, capex delays, capacity utilisation (transcripts, T28)
9. **Macro**: rate cycle, inflation, GDP, export markets (T21)
10. **Valuation**: premium multiple with no margin of safety (T36–T43)
11. **Concentration**: customer, supplier or geography (AR)

Rate each **CRITICAL / HIGH / MEDIUM / LOW**, with evidence (table refs) and what to monitor.

### C2. Forensic Accounting Flags (report §5.4, T24)
Run these checks on every report, from the filings-based tables:

| Check | Flag if | Source |
|---|---|---|
| Revenue recognition | Revenue growing much faster than CFO | T4, T8 |
| Receivables quality | Debtor days rising while revenue accelerates | T9 |
| Inventory build-up | Inventory days rising sharply and CFO negative | T9, T8 |
| Auditor change | New auditor appointed without explanation | Exchange announcements, AR |
| Audit qualification | Any "except for" opinion or "emphasis of matter" | AR auditor's report |
| Related-party transactions | RPTs growing as % of revenue | AR RPT note |
| Contingent liabilities | Large legal or tax claims vs net worth | AR notes |
| Promoter pledging | Pledged % rising QoQ | T14 |

If the number of flags reaches TH-FOR-1, add a ⚠️ FORENSIC ALERT callout in report §9.

---

## D. RECOMMENDATION FRAMEWORK (report §9)

### D1. Rating bands
Expected return per §0.3, over 12 months.

| Rating | Expected return |
|---|---|
| **BUY** | Above TH-RATE-1 |
| **ADD / Accumulate** | TH-RATE-2 to TH-RATE-1 |
| **HOLD** | TH-RATE-3 to TH-RATE-2 |
| **REDUCE** | TH-RATE-4 to TH-RATE-3, or fundamentals weakening (a Negative Conclusion box in report §5.2, §5.4 or §5.6) |
| **SELL** | Below TH-RATE-4, or significant deterioration (Negative in two or more of those sections) |

### D2. Split verdict
- **Existing holders:** the band from D1.
- **New investors:** one notch lower (TH-RATE-5; BUY → ADD, ADD → HOLD) when the CMP is above the accumulate-zone top (§0.3) or the technical summary (§B7, T31) is Cautiously Bearish or Bearish. HOLD, REDUCE and SELL are the same for both.

### D3. Target price and catalysts
- Derive the target price from the valuation models only; never state it without showing the model.
- List catalysts per TH-CAT-1, with estimated timing and probability (§I).

---

## E. MANAGEMENT QUALITY DEEP-DIVE

This section is frequently the difference between a good and great research report. Cover:

### E1. Promoter Background
- Founder/promoter history: previous ventures, sector expertise, years in industry
- Track record at this company: how has the business grown under their stewardship?
- Source: annual report (Board of Directors section), company website. LinkedIn profiles found by web search are secondary: mark them so.

### E2. Corporate Governance Checklist (report §5.7, T27)
Check each item from the annual report (corporate governance report, board's report, auditor's report) and exchange filings:

| Item | Rule | Source |
|---|---|---|
| Board independence | Independent directors meet TH-GOV-1 (depends on whether the chair is executive or promoter-related) | Governance report |
| Audit committee | Chaired by an independent director; meetings meet TH-GOV-2 | Governance report |
| Auditor | Name the firm and its network (e.g. S.R. Batliboi = EY; Price Waterhouse = PwC; Deloitte Haskins & Sells = Deloitte; B S R & Co. = KPMG; Walker Chandiok = Grant Thornton; MSKA = BDO) | Auditor's report |
| Auditor tenure | Within the rotation limits in TH-GOV-3; a breach is a red flag | Board's report |
| Related-party transactions | Volume and nature: routine operating flows or questionable capital flows | RPT note |
| Promoter remuneration | Whether it crosses TH-GOV-4, and whether the special resolution was passed | Board's report, AGM notice |
| Promoter pledging | Current % and trend | T14 |
| SEBI enforcement | Warning letters, orders, consent orders | SEBI website |

Rate governance **Strong / Adequate / Weak**, with evidence.

### E3. Capital Allocation Track Record (10 years)
How has management used cash over FY[T-9]–FY[T]? Use T8's cumulative CFO, capex and FCF.
- Reinvestment in the core business: capex vs D&A, and the ROIC that followed (T26).
- Acquisitions: cumulative spend (T8) and ROIC before vs after (T26).
- Dividends and buybacks: cumulative payout vs cumulative FCF.
- Balance sheet: net debt at the start vs end of the window (T7).

### E4. Management Guidance Track Record (report §5.7, T28)
Use the **last 6 earnings-call transcripts** (Stage 1 checklist row 3).
- Take every quantified guidance item from the older calls and check it against the actuals that have since been reported. Actuals come from T10 (quarterly), T4/T8 (annual) or T3 (segments).
- Guidance whose period hasn't ended yet is marked "Pending" and is not scored.
- What counts: revenue / volume growth, margin, capex, debt, capacity commissioning dates, and segment targets. Vague statements ("strong demand") are not guidance; leave them out.

| # | Call (date, transcript page) | Guidance (verbatim quote) | Metric | Period targeted | Actual (T# / W#) | Met / Missed / Pending |
|---|---|---|---|---|---|---|

- **Score:** % met among scored items. Credibility is **High** at TH-GUID-1, **Medium** at TH-GUID-2 up to High, and **Low** below that. With fewer scored items than TH-GUID-3, write "insufficient record" and don't rate.
- **Source:** transcripts in `<TICKER>/inputs/`. Otherwise take the transcript PDF links from Screener's Documents section and download them with curl (data-sources §9). Use transcript summaries only if no transcript exists, and mark them secondary.

### E5. Concall Tone Analysis
From the most recent 1–2 concall transcripts, flag:
- **Positive signals**: Specific guidance with numbers, candid discussion of challenges, new business wins
- **Caution signals**: Vague language ("demand environment uncertain"), excessive optimism without data, avoiding analyst questions
- **Red flags**: Changing accounting policies mid-year, blaming macro for company-specific problems, sudden CEO/CFO resignation

---

## F. TAM & MARKET SIZING

For every report, quantify the total addressable market to contextualize the company's growth runway.

### F1. TAM Calculation
- **Top-down**: Total India market size × addressable % for this company's product/service
- **Bottom-up**: Number of potential customers × average spend per customer
- Source: IBEF sector reports, MOSPI data, RBI sectoral credit data, industry associations

Present as:
```
India [Sector] TAM: ₹[X,000] Cr (FY[T]) growing at [Y]% CAGR
Company's current market share: [Z]% (₹[revenue] Cr / ₹[TAM] Cr)
Achievable market share in 5 years (A#): [A]% → Revenue potential: ₹[B] Cr
```

### F2. Runway Assessment
- At current growth rates, how many years of runway does the company have?
- Is the market growing fast enough to support the company's growth without taking share from competitors?
- What % of TAM is already captured — is it still early-stage or approaching saturation?

---

## G. SENSITIVITY ANALYSIS

Every valuation model has assumptions. Show what happens when they change.

### G1. Target Price Sensitivity Tables (report §7.4, T41–T42)
Build two 2-variable tables for the main models. Highlight the base-case cell.

**Example: P/E re-rating**

| | P/E: 30x | P/E: 35x | P/E: 40x | P/E: 45x | P/E: 50x |
|---|---|---|---|---|---|
| EPS: ₹18 | ₹540 | ₹630 | ₹720 | ₹810 | ₹900 |
| EPS: ₹20 | ₹600 | ₹700 | ₹800 | ₹900 | ₹1,000 |
| EPS: ₹22 | ₹660 | ₹770 | ₹880 | ₹990 | ₹1,100 |
| EPS: ₹24 | ₹720 | ₹840 | ₹960 | ₹1,080 | ₹1,200 |
| EPS: ₹26 | ₹780 | ₹910 | ₹1,040 | ₹1,170 | ₹1,300 |

**DCF:** WACC × terminal g, per TH-DCF-6 around the base case (§A5 DCF).

### G2. Margin of Safety
- Margin of safety = (probability-weighted value − CMP) ÷ probability-weighted value.
- **What the price implies:** the reverse-DCF revenue CAGR (§A5 DCF) vs the 9-period actual. Example: "At ₹999 the price implies 18% revenue CAGR for 5 years vs 11% achieved over FY17–26."

---

## H. INSTITUTIONAL FLOW TRACKER

Institutional money flows are one of the most powerful leading indicators for stock price. Build this from BSE/NSE data.

### H1. Bulk & Block Deal History (report §5.8, T29)
**Window:** TH-FLOW-1. Use this window everywhere in the report (§B3, report §5.8).

**Source order** (stop at the first that works; record which one was used in T19):
1. **User-supplied NSE CSV**, from https://www.nseindia.com/report-detail/display-bulk-and-block-deals (filter by symbol, 6 months; both the Bulk and Block tabs). This is Stage 1 checklist row 15. NSE's API is blocked for automated fetch (data-sources §10).
2. **BSE bulk-deals page**: `https://www.bseindia.com/markets/equity/EQReports/BulkDeals.aspx`. It is **untested**: try once, and if it is blocked or JS-only, move on. Don't retry.
3. **Web search**: `"<TICKER>" bulk deal OR block deal <current year>`, and the previous year if the window crosses a year boundary. Use approved news only (data-sources §7). Check each article's date is inside the window.

| Date | Buyer / Seller | Bulk / Block | Buy / Sell | Qty (shares) | Price (₹) | % of equity (W#) | Source |
|---|---|---|---|---|---|---|---|

- Promoter or promoter-group selling is always listed and flagged.
- **No deals found:** write "No bulk/block deals found in <sources checked>, <window>". Never write "no deals occurred" unless the source was the NSE CSV.
- If only source 3 was available, add a T20 row: "bulk/block deals: news-search only, may be incomplete".

### H2. Mutual-Fund Holding Trend
- Use the aggregate MF % from the shareholding-pattern PDFs (Table III, (B)(1) mutual funds) for the latest 8 quarters, shown in T14.
- Fund-level holdings are not used: the only listed source (Trendlyne) is behind a login.

### H3. Flow Signal Interpretation
- Large domestic MF entering / adding = strong conviction signal (they have done deeper due diligence)
- FII entering = global risk-on for India; exiting = risk-off or stock-specific concern
- Promoter pledging falling = confidence; rising = distress signal

---

## I. EVENT CALENDAR & CATALYST TRACKER (report §8, T44)

List catalysts per TH-CAT-1, matching the 12-month target horizon.

| Date (est.) | Event | Expected outcome | Bull impact | Bear impact | Probability |
|---|---|---|---|---|---|
| [Month] | Q[N] FY[T] results | Revenue ~₹X Cr (A#) | Beat → re-rating | Miss → de-rating | [H/M/L] |
| [Month] | Capacity commissioning | Volume ramp-up | Margin expansion | Delay | [H/M/L] |
| [Month] | Corporate action (record date, demerger, listing) | Value unlock | Re-rating | Delay or adverse terms | [H/M/L] |
| [Month] | Budget / policy event (T21) | Duty or tax change | Demand support | Rollback | [H/M/L] |
| [Month] | Large order, contract or regulatory approval | Revenue visibility | Upgrade | Cancellation | [H/M/L] |

**Highest-conviction catalyst:** the single event most likely to move the stock materially, and when.

---

## J. SANITY RANGES (trigger a re-fetch from a second source)

| Check | Re-fetch if |
|---|---|
| P/B | TH-DQ-1 |
| P/E | TH-DQ-2 |
| Ownership % vs shares held ÷ shares outstanding | TH-DQ-3 |
| Market cap vs CMP × shares outstanding | TH-DQ-4 |
| Quarterly revenue vs filing revenue from operations (check whether other income is included) | TH-DQ-5 |
| Technical level (DMA, RSI) vs in-house computation | TH-DQ-6 |
| Any figure, two sources | TH-DQ-7 |

Report both values and which one was used, in the Data Gaps / Reconciliation table.

---

## K. SECTION CONCLUSIONS, ASSUMPTIONS REGISTER & WORKINGS APPENDIX

**Conclusion box (end of every [ANALYSIS] section):**
```
CONCLUSION — [Section]: [Positive / Neutral / Negative]
• [Metric]: [value] vs [benchmark] → [one-clause implication]
• [Metric]: [value] vs [benchmark] → [implication]
• (optional third bullet)
```

**Assumptions Register (A#), in the appendix and cited throughout:**

| A# | Assumption | Value used | Anchor (peer median / own history / guidance / broker) | Source | Range tested | Used in (W#) |
|---|---|---|---|---|---|---|

Every multiple, discount, growth rate, margin, estimate or proxy used anywhere in the report must appear here. If an assumption has no anchor, write "no anchor — judgement" explicitly. In the body, label assumed numbers inline as `ASSUMED (A#)`.

**Workings Appendix (W#):** every calculated figure in the report has one working.

```
W# — <what is being calculated>
Formula:  <symbolic formula>
Inputs:   <name> = <value> [Source: doc p.N / URL, date]  (or ASSUMED, A#)
          <name> = <value> [...]
Steps:    <substituted arithmetic, one line per step>
Result:   <value, unit>   → used in <T# / section>
Check:    <cross-check vs another source, if any, and the difference>
```

Rules:
- One W# per distinct calculation. Repeated calculations (e.g. the P/E at 40 quarter-ends) may share a W# with a table of inputs.
- Show enough steps that a reader can redo the arithmetic with a calculator.
- Group the workings by section (Data pack, Ratios, ROIC/WACC, Technicals, Valuation, Scenarios).
- The body cites them inline: "base value ₹3,308 (W12; A2, A3)".

---

## L. MACRO & POLICY IMPACT (report §5.1, T21)

**Scope:** include a macro variable or policy only when it touches a segment above TH-MACRO-1 (T1), within the TH-MACRO-2 look-back.

| # | Variable / policy | Latest value or status + date | Official source (document no., date) | Segment affected (T1) | Line item hit (T4) | Direction | Impact: ₹ Cr or bps (W# / A#) |
|---|---|---|---|---|---|---|---|

**Source rules** (data-sources §8):
- **Macro values** (repo rate, CPI, IIP, GDP, G-Sec, INR) come from Tier 1 only: RBI / DBIE, MOSPI, FBIL. Commodity prices come from the industry sources in data-sources §8. If the fetch fails, use TradingEconomics and label it.
- **Policies** need an **official document**:
  - Gazette notification (egazette.gov.in), PIB release (pib.gov.in) or Union Budget document (indiabudget.gov.in);
  - CBIC customs / GST notification (cbic.gov.in) or DGTR anti-dumping finding (dgtr.gov.in);
  - a sector-regulator circular (SEBI, RBI, IRDAI, TRAI, CEA, PNGRB…).
  Cite the document number and date.
- **News** (approved list, data-sources §7) may explain a policy or show that one is pending. On its own, it can't support a quantified impact: mark such rows "news only" and don't quantify them.
- **Impact:** quantify only when the transmission is arithmetic (e.g. duty % × import volume, rate change × floating debt), as a W#. Otherwise write "not quantified". Unquantified rows don't feed the valuation.
- The 5.1 Conclusion box states the net quantified impact (₹ Cr EBITDA and % of FY[T] EBITDA) and the number of unquantified rows.

