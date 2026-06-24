import csv
import re

INPUT_FILE = "data/dataset.csv"
OUTPUT_FILE = "data/dataset_prelabeled.csv"

# Journalist/source attribution patterns that signal news posts
NEWS_BRACKET_PATTERN = re.compile(
    r"^\[(?:Charania|Fischer|Krawcz|Scotto|Haynes|Windhorst|Stein|Begley|"
    r"Smith|Jackson|Amick|O'Connor|Chiang|Iko|Nehm|Vecenie|Robbins|"
    r"Bleacher Report|StatMuse|Stat\]|Bill Simmons|7PM|Kenney|Basket News)",
    re.IGNORECASE,
)

# Keywords that suggest verifiable statistical analysis
ANALYSIS_KEYWORDS = [
    "basketball-reference.com", "statmuse.com", "screwball.com",
    "win shares", "true shooting", "efg%", "ts%", " bpm", "vorp",
    "per game", "all-time record", "all time record",
    "points per", "rebounds per", "assists per", "blocks per",
    "field goal", "free throw percentage", "three-point percentage",
]

# Patterns that signal junk (not labelable)
JUNK_PATTERNS = [
    re.compile(r"^https?://", re.IGNORECASE),          # bare URLs
    re.compile(r"imgur\.com", re.IGNORECASE),
    re.compile(r"^E: thanks", re.IGNORECASE),
]

JUNK_EXACT = {
    "comments moving so fast no one will know i love my wife",
    "how am i getting suns stuff then?",
}


def is_junk(text: str) -> bool:
    stripped = text.strip()
    if len(stripped) < 20:
        return True
    for pat in JUNK_PATTERNS:
        if pat.search(stripped):
            return True
    if stripped.lower() in JUNK_EXACT:
        return True
    # LeBron instagram caption (emojis + hashtags, no NBA discourse value)
    if "striveforgreatness" in stripped.lower():
        return True
    return False


def is_news(text: str, row_idx: int) -> bool:
    # User-collected news batch: data rows 151-201 (0-indexed)
    if 151 <= row_idx <= 201:
        return True
    stripped = text.strip()
    if NEWS_BRACKET_PATTERN.match(stripped):
        return True
    # Named player/coach statements reported verbatim (e.g., "Anthony Edwards has responded:")
    if re.match(r"^[A-Z][a-zA-Z ]+(?:has responded|said|says|on |:)\s*[\"«]", stripped):
        return True
    # "THE NBA'S 72 YEAR STREAK" style factual announcements in bold
    if stripped.startswith("**THE NBA") and "STREAK" in stripped:
        return True
    # Suspension/transaction announcements ("Morant is suspended")
    if re.search(r"\b(?:suspended|traded|signed|waived|hired|fired)\b", stripped, re.IGNORECASE):
        if len(stripped) < 180:
            return True
    return False


def is_analysis(text: str, row_idx: int) -> bool:
    # User-collected analysis batch: data rows 202-251 (0-indexed)
    if row_idx >= 202:
        return True
    text_lower = text.lower()
    signal_count = sum(1 for kw in ANALYSIS_KEYWORDS if kw in text_lower)
    # Multiple analysis signals in a long post
    if signal_count >= 2 and len(text) > 200:
        return True
    # Specific known analysis posts from the comment batch
    if "first team in nba history to come back from multiple 3-1 deficits" in text_lower:
        return True
    if "giannis shooting 17-19 from the ft line" in text_lower:
        return True
    return False


def is_reaction(text: str) -> bool:
    stripped = text.strip()
    # Very short posts are almost always reactions
    if len(stripped) < 80:
        return True
    text_lower = stripped.lower()
    reaction_signals = [
        r"\blmao\b", r"\blmfao\b", r"\bbro\b", r"\bomg\b", r"holy shit",
        r"as a .{3,20} fan", r"i can'?t (?:believe|even|put)",
        r"what the (?:fuck|hell)", r"oh my god",
    ]
    if any(re.search(pat, text_lower) for pat in reaction_signals):
        return True
    # Emotional exclamations
    if stripped.count("!") >= 3:
        return True
    return False


def prelabel(text: str, row_idx: int) -> str:
    if is_junk(text):
        return "junk"
    if is_news(text, row_idx):
        return "news"
    if is_analysis(text, row_idx):
        return "analysis"
    if is_reaction(text):
        return "reaction"
    return "hot_take"


def main():
    rows = []
    seen_texts = set()

    with open(INPUT_FILE, newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            text = row["text"]
            text_key = text.strip().lower()

            # Flag duplicates as junk
            if text_key in seen_texts:
                label = "junk"
            else:
                seen_texts.add(text_key)
                label = prelabel(text, i)

            rows.append({
                "text": text,
                "pre_label": label,
                "final_label": "",
                "pre_labeled": "True",
                "notes": row.get("notes", ""),
                "changed": "",
            })

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["text", "pre_label", "final_label", "pre_labeled", "notes", "changed"]
        )
        writer.writeheader()
        writer.writerows(rows)

    # Summary
    counts = {}
    for r in rows:
        counts[r["pre_label"]] = counts.get(r["pre_label"], 0) + 1

    print(f"Pre-labeled {len(rows)} rows -> {OUTPUT_FILE}")
    print()
    for label in ["analysis", "hot_take", "reaction", "news", "junk"]:
        print(f"  {label:10s}: {counts.get(label, 0)}")


if __name__ == "__main__":
    main()
