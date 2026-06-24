import csv

INPUT_FILE = "data/dataset_prelabeled.csv"
OUTPUT_FILE = "data/dataset.csv"

rows = []
with open(INPUT_FILE, newline="", encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append({
            "text": row["text"],
            "label": row["final_label"],
            "notes": row.get("notes", ""),
        })

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "label", "notes"])
    writer.writeheader()
    writer.writerows(rows)

counts = {}
for r in rows:
    counts[r["label"]] = counts.get(r["label"], 0) + 1

print(f"Exported {len(rows)} rows to {OUTPUT_FILE}")
for label in ["analysis", "hot_take", "reaction", "news"]:
    print(f"  {label:10s}: {counts.get(label, 0)}")
