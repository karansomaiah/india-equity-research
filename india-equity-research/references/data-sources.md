# Data Sources for India Equity Research

## ⚡ Rules
1. **Choose sources by data type**, using the tier tables below. Use Tier 1 when it exists. Tier 2 is for cross-checks and filling gaps. Never use a ❌ source.
2. **Company filings outrank every aggregator.** When a filing and an aggregator disagree, use the filing and footnote the difference.
3. **Record the source, date and page/URL for every figure.**

Reliability evidence for the tiers comes from a field test on GRASIM, 25 Sep – 4 Oct 2026. Summary in §9.

---

## 1. Price, market cap, price history, index levels

| Tier | Source | Access | Notes |
|---|---|---|---|
| 1 | **Tickertape price API** | `https://api.tickertape.in/stocks/charts/inter/<SID>?duration=1y` (daily) · `duration=3y` / `5y` / `max` (weekly points) | JSON `{ts, lp, v}`. The last point is the last close. Verified for stocks and for Nifty (`<SID>=.NSEI`). The SID is the suffix of the Tickertape slug (e.g. `grasim-industries-GRAS` → `GRAS`). **Daily data covers 1 year only**; `2y` is rejected ("invalid duration"). Weekly points are dated the **Monday** of the week, but `lp` is the **close of that week's last trading day**. |
| 1 | **Tickertape info API (CMP + ratios)** | `https://api.tickertape.in/stocks/info/<SID>` | `data.ratios.lastPrice` = **official close** (matches the daily chart). Also `marketCap`, `pe` (last-FY EPS), `ttmPe`, `pb`, `roe`, `beta`, `52wHigh`/`52wLow` (intraday). Use this for the CMP of the company and every peer. |
| ❌ for CMP | Tickertape quotes / search `quote.price` | `stocks/quotes?sids=<SID>` | `price` = **last traded price**, not the close (GRASIM 06-Oct-26: 2,969 vs official close 2,958). Trendlyne and some CSV exports show the same last-traded value. |
| 1 | **NSE historical daily closes, user-downloaded CSV** | https://www.nseindia.com/get-quotes/equity?symbol=<TICKER> → "Historical Data" | **Use for any date older than 1 year** (P/E history quarter-ends, 12×12 matrix, implied-discount history). The NSE API cannot be fetched automatically (§10), so ask the user. Field test: matched Tickertape closes on 244/248 days; the 4 mismatches were last-traded prices, so prefer the Tickertape close where both exist. |
| 1 | **Nifty 50 daily closes, user-downloaded CSV** | https://www.niftyindices.com/reports/historical-data | Cross-check for beta and relative returns. Field test: identical to Tickertape `.NSEI` on every overlapping day. |
| 1 | Tickertape stock page | `https://www.tickertape.in/stocks/<slug>` | Date-stamped CMP, market cap, 52-week range. |
| 2 | Google Finance card (web search), 5Paisa | — | CMP fallback only. |
| 2 | MarketScreener | quote page | Shows last close with date; useful as a cross-check. |
| ❌ | Screener displayed price | — | Often a stale cached price. |
| ❌ | Yahoo Finance | — | Blocked for CMP (v1.1 benchmark discrepancy). |
| ❌ | Search-result snippet market caps | — | Gave an inconsistent ABCap market cap / P/B (119x) in testing. |

**Market cap:** compute it as CMP × shares outstanding from the annual report share-capital note. Websites may exclude treasury or partly paid shares (Tickertape implied 67.3 Cr Grasim shares vs 68.06 Cr in the annual report).

**Finding a Tickertape SID.**
1. Try `https://api.tickertape.in/search?text=<ticker or name>&types=stock` and take the row whose `ticker` matches exactly.
2. The search index is **stale for listings after ~2024 and for renamed tickers**. It returned nothing for ABLBL, NTPCGREEN, TATACAP, ACMESOLAR, SANATHAN, CHEMPLASTS, EPIGRAL, NUVOCO, INDIGOPNTS, POONAWALLA and KAMAHOLD, and old names for L&TFH and SRTRANSFIN.
3. In that case, web-search `tickertape.in stocks <company name>` (restrict the domain to tickertape.in) and read the SID from the slug.
4. Always verify with `stocks/info/<SID>`: `info.ticker` must equal the NSE ticker.
5. New SIDs are often 3 letters. Verified SIDs:

| SID | Company | SID | Company | SID | Company |
|---|---|---|---|---|---|
| ABL | ABLBL | NTP | NTPCGREEN | KPI | KPIGREEN |
| TATAC | TATACAP | MAGM | POONAWALLA | NUV | NUVOCO |
| INDIG | INDIGOPNTS | ABS | ABSLAMC | CHEMP | CHEMPLASTS |
| SANA | SANATHAN | MFM | EPIGRAL | MODIA | LORDSCHLO |
| LTFH | LTF | SRTR | SHRIRAMFIN | JKLC | JKLAKSHMI |
| KAM | KAMAHOLD | ACMES | ACMESOLAR | | |

Akzo Nobel India now appears under ticker JSWDULUX (SID AKZO).

**Price adjustments:** Tickertape history is adjusted for corporate actions. For example, the ABFRL series before its May-2025 demerger is scaled down. To value a stake at a past date, use the company's reported fair value from that quarter's presentation, not an adjusted price. **NSE CSV closes are unadjusted:** adjust them and every per-share series before mixing them with Tickertape data (report-template §3.0b).

---

## 2. Financial statements

| Tier | Source | Notes |
|---|---|---|
| 1 | **Annual report** (`<TICKER>/inputs/` or company IR / BSE) | Financial Highlights page (5-year consolidated + standalone, including net debt excluding financial services), audited statements, notes. |
| 1 | **Quarterly / Q4 results filings** (`<TICKER>/inputs/` or BSE) | Audited Statement of Assets & Liabilities, cash flow, segment note, basic EPS. |
| 2 | **Tickertape financials API** | `https://api.tickertape.in/stocks/financials/balancesheet/<SID>/annual/normal?count=10` · `/financials/income/<SID>/interim/normal?count=12` (quarterly) · `/income/<SID>/annual/...` · `/cashflow/...`. Consolidated JSON with granular fields (`balMint` = minority interest, `balTdeb` = total debt, `balCsti` = cash + ST investments). |
| 2 | **Screener.in** | `https://www.screener.in/company/<TICKER>/consolidated/` | Fast 10-year view, ratios, shareholding. The HTML is easy to fetch. |

**10-year coverage (report-template §3).** The latest AR's 5-year highlights + audited statements cover FY[T-4]–FY[T]; the FY[T-5] AR covers FY[T-9]–FY[T-5]. Fill any lines the highlights omit (e.g. cash-flow detail, NCI split) from Tickertape `annual/normal?count=10` or Screener, tag those year columns `TT`/`SCR`, and reconcile one overlapping filing year in T15. **Standalone** statements (T5, T6b, T8b) come from the same two ARs. For years they don't cover, use Screener's standalone page `https://www.screener.in/company/<TICKER>/` (no `/consolidated/`), tagged `SCR-S`. Tickertape `normal` financials are consolidated, so don't use them for standalone. For the 43 quarters of T10, each results filing gives the current and year-ago quarter. Tickertape `interim/normal?count=43` is tested in Stage 1 (SKILL step 3; counts above 12 are unverified): use it only if PAT and EPS for the latest 4 quarters match the filings. Revenue won't match, because Tickertape includes other income.

### Known pitfalls (verified on GRASIM FY26)

| Item | Screener | Tickertape | Correct handling |
|---|---|---|---|
| "Total Liabilities" | Includes equity (whole right-hand side) | Excludes owners' equity **and** NCI | Use the audited layout. |
| Non-controlling interest (NCI) | Hidden inside "Other Liabilities" | Separate (`balMint`) and counted inside "Total Equity" | Always show NCI on its own line. |
| Borrowings | Includes lease liabilities | Total debt includes leases | Show borrowings and leases separately. |
| Cash | Inside "Other Assets" | "Cash & ST investments" **includes insurance-business investments and assets held to cover linked liabilities** | Use cash + bank + liquid current investments from the filing. |
| Total assets | Net of the deferred tax asset | Net of the deferred tax asset | Expect ~DTA difference vs the filing. |
| EPS | Restated figures | As first reported | Use filings (latest restated); footnote originals. |
| Quarterly revenue | Revenue from operations | **Total revenue incl. other income** | Use revenue from operations. |
| "Operating profit" vs EBITDA | Before **all** interest, including the NBFC's interest cost → overstates EBITDA for groups with a lender (Grasim FY26: 36,296 vs company 25,872) | similar | Use company-reported EBITDA and net debt excluding financial services. |
| Segment data | ✗ | ✗ | Filings only. |
| Subsidiary EBITDA (e.g. UltraTech) | — | `incEbi` = total revenue − opex (17,443 vs company 17,598) | Use the company figure. For a quarter not in a press release, compute it from the subsidiary's results statement as **PBT before exceptional items + finance costs + D&A**. This reproduced UltraTech FY26 at 17,597.74 vs 17,598 reported. It **includes other income**, so say so when deriving a parent segment residual. |

### Tickertape financials: field map (used for peer tables)

| Statement | Fields |
|---|---|
| Annual income (`incTrev`, `incEbi`, `incPbi`, `incIoi`, `incPbt`, `incNinc`, `incEps`) | Total revenue **incl. other income**; EBITDA incl. other income; EBIT (PBIT); interest; PBT; net income; EPS |
| Quarterly income | Same fields with a `qInc…` prefix (e.g. `qIncTrev`, `qIncEbi`) |
| Balance sheet (`balTdeb`, `balCsti`, `balTeq`, `balMint`, `balTcso`) | Total debt; cash + ST investments; total equity (incl. NCI); NCI; shares outstanding (crore) |
| Holdings (`/stocks/holdings/<SID>`) | Last 6 quarters: `pmPctT` promoter %, **`pmPctP` promoter pledge %**, `fiPctT` FII % (incl. GDRs), `diPctT` DII %, `mfPctT`, `isPctT`, `rhPctT` |

### PDF extraction notes
- **Page numbers:** pypdf numbers pages from 0. Cite **viewer page = pypdf index + 1** and label it "PDF p.N". The GRASIM brief mixed the two conventions.
- Some results PDFs are OCR'd scans (e.g. UltraTech Q1 FY27); the plain text is jumbled across columns. Use `page.extract_text(extraction_mode="layout")` on the specific page to read the table rows.
- Excel files from the user: unzip the `.xlsx` and read `xl/sharedStrings.xml` + `xl/worksheets/*.xml` if `openpyxl` is not installed.
- HEIC screenshots: convert with `sips -s format png <in.heic> --out <out.png>` and read the PNG. If the filename contains a narrow no-break space (macOS screenshots), copy it first via `ls` globbing.
- **Indian digit grouping:** "3,31,75,66,167" = 3,317,566,167. Never retype share counts by hand. Strip the commas programmatically and sanity-check value = shares × price against the company's reported fair value. In the GRASIM run, a retyped Vodafone Idea count was 10× too large.

---

## 3. Holdings, share counts, ownership

| Tier | Source | Notes |
|---|---|---|
| 1 | Parent annual report → standalone note "Investments in Subsidiaries, JVs and Associates" and "Other Investments" | Shares held, ownership %, book and fair values. Includes non-subsidiary listed stakes (e.g. Hindalco, Vodafone Idea). |
| 1 | Parent annual report → Form AOC-1 | Summary financials of every subsidiary/JV. Use when subsidiary volumes are scanned. |
| 1 | Subsidiary's latest BSE shareholding pattern | For changes after the balance-sheet date (e.g. preferential issues). |
| 1 | **Subsidiary's allotment intimation** (company IR site, "Announcements") | Exact shares allotted, price and the post-allotment total share count. Example: ABCL 23-Jun-26 PDF on adityabirlacapital.com. It downloaded via WebFetch (saved binary) and was read with pypdf. **Value a stake as shares held × price; % ownership is only a label.** Basic vs fully diluted % can differ (ABCap 53.06% vs 52.30%). |
| 1 | **Company's quarterly shareholding-pattern PDFs** (Reg. 31), latest 8 quarters (older quarters of the 40-quarter T14: Promoter / FII / DII / public % from https://www.bseindia.com/corporates/shpSecurities.aspx?scripcd=<BSE_CODE>), user-downloaded from the company IR site or BSE | Promoter %, pledge declaration ("Whether any shares held by promoters are pledged…? No"), Table III categories: (B)(1) domestic institutions, MF, insurance, PF; (B)(2) foreign institutions; (B)(4) non-institutions; (C2) employee trust; shareholder count. |
| 2 | Tickertape `stocks/holdings/<SID>` | 6 quarters incl. pledge %. FII % **includes GDRs**. |
| 2 | Screener shareholding block | 12 quarters + shareholder count. FII % **excludes GDRs**, so Screener and Tickertape FII % differ by the GDR share (GRASIM Jun-26: 14.63% vs 17.17%; GDRs 2.53%). |
| 2 | Company press releases / announcements | e.g. preferential allotments. |
| ❌ | Undated web snippets for ownership % | Testing found 57.27% used where the annual report showed **56.11%**. |

**Share-count reconciliation:** the shareholding pattern total can differ from the annual report (GRASIM 68,05,80,576 incl. partly paid vs 68,06,08,871 in the AR). Use the AR count for market cap and footnote the difference.

**Quarter-end fair values of other investments:** investor presentations list standalone "Vodafone Idea", "Other Investments", "Liquid Investments" and "Net Debt / (Surplus)" every quarter. Use these for the implied-discount history instead of reconstructing values from adjusted price series.

---

## 4. Technicals, beta, returns

| Tier | Source | Notes |
|---|---|---|
| 1 | **Compute in-house** from the Tickertape price API | DMA, RSI(14), beta, returns. Formulas in analysis-frameworks §B. |
| 2 | Chartink, TradingView (via search) | Cross-check only. |
| ❌ | Investing.com / undated snippets | Testing found a 200-DMA of ₹2,777 vs ₹2,975 computed. |
| ❌ | Trendlyne technicals | Behind a login. |

---

## 5. Analyst consensus & forecasts

| Tier | Source | Notes |
|---|---|---|
| 1 | **MarketScreener broker-research page** | `https://www.marketscreener.com/quote/stock/<SLUG>/news-broker-research/`. The `/consensus/` page did not render via WebFetch (Oct-26), but this page lists named, dated actions (e.g. Jefferies Buy ₹3,910, 14-Aug). Find the slug with a web search "marketscreener <company> analyst recommendations" (GRASIM: `GRASIM-INDUSTRIES-LTD-9058936`). Dates without a year are in the current year. |
| 1 | **Trendlyne consensus-estimates page** | `https://trendlyne.com/equity/consensus-estimates/<id>/<TICKER>/<slug>/`. Gives the average target and analyst count (GRASIM: ₹3,838 from 10 analysts). Find `<id>` by web-searching on trendlyne.com; a guessed id returns another company (e.g. id 1150 was RPP Infra). |
| 2 | Approved news (broker notes) | **Check the article date.** URLs with a `125…` ID prefix were 2025 articles. |

---

## 6. Management commentary

| Tier | Source | Notes |
|---|---|---|
| 1 | Earnings-call transcripts (`<TICKER>/inputs/` or BSE / company IR) | Quote directly with page. |
| 1 | Investor presentations | Segment KPIs. |
| 2 | Transcript summaries (Cofacto, GuruFocus, Yahoo highlights) | Mark as secondary. Use only if the transcript is unavailable. |

---

## 7. News

| Tier | Source | Notes |
|---|---|---|
| 1 | NSE / BSE corporate announcements | Primary disclosures. |
| 2 | ET Markets, Moneycontrol, Mint, CNBC-TV18, **NDTV Profit** (formerly BQ Prime), Hindu BusinessLine | — |
| 2 | Business Standard | Direct fetch returns 403. Use search snippets and cite the article date. |
| ❌ | Finviz | US-listed stocks only; no NSE/BSE coverage. |
| ❌ | Reddit, X, Telegram, Substack, blogs, Wikipedia (for figures) | — |

---

## 8. Macro, industry, credit

| Data | Tier 1 | Tier 2 |
|---|---|---|
| 10Y G-Sec | **FBIL G-Sec benchmark**: https://www.fbil.org.in (Benchmarks → G-Sec); RBI Weekly Statistical Supplement: https://www.rbi.org.in/Scripts/BS_ViewWSS.aspx. Ask the user for the value if the fetch fails. | TradingEconomics (gave 7.22% vs FBIL 7.198%, 6-Oct-26) |
| Policy rate, credit | RBI / DBIE | TradingEconomics |
| NBFC sector size | **RBI Financial Stability Report** (https://www.rbi.org.in/Scripts/FsReports.aspx). The stress-test footnote gives the sample's total advances and its coverage (Jun-26 FSR: ₹34.45 lakh Cr = ~95% of non-govt UL+ML NBFC advances → ~₹36.3 lakh Cr). The chart "Credit Growth and Share" gives YoY growth. | — |
| CPI, IIP, GDP | MOSPI | TradingEconomics |
| Cement production | DPIIT Index of Eight Core Industries (https://eaindustry.nic.in): **gives index values only, not tonnes**. Use it to verify growth. | Economic Survey figure via approved news (FY26: 491.4 Mt, +8.6%) |
| Caustic soda capacity | Alkali Manufacturers Association of India: https://ama-india.org/industry-data/caustic-soda/ (FY26 6.7 MTPA; FY25 6.40 MTPA, production 5.02 Mt) | — |
| Renewable capacity | MNRE physical progress; company AR MD&A (India RE 274.7 GW, Mar-26) | — |
| Industry size & market share | Company annual report MD&A (e.g. Grasim: paints industry ~₹76,000 Cr), industry bodies, IBEF | Approved news. ❌ market-research SEO pages (e.g. Mordor, Research&Markets "VSF market 6.19 Mt") |
| Global fibre (VSF / man-made cellulosic) | Lenzing annual report (https://www.lenzing.com/investors/publications); company AR MD&A (China = 65–70% of CSF) | — |
| Overseas listed peers (no Tickertape coverage) | Company annual reports; cninfo.com.cn (China) | **stockanalysis.com** `/quote/<exch>/<code>/statistics/` (multiples) and `/financials/` (3-year revenue). WebFetch works for statistics; the user can screenshot financials. Exchange codes: `vie/LNZ`, `sha/600409`, `she/000420`, `she/002092`. |
| Credit ratings | CRISIL, ICRA, CARE, India Ratings, Acuité | — |
| Regulatory | SEBI, sector regulators (TRAI, IRDAI, AMFI, PNGRB, CEA, DPIIT) | — |
| Policy documents (report §5.1) | Gazette (egazette.gov.in), PIB (pib.gov.in), Union Budget (indiabudget.gov.in), CBIC customs / GST notifications (cbic.gov.in), DGTR anti-dumping findings (dgtr.gov.in), sector-regulator circulars. Cite the document number and date (analysis-frameworks §L). | Approved news, to explain a policy only; it can't support a quantified impact |

---

## 9. Field-test summary (GRASIM, Sep–Oct 2026)

| Source | Result |
|---|---|
| Company filings / annual report | ✅ Most complete. Only source for segments, stakes, cash, contingent liabilities, governance. |
| Tickertape API | ✅ Matched the audited balance sheet line for line once mapped. Daily prices and Nifty data work. |
| Screener | ✅ Matched audited totals; condensed layout hides NCI and cash. |
| MarketScreener | ✅ Dated broker actions. |
| Trendlyne | ⚠️ Target only; the rest is behind a login. |
| Investing.com technicals | ❌ Wrong 200-DMA. |
| Search-snippet market caps / ownership | ❌ Inconsistent. |
| Business Standard direct fetch | ❌ 403. |
| **Stage 2 run, 6-Oct-26** | |
| Tickertape `stocks/info` | ✅ Official close + ratios for ~65 peers in one pass; field-mapped EV/EBITDA and ROCE. |
| Tickertape search | ⚠️ Stale for new listings (see §1 for the fix). |
| BSE API / NSE API | ❌ Blocked (§10). |
| User-downloaded NSE CSVs, shareholding PDFs, results PDFs | ✅ Exact; resolved every remaining gap in one round. |
| Company IR PDFs via WebFetch | ✅ Binary saved; readable with pypdf (ABCL allotment). |
| nsearchives.nseindia.com PDFs | ❌ WebFetch timed out. |
| MarketScreener `/news-broker-research/` | ✅ Dated broker calls. |
| Trendlyne `/consensus-estimates/` | ✅ Average target and analyst count. |
| stockanalysis.com | ✅ Overseas peer multiples (Tier 2). |
| **BAJAJFINSV Stage 1, 7-Oct-26** | |
| nsearchives.nseindia.com PDFs **via `curl -A "<browser UA>" -H "Referer: https://www.nseindia.com/"`** | ✅ Downloaded (2.3 MB investor deck). The WebFetch timeout above is a WebFetch problem, not a block. |
| BSE filing PDFs (`bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=<id>.pdf`, `bseindia.com/xml-data/corpfiling/AttachHis/<id>.pdf`) **via curl + browser UA + `Referer: https://www.bseindia.com/`** | ✅ Annual report (18.7 MB), transcripts, intimations. Only the BSE **API** is blocked. |
| **Screener company page → "Documents" section** (`screener.in/company/<TICKER>/consolidated/`) | ✅ Fastest way to find filing URLs: direct BSE links to every annual report, each quarter's transcript / PPT, and the latest announcements. Parse `<a href>` inside `id="documents"`. |
| NSE iXBRL integrated filing (`nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_<format>_<id>_<DDMMYYYYhhmmss>_iXBRL_WEB.html`) | ✅ Consolidated P&L, segment revenue / result / assets / liabilities, EPS, in **₹ lakh**. Find it by web-searching `nsearchives BAJAJFINSV <DDMMYYYY>`. Has no notes and no standalone statements, so still ask for the results PDF. Some iXBRL labels are offset by one cell (e.g. "Face value" showing paid-up capital): read values next to their own label. |
| Tickertape search `marketCap` | ❌ Wrong (BAJAJFINSV 92,957 vs `stocks/info` 2,80,387). Use `stocks/info` only. |
| Company IR sites built in JS (aboutbajajfinserv.com) | ⚠️ curl returns no document links. Use Screener Documents or BSE instead. |
| International investor decks | ⚠️ Some are in **USD** (BFS: ₹94.5/$ stated on p.2). Never quote converted figures in the report; get ₹ from filings. |

---

## 10. Blocked for automated fetch → ask the user (with these links)

| Data | Blocked endpoint (observed Oct-2026) | Ask the user to download from |
|---|---|---|
| Daily price history > 1 year (company, listed subsidiaries) | `nseindia.com/api/historical/...` → 503; Tickertape daily is 1 year only | https://www.nseindia.com/get-quotes/equity?symbol=<TICKER> → Historical Data → CSV, from (today − 2 years) to today |
| Nifty 50 history | — (Tickertape works for 1 year) | https://www.niftyindices.com/reports/historical-data (NIFTY 50, CSV) |
| Shareholding pattern, 8 quarters | `api.bseindia.com/...shpSecSummary...` → Access Denied | https://www.bseindia.com/corporates/shpSecurities.aspx?scripcd=<BSE_CODE>, or company IR "Shareholding Pattern" PDFs |
| Bulk & block deals, last 6 months | NSE API blocked; BSE `BulkDeals.aspx` untested (try once) | https://www.nseindia.com/report-detail/display-bulk-and-block-deals → filter symbol, 6 months, Bulk + Block tabs → CSV. Fallback: dated news search (analysis-frameworks §H1) |
| Corporate announcements (deal terms, allotments, board-meeting dates) | `api.bseindia.com/...AnnSubCategoryGetData` → Access Denied | https://www.bseindia.com/stock-share-price/<slug>/<ticker>/<BSE_CODE>/corp-announcements/, or the company IR site. **Try first:** take the announcement PDF links from Screener's Documents section and curl them with a browser UA + BSE referer (§9, 7-Oct-26). That works for recent announcements, ARs, transcripts and PPTs. |
| Subsidiary results (latest quarter) | BSE API blocked | Subsidiary IR site, or BSE <code> → Results |
| 10Y G-Sec benchmark | RBI/FBIL pages not reliably parseable | https://www.fbil.org.in (G-Sec benchmark) — the user can just send the number |
| Industry data behind web apps | — | AMAI (caustic), DPIIT eaindustry.nic.in (core index), RBI FSR (NBFC), Lenzing AR (fibre) |
| Overseas peer 3-year financials | cninfo is not machine-friendly | stockanalysis.com `/financials/` (screenshot) or company AR |

**Protocol:** before writing, send the user **one prioritised list** with the item, exact URL and suggested filename:
1. **Priority 1:** affects valuation or a template table.
2. **Priority 2:** fills peer or market-share gaps.
3. **Priority 3:** confirms facts currently held as assumptions.

Then wait for the files, ingest them, and record any remaining items in Data Gaps (T20).

## 11. Always fetch (ask in Stage 1 if missing)
These were missing in the GRASIM run and changed the report once supplied:
1. **NSE daily close CSV, last 2 years**, for the company and every listed subsidiary used in SOTP. Plus a Nifty 50 CSV for the same period.
2. **Shareholding-pattern PDFs, last 8 quarters** (pledge, GDR split, institution categories).
3. **10Y G-Sec benchmark yield** on the valuation date (FBIL).
4. **Latest-quarter results of each listed subsidiary.** They give exact comparatives for derived segment numbers and the post-issue book value for P/B checks.
5. **Exchange intimations for every pending or recent corporate action** named in the results notes (allotments, acquisitions, PE investments into subsidiaries). They carry the EV, shares and price, which the results notes omit.
6. **Industry-size source per business** (association data, RBI FSR, company AR MD&A).
7. **Overseas peer financials** (3-year revenue) where Indian peers are fewer than 7.
8. **NSE bulk & block deals CSV, last 6 months** (both tabs). It is the only complete source; news search can miss deals (analysis-frameworks §H1).

---

## Fetch sequence

0. Load the Stage 1 brief; extract from `<TICKER>/inputs/` (annual report, results) into `<TICKER>/inputs/_extracted/`.
1. CMP via `stocks/info/<SID>` + 1-year daily prices + Nifty (Tickertape API); older daily closes from the user's NSE CSVs (§10).
2. Tickertape financials API + Screener: cross-check against filings.
3. Shareholding (user-supplied shareholding PDFs; Tickertape holdings for pledge; Screener as cross-check), subsidiary allotment intimations.
4. Transcripts, last 6 (local, else Screener Documents links + curl, else BSE).
5. Peers (Stage 2, Step 6): resolve SIDs (§1), then `stocks/info` + `financials/income` (annual, `count=10`) + `financials/balancesheet` + price charts (`1y` daily, `5y` weekly) per peer and for the Nifty 50; overseas peers via stockanalysis.com.
6. MarketScreener `/news-broker-research/` + Trendlyne `/consensus-estimates/`.
7. Bulk & block deals (user NSE CSV, else analysis-frameworks §H1 order).
8. Macro (FBIL, RBI / DBIE, MOSPI), policy documents (§8), news (company IR announcements, then approved media).
9. Completeness gate (SKILL.md Stage 2, Step 4). For anything blocked, send the §10 link list to the user before writing.
