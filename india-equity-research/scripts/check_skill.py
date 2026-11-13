#!/usr/bin/env python3
"""Consistency check for the india-equity-research skill.

Run after every edit to the skill:  python3 scripts/check_skill.py
Exit code 0 = clean, 1 = errors found. Warnings don't fail the run.

Checks
  1. Threshold IDs: every TH-* cited is defined in analysis-frameworks §0.1,
     and every defined TH-* is cited somewhere.
  2. Hard-coded thresholds: comparison operators with numbers outside the
     register (allow-listed exceptions below, each with a reason).
  3. Table / chart numbers: T# and C# cited anywhere exist in report-template,
     and T numbers there run without gaps.
  4. Section references (analysis-frameworks §X, report §X, data-sources §N,
     report-template §X) point to headings that exist.
  5. Stale phrases left over from older coverage settings.
  6. CHANGELOG: newest entry is well-formed and the file was updated after the
     other skill files.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = {
    "SKILL": "SKILL.md",
    "AF": "references/analysis-frameworks.md",
    "DS": "references/data-sources.md",
    "RT": "references/report-template.md",
    "ST": "references/scoping-template.md",
}
TEXT = {k: open(os.path.join(ROOT, v), encoding="utf-8").read() for k, v in F.items()}
errors, warnings = [], []


def lines(key):
    return TEXT[key].split("\n")


def af_register_span():
    """Line range (start, end) of analysis-frameworks §0, exclusive end."""
    ls = lines("AF")
    start = next(i for i, l in enumerate(ls) if l.startswith("## 0."))
    end = next(i for i, l in enumerate(ls) if i > start and l.startswith("## A."))
    return start, end


# ---------------------------------------------------------------- 1. TH IDs
TH = re.compile(r"\bTH-[A-Z]+-\d+\b")
defined = {}
for i, l in enumerate(lines("AF")):
    m = re.match(r"^\| (TH-[A-Z]+-\d+) \|", l)
    if m:
        if m.group(1) in defined:
            errors.append(f"[TH] {m.group(1)} defined twice in the register")
        defined[m.group(1)] = i
cited = {}
for key in F:
    for i, l in enumerate(lines(key)):
        if key == "AF" and re.match(r"^\| TH-[A-Z]+-\d+ \|", l):
            continue
        for t in TH.findall(l):
            cited.setdefault(t, []).append(f"{F[key]}:{i+1}")
for t, where in sorted(cited.items()):
    if t not in defined:
        errors.append(f"[TH] {t} cited but not defined in §0.1 ({', '.join(where[:3])})")
for t in sorted(defined):
    if t not in cited:
        errors.append(f"[TH] {t} defined in §0.1 but never cited")

# ------------------------------------------------- 2. hard-coded thresholds
# A comparison operator (symbol or words) followed by a number, outside the register.
OP = re.compile(r"(?:[<>≤≥]|>=|<=)\s*[−-]?\s*₹?\d"
                r"|\b(?:above|below|more than|less than|at least|at most|exceeds?)\s+[−-]?\d+(?:\.\d+)?\s?(?:%|x\b|pp\b|bp\b)",
                re.I)
ALLOW = [  # (regex on the line, reason)
    (r"≥ ?7\b.*peer|peer.*≥ ?7\b|≥7 per business|≥7 candidate|≥ ?7 each|≥ ?7\)", "peer-count coverage setting (§0.2)"),
    (r"≤ ?150[ -]words?|≤ ?6 bullets|≤ ?10-line", "report-format coverage setting (§0.2)"),
    (r"≤ ?28 characters", "table-label formatting rule"),
    (r"≥ ?2 standalone-value assumptions", "procedure: number of SOTP variants, not a cut-off"),
    (r"start or end value is ≤ 0|start or end value ≤ 0|\" if the start or end", "mathematical: CAGR undefined"),
    (r"Monday \+ 4 days ≤ month-end", "date arithmetic, not a threshold"),
    (r"older than TH-|> 1 year|Daily price history >", "data-range description"),
]
r0, r1 = af_register_span()
for key in F:
    for i, l in enumerate(lines(key)):
        if key == "AF" and r0 <= i < r1:
            continue
        if not OP.search(l):
            continue
        if any(re.search(rx, l) for rx, _ in ALLOW):
            continue
        errors.append(f"[NUM] possible hard-coded threshold at {F[key]}:{i+1}: {l.strip()[:110]}")

# ------------------------------------------------------ 3. tables / charts
rt_tables = set(re.findall(r"\bT(\d+)[a-z]?\b", TEXT["RT"]))
nums = sorted(int(n) for n in rt_tables)
if nums:
    missing = [n for n in range(1, nums[-1] + 1) if n not in nums]
    if missing:
        errors.append(f"[T#] report-template skips table numbers: {missing}")
max_t = nums[-1] if nums else 0
for key in F:
    for i, l in enumerate(lines(key)):
        for n in re.findall(r"(?<![\w§])T(\d+)[a-z]?\b", l):
            if int(n) > max_t or int(n) == 0:
                errors.append(f"[T#] T{n} at {F[key]}:{i+1} is not a report-template table")
rt_charts = sorted(int(n) for n in re.findall(r"\*\*C(\d+)\*\*", TEXT["RT"]))
max_c = rt_charts[-1] if rt_charts else 0
for key in F:
    for i, l in enumerate(lines(key)):
        for n in re.findall(r"(?<![\w§(])C(\d+)\b(?!\))", l):
            if int(n) > max_c:
                warnings.append(f"[C#] C{n} at {F[key]}:{i+1} is above the last chart C{max_c}")

# ------------------------------------------------------ 4. section references
def heading_ids(key, pattern):
    return {m.group(1) for l in lines(key) for m in [re.match(pattern, l)] if m}

af_ids = heading_ids("AF", r"^#{2,4} ([0-9A-L](?:\.\d+)?[0-9]*[a-z]?)[.\s]")
rt_ids = heading_ids("RT", r"^#{2,3} (\d+(?:\.\d+)?[a-z]?)[.\s]")
rt_ids |= {m for m in re.findall(r"^\| (\d+\.\d+) \|", TEXT["RT"], re.M)}
rt_ids |= {m for m in re.findall(r"\*\*(\d+\.\d+) ", TEXT["RT"])}
ds_ids = heading_ids("DS", r"^## (\d+)\.")
# A bare "§X" inherits the last document named earlier on the same line. With no
# document named, letter IDs (A–L) and 0.x belong to analysis-frameworks; numeric
# IDs belong to the file itself (SKILL and scoping default to data-sources).
SID = re.compile(r"[0-9A-L](?:\.\d+)?[0-9]*[a-z]?")
AFREF = re.compile(r"analysis-frameworks\s+([A-L]\d+[a-z]?)\b")
DEFAULT = {"AF": "analysis-frameworks", "RT": "report-template", "DS": "data-sources",
           "SKILL": "data-sources", "ST": "data-sources"}
NAMED = re.compile(r"analysis-frameworks|report-template|data-sources|\breport\b")
for key in F:
    for i, l in enumerate(lines(key)):
        found = []
        for m in re.finditer(r"§\s?(" + SID.pattern + r")", l):
            before = NAMED.findall(l[:m.start()])
            sid = m.group(1)
            if before:
                doc = before[-1]
            elif re.match(r"[A-L]|0\.", sid):
                doc = "analysis-frameworks"
            else:
                doc = DEFAULT[key]
            found.append((doc, sid))
        found += [("analysis-frameworks", m.group(1)) for m in AFREF.finditer(l)]
        for doc, sid in found:
            if re.match(r"[A-L]|0\.", sid) and doc in ("report", "report-template"):
                doc = "analysis-frameworks"  # e.g. "Rules (analysis-frameworks)" column, "report §5.2 ... §A1a"
            if doc == "analysis-frameworks":
                target, ids = "analysis-frameworks", af_ids
            elif doc in ("report", "report-template"):
                target, ids = "report-template", rt_ids
            else:
                target, ids = "data-sources", ds_ids
            if sid not in ids:
                errors.append(f"[§] {F[key]}:{i+1} cites {target} §{sid}, which has no heading")

# ------------------------------------------------------------ 5. stale phrases
STALE = ["9 quarter", "8–12 quarters", "8-12 quarters", "3-yr", "3yr", "last 3-5 years", "last 3–5 years",
         "next 6 months", "T1–T20", "T21–T22", "40-quarter pack", "count=40", "up to 37 rows",
         "fetch from RBI", "Q1FY17", "5-year median TTM P/E (from the history table)"]
for key in F:
    for i, l in enumerate(lines(key)):
        for p in STALE:
            if p in l:
                errors.append(f"[STALE] '{p}' at {F[key]}:{i+1}")

# ----------------------------------------------------------------- 6. changelog
cl_path = os.path.join(ROOT, "CHANGELOG.md")
cl = open(cl_path, encoding="utf-8").read()
m = re.search(r"^## \[(\d+\.\d+\.\d+)\] — (\d{4}-\d{2}-\d{2})", cl, re.M)
if not m:
    errors.append("[LOG] CHANGELOG has no '## [x.y.z] — YYYY-MM-DD' entry")
others = [os.path.join(ROOT, v) for v in F.values()]
others += [os.path.join(ROOT, p) for p in ("MAINTAINING.md", "scripts/check_skill.py") if os.path.exists(os.path.join(ROOT, p))]
newest = max(others, key=os.path.getmtime)
if os.path.getmtime(newest) > os.path.getmtime(cl_path) + 1:
    errors.append(f"[LOG] {os.path.relpath(newest, ROOT)} changed after CHANGELOG.md: add an entry")

# ----------------------------------------------------------------- report
print(f"india-equity-research check · version {m.group(1) if m else '?'} · "
      f"{len(defined)} thresholds, T1–T{max_t}, C1–C{max_c}")
for e in errors:
    print("ERROR  ", e)
for w in warnings:
    print("WARN   ", w)
print("OK" if not errors else f"{len(errors)} error(s)")
sys.exit(1 if errors else 0)
