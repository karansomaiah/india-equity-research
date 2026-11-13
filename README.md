# india-equity-research

A Claude Code skill for filings-first equity research on NSE/BSE-listed Indian companies. It works in two stages:

| Stage | You say | It writes |
|---|---|---|
| 1 · Scoping | `Use the india-equity-research skill, Stage 1 (scoping), for <COMPANY or TICKER>.` | `<TICKER>/reports/<TICKER>_research_brief.md`: company facts, a documents checklist with download links, and a ready-to-run Stage 2 prompt |
| 2 · Report | The Stage 2 prompt from the brief | `<TICKER>/reports/<TICKER>_Equity_Report_<Mon><YYYY>.md`: a Markdown report with a 10-year data pack, numbered tables T1–T46, quarterly charts, DCF and peer valuation, an Assumptions Register and a Workings Appendix |

The skill loads only when you name it.

## Install (Claude Code CLI)

Symlink the skill folder into your personal skills directory, so edits in the repo take effect immediately:

```bash
git clone git@github.com:karansomaiah/india-equity-research.git
ln -sfn "$PWD/india-equity-research/india-equity-research" ~/.claude/skills/india-equity-research
```

Check it with `ls -l ~/.claude/skills/india-equity-research`; it should point into this repo.

## Working folders

Run Claude Code from a project folder (not this repo). Each company gets its own folder there:

```
<TICKER>/
  inputs/       ← filings you download (annual reports, results, transcripts, CSVs)
    _extracted/ ← extracts the skill writes, with page references
  reports/      ← research brief and reports
```

## Layout

```
india-equity-research/
  SKILL.md                     ← workflow, completeness gate, quality checks
  references/
    analysis-frameworks.md     ← §0 register (thresholds, coverage, definitions), methods
    data-sources.md            ← source tiers, verified endpoints, blocked sources
    report-template.md         ← Stage 2 report structure, tables T1–T46, charts
    scoping-template.md        ← Stage 1 brief and the Stage 2 prompt
  scripts/check_skill.py       ← consistency checker
  MAINTAINING.md               ← edit checklist
  CHANGELOG.md
```

## Changing the skill

Follow [`india-equity-research/MAINTAINING.md`](india-equity-research/MAINTAINING.md). Every threshold lives once, in `analysis-frameworks.md` §0.1. After any edit, add a CHANGELOG entry and run:

```bash
python3 india-equity-research/scripts/check_skill.py
```

## Disclaimer

Reports are for informational and educational use only. They are not investment advice or SEBI-registered research.

## License

MIT, see [LICENSE](LICENSE).
