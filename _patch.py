import re, sys

# ── publications_section.yaml ──────────────────────────────────────────────
path_pub = "marine-cv-docs/publications_section.yaml"
with open(path_pub, encoding="utf-8") as f:
    text = f.read()

orig_len = len(text)

# 1. A Review of Cloud Computing... (GJI) → article_type: review
text = text.replace(
    "  doi: 10.1093/gji/ggaf322\n  journal: Geophysical Journal International\n  date: 2025-01",
    "  doi: 10.1093/gji/ggaf322\n  journal: Geophysical Journal International\n  article_type: review\n  date: 2025-01",
)

# 2. Ambient field seismology... (Comptes Rendus) → article_type: review
text = text.replace(
    "  doi: 10.5802/crgeos.310\n  url: https://doi.org/10.5802/crgeos.310\n  journal: Comptes Rendus. G\u00e9oscience, 357\n  date: 2025-01",
    "  doi: 10.5802/crgeos.310\n  url: https://doi.org/10.5802/crgeos.310\n  journal: Comptes Rendus. G\u00e9oscience, 357\n  article_type: review\n  date: 2025-01",
)

# 3. Quiet Anthropocene, quiet Earth (Science) → article_type: perspective
text = text.replace(
    "  doi: 10.1126/science.abd8358\n  url: https://doi.org/10.1126/science.abd8358\n  journal: Science, 369\n  date: 2020-01",
    "  doi: 10.1126/science.abd8358\n  url: https://doi.org/10.1126/science.abd8358\n  journal: Science, 369\n  article_type: perspective\n  date: 2020-01",
)

added = len(text) - orig_len
if added == 0:
    print("WARNING: no substitutions made – check source strings", file=sys.stderr)
else:
    with open(path_pub, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"publications_section.yaml: +{added} chars ({text.count('article_type')} article_type fields inserted)")

# ── update_cv_stats.py ─────────────────────────────────────────────────────
path_stats = "scripts/update_cv_stats.py"
with open(path_stats, encoding="utf-8") as f:
    src = f.read()

OLD = """        total += 1
        is_preprint = any(kw in journal_raw for kw in PREPRINT_KEYWORDS)
        is_review = any(kw in journal_raw for kw in REVIEW_KEYWORDS)
        is_t1 = any(kw in journal_raw for kw in T1_JOURNALS)
        is_t2 = any(kw in journal_raw for kw in T2_JOURNALS)

        if is_preprint:
            counts["preprint"] += 1
        elif is_review:
            counts["review"] += 1
        elif is_t1:
            counts["t1"] += 1
        elif is_t2:
            counts["t2"] += 1
        else:
            counts["t3"] += 1"""

NEW = """        total += 1
        # Explicit article_type field takes priority (review, perspective, etc.)
        article_type = str(entry.get("article_type", "")).lower()
        if article_type in ("review", "perspective", "commentary"):
            counts["review"] += 1
            continue

        # Strip submission-status prefixes ("in review in X") before keyword matching
        journal_clean = re.sub(
            r"^(in review in|in press in|accepted in|preprint on|under review)\\s+",
            "",
            journal_raw,
        )
        is_preprint = any(kw in journal_clean for kw in PREPRINT_KEYWORDS)
        is_review = any(kw in journal_clean for kw in REVIEW_KEYWORDS)
        is_t1 = any(kw in journal_clean for kw in T1_JOURNALS)
        is_t2 = any(kw in journal_clean for kw in T2_JOURNALS)

        if is_preprint:
            counts["preprint"] += 1
        elif is_review:
            counts["review"] += 1
        elif is_t1:
            counts["t1"] += 1
        elif is_t2:
            counts["t2"] += 1
        else:
            counts["t3"] += 1"""

if OLD not in src:
    print("WARNING: classifier block not found verbatim in update_cv_stats.py", file=sys.stderr)
    # show a snippet to diagnose
    idx = src.find("total += 1")
    print(repr(src[idx:idx+400]))
else:
    src = src.replace(OLD, NEW)
    # Ensure `re` is imported
    if "import re" not in src:
        src = "import re\n" + src
    with open(path_stats, "w", encoding="utf-8") as f:
        f.write(src)
    print("update_cv_stats.py: classifier updated OK")
