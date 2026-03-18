import sys, re
sys.path.insert(0, ".")
import yaml

T1_JOURNALS = {
    "nature", "science", "proceedings of the national academy",
    "pnas", "nature geoscience", "nature communications",
    "science advances", "nature climate", "nature methods",
}

with open("marine-cv-docs/publications_section.yaml") as f:
    data = yaml.safe_load(f)

for entry in (data if isinstance(data, list) else data.get("entries", [])):
    article_type = str(entry.get("article_type", "")).lower()
    journal_raw = str(entry.get("journal", "")).lower()
    journal_clean = re.sub(
        r"^(in review in|in press in|accepted in|preprint on|under review)\s+",
        "", journal_raw)
    if article_type in ("review", "perspective", "commentary"):
        tier = "REVIEW"
    elif any(kw in journal_clean for kw in T1_JOURNALS):
        tier = "T1"
    else:
        tier = "other"
    if tier in ("T1", "REVIEW"):
        print(f"{tier:8s} | {entry.get('title','')[:60]} | {entry.get('journal','')}")
