# Stage 1 Research Brief Template

Write the brief to `<TICKER>/reports/<TICKER>_research_brief.md`. Keep it factual: no valuation, no rating.
Mark every Stage 1 fact as **provisional** with its source. Stage 2 re-verifies these facts against the annual report.

---

```markdown
# <COMPANY> — Research Brief (Stage 1)
Prepared: <DD-Mon-YYYY> · Skill: india-equity-research

## 1. Identifiers
| Field | Value | Source |
|---|---|---|
| Company | | |
| NSE ticker / BSE code | | |
| Tickertape SID / slug | | |
| Company IR page | | |
| Latest close (₹, date) | | Tickertape price API |
| Company type | Operating / Holdco / BFSI / Group with lender (A6) | reasoning in one line |
| Fiscal year end | | |
| Latest reported quarter | | |
| Tickertape 43-quarter test | Pass / Fail (PAT, EPS of latest 4 quarters vs filings) | SKILL Stage 1 step 3 |

## 2. Structure (provisional)
### 2.1 Reportable segments
| Segment | What it covers | Latest FY revenue | Source |
|---|---|---|---|

### 2.2 Listed subsidiaries & listed investments
| Entity | Ticker | Relationship | Approx. stake % | Source |
|---|---|---|---|---|

### 2.3 Material unlisted subsidiaries / JVs
| Entity | Business | Stake % | Source |
|---|---|---|---|

## 3. Inputs inventory (`<TICKER>/inputs/`)
| File | Period | Type | Pages | Text extractable? |
|---|---|---|---|---|

## 4. Documents checklist
| # | Document | Status | Where to download |
|---|---|---|---|
| 1 | Latest integrated annual report (FY<YY>) | ✅ / ❌ | <IR URL> |
| 1a | Annual report from 5 years earlier (FY<YY−5>), for years FY[T-9]–FY[T-5] of the 10-year tables. Skip it if the latest AR has 10-year highlights | | <IR URL> / BSE |
| 2 | Last 4 quarterly results filings, plus older ones for the 43-quarter T10 if the Tickertape test failed | | Screener Documents links / BSE / IR |
| 3 | Last 6 earnings-call transcripts (guidance track record) | | Screener Documents links / BSE / IR |
| 4 | Latest investor presentation | | IR |
| 5 | Annual report of each listed subsidiary | | each IR |
| 6 | Subsidiary financials (only if material) | | IR |
| 7 | NSE daily closes, last 2 years: company + each listed subsidiary (CSV) | | https://www.nseindia.com/get-quotes/equity?symbol=<TICKER> → Historical Data |
| 8 | Nifty 50 daily closes, same period (CSV) | | https://www.niftyindices.com/reports/historical-data |
| 9 | Shareholding-pattern PDFs, last 8 quarters (older quarters of the 40-quarter T14: summary % from the BSE page) | | https://www.bseindia.com/corporates/shpSecurities.aspx?scripcd=<BSE_CODE> or IR |
| 10 | 10Y G-Sec benchmark on the valuation date (a number is enough) | | https://www.fbil.org.in |
| 11 | Latest-quarter results of each listed subsidiary | | Subsidiary IR / BSE |
| 12 | Exchange intimations for pending or recent corporate actions (allotments, acquisitions, PE deals) | | Company IR announcements / BSE corp-announcements |
| 13 | Industry-size source per business (association data, RBI FSR, AR MD&A) | | see data-sources §8 |
| 14 | Overseas peer financials (only if fewer than 7 Indian peers) | | Company AR / stockanalysis.com `/financials/` |
| 15 | NSE bulk & block deals, last 6 months (CSV, both tabs) | | https://www.nseindia.com/report-detail/display-bulk-and-block-deals |

Items 7–15 can't be fetched automatically (data-sources §10), so ask the user for them up front.

## 5. Frameworks that apply
- [x] DCF, mandatory (holdco: standalone businesses only) — or [ ] residual income instead (lender / insurer)
- [ ] SOTP (holdco) · [ ] A6 lender consolidation · [ ] P/B (BFSI) · [ ] EV/Sales (loss-making segments)

## 6. Proposed peer universe (to verify in Stage 2)
### 6.1 Holdco peers (if holdco; ≥7)
### 6.2 Per business (≥7 each where they exist)
| Business | Industry label | Candidate peers (ticker) |
|---|---|---|

## 7. Known issues / carry-forward
- Prior reports found: <paths or "none">
- Known errors or gaps to avoid: <list>

## 8. Stage 2 prompt
<filled-in prompt from the template below, inside a fenced code block>
```

---

# Stage 2 Prompt Template

Fill every `<…>` from the brief. Delete lines that don't apply (e.g. the SOTP lines for an operating company).

```
Use the india-equity-research skill, Stage 2, to produce the full research report for
<COMPANY> (NSE: <TICKER>, BSE: <BSE_CODE>, Tickertape SID: <SID>).

Context:
- Research brief: <TICKER>/reports/<TICKER>_research_brief.md. Load it first.
- Inputs: <TICKER>/inputs/ (<n> documents; scanned: <list or "none">).
- Company type: <type>. Frameworks: <DCF or residual income / SOTP / A6 / P/B / EV/Sales>.
- Prior report(s) for continuity, not as a data source: <paths or "none">. Known issues to avoid: <list>.

Company-specific requirements:
1. Segments to cover: <segment list>.
2. Holdings to value as shares held × latest CMP: <entity (ticker) list>. Unquoted holdings at fair value
   from the annual report: <list>. Recent changes to verify on BSE: <e.g. preferential allotment, date>.
3. Peer sets (≥7 each where they exist): holdco → <list>; <business 1> → <list>; <business 2> → <list> …
4. Items flagged in the brief that need special attention: <e.g. lender consolidation, demerger,
   suspended listing, pending dividend from subsidiary>.

Standard requirements (all companies):
5. Prices from the Tickertape price API as of the latest close. Market cap = CMP × annual-report share count.
6. Pass the completeness gate. If an item is missing after two attempts, stop and ask me, naming the
   document and line item.
7. Build every template table (T1–T46, with a "not applicable" line for those that don't apply) and chart
   (C1–C8). Annual tables cover 10 years in the wide format; T10 collects 43 quarters and quarterly series
   show 40. Adjust per-share data for corporate actions and footnote accounting breaks. Include the TTM P/E history, the 12×12 month-end close
   matrix, the rolling TTM financials matrix, the source reconciliation and the peer tables.
8. Put every calculation in the Workings Appendix (W#) and every assumed number in the Assumptions
   Register (A#), with its anchor and the range tested. Cite them in the text.
9. Compute technicals and beta in-house. Consensus = MarketScreener's dated calls + the Trendlyne average.
10. Write only <TICKER>/reports/<TICKER>_Equity_Report_<Mon><YYYY>.md. Run the quality check and the
    D1–D5 self-score, and paste a ≤150-word summary in chat.
```

---

# Stage 1 Prompt (generic: the user can paste this for any company)

```
Use the india-equity-research skill, Stage 1 (scoping), for <COMPANY NAME or TICKER>.
Inputs folder: <TICKER>/inputs/ (it may be empty or partial).
Produce the research brief and the filled-in Stage 2 prompt. Do not value the company or give a rating.
```
