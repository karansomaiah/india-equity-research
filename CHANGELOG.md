# Changelog

All notable changes to the India Equity Report Skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-03-03

### 🎉 Initial Public Release

The first production-ready version of the India Equity Research Report Skill.

### ✨ Features

#### Core Analysis
- **Multi-source data integration** (Screener.in, BSE, NSE, Google Finance, Tickertape)
- **Live price verification** with stale cache detection
- **Comprehensive financial analysis** (5-year P&L, quarterly trends, balance sheet, cash flows)
- **Institutional-grade metrics** (ROE, ROCE, ROIC, working capital ratios)

#### Valuation Models
- **P/E re-rating** with peer/historical comparison
- **EV/EBITDA multiples** approach
- **DCF (Discounted Cash Flow)** - 3-stage model
- **P/B ratio** (for BFSI stocks)
- **Blended target price** with configurable weights
- **Sensitivity analysis tables** (2-variable)

#### Risk Management
- **11-category risk framework** (governance, regulatory, execution, macro, etc.)
- **Forensic accounting checks** (8 red flags: CFO/PAT, accruals, receivables, etc.)
- **Management quality assessment** with credibility scoring
- **Corporate governance scorecard**

#### Technical Analysis
- **Trend identification** (50/200 DMA)
- **Momentum indicators** (RSI, MACD, Stochastic, ADX)
- **Support/Resistance levels** with pivot points
- **Volume & delivery analysis**
- **Relative strength vs index**

#### Advanced Features
- **DuPont ROE decomposition** (3-factor analysis)
- **ROIC vs WACC spread** (value creation/destruction)
- **TAM (Total Addressable Market) sizing**
- **Institutional flow tracking** (MF holdings, bulk/block deals)
- **Event calendar & catalyst tracker**
- **Scenario analysis** (Bull/Base/Bear cases)

#### Output Quality
- **Professional DOCX generation** (1,500-3,000 words)
- **Inline source citations** for every data point
- **Zero-hallucination guardrails** (7 layers of verification)
- **SEBI-compliant disclaimers**
- **Markdown summary** in chat

### 🛡️ Anti-Hallucination Measures

- ✅ Mandatory source citations for all financial figures
- ✅ Stale data flagging (if > 6 months old)
- ✅ No analyst consensus invention (only cite if fetched)
- ✅ Formula-free reports (displays ₹ numbers, not `=GOOGLEFINANCE(...)`)
- ✅ Quality check before publishing (9-point checklist)
- ✅ Screener.in CMP never used (known stale cache issue)
- ✅ Live price verification via Google Finance web_search

### 📊 Tested Stocks

Successfully generated reports for:
- **Large-cap**: RELIANCE, HDFCBANK, INFY, TCS, ITC
- **Mid-cap**: DIXON, LATENTVIEW
- **Small-cap/SME**: MACFOS (BSE: 543787)

Across sectors:
- Conglomerates, BFSI, IT Services, Electronics Manufacturing, B2B Distribution

### 📚 Documentation

- ✅ Comprehensive README.md with feature overview
- ✅ Step-by-step WALKTHROUGH.md for beginners
- ✅ Detailed INSTALL.md with troubleshooting
- ✅ Example reports with commentary (examples/)
- ✅ CONTRIBUTING.md guide
- ✅ MIT LICENSE with financial disclaimers

### 🐛 Known Issues

1. **Screener.in occasional timeouts**
   - Workaround: Retry mechanism built-in
   - Fallback: Tickertape.in

2. **Very new IPOs (< 1 month)**
   - Limited historical data available
   - Generates shorter reports with disclaimer

3. **Illiquid stocks**
   - Wide bid-ask spreads
   - Report flags liquidity risk

### 🔮 Roadmap for v1.1

Planned enhancements:
- [ ] FII/DII flow auto-tracking
- [ ] Options data integration (PCR, max pain)
- [ ] Automated peer discovery
- [ ] Excel (.xlsx) output format
- [ ] Quarterly report auto-updates

---

## [0.9.0-beta] - 2026-02-15

### 🧪 Beta Testing Phase

Internal testing version with core features.

### Added
- Basic SKILL.md workflow structure
- Analysis frameworks (fundamental, technical, valuation)
- Report template (20 sections)
- Data sources documentation
- Quality check procedures

### Changed
- Migrated from hardcoded data to live fetching
- Improved error handling for missing data
- Enhanced source citation format

### Fixed
- Formula embedding in CMP field (added quality check)
- Screener.in stale price issue (added Google Finance verification)
- Missing quarterly data handling

### Testing
- Tested on 10 stocks (RELIANCE, HDFCBANK, INFY, TCS, DIXON, etc.)
- Identified and fixed 12 major bugs
- Validated output against Tier-1 brokerage reports

---

## [0.5.0-alpha] - 2026-01-20

### 🌱 Alpha Version

Initial proof-of-concept.

### Added
- Basic equity report generation
- Screener.in integration
- Simple P/E valuation
- DOCX output using `docx` skill

### Limitations
- No live price verification
- Limited error handling
- Basic template (10 sections)
- No technical analysis

---

## Version Numbering

**Format:** MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes (e.g., YAML schema changes, template restructuring)
- **MINOR**: New features (e.g., new valuation models, data sources)
- **PATCH**: Bug fixes, documentation updates

**Examples:**
- `1.0.0` → `1.1.0`: Added FII flow tracking (new feature)
- `1.1.0` → `1.1.1`: Fixed Screener timeout handling (bug fix)
- `1.1.1` → `2.0.0`: Changed YAML frontmatter structure (breaking change)

---

## Upgrade Guide

### From 0.9.0-beta to 1.0.0

**Breaking Changes:** None

**New Features:**
- Enhanced forensic accounting (8 checks vs 4)
- ROIC-WACC spread analysis
- Event calendar with catalyst probability

**Migration:**
1. Replace skill folder with new version
2. No changes needed to existing queries
3. Old reports remain compatible

### From 0.5.0-alpha to 1.0.0

**Breaking Changes:**
- Report template completely restructured
- YAML frontmatter format changed

**Migration:**
1. Delete old skill folder
2. Install new version fresh
3. Regenerate any saved reports (old format deprecated)

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to suggest changes.

Report bugs via [GitHub Issues](https://github.com/[username]/india-equity-report-skill/issues).

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**Stay updated:** Watch this repository for release notifications.
