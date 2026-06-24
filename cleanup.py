import csv

INPUT_FILE = "data/dataset_prelabeled.csv"

rows = []
with open(INPUT_FILE, newline="", encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for row in reader:
        final_label = row.get("final_label", "").strip()
        pre_label = row.get("pre_label", "").strip()
        pre_labeled = row.get("pre_labeled", "").strip().lower()

        if final_label == "junk" or not final_label:
            continue

        if pre_labeled == "true" and pre_label:
            row["changed"] = "True" if final_label != pre_label else "False"
        else:
            row["changed"] = ""

        rows.append(row)

with open(INPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f, fieldnames=["text", "pre_label", "final_label", "pre_labeled", "notes", "changed"]
    )
    writer.writeheader()
    writer.writerows(rows)

counts = {}
for r in rows:
    label = r["final_label"]
    counts[label] = counts.get(label, 0) + 1

changed_count = sum(1 for r in rows if r.get("changed") == "True")

print(f"Wrote {len(rows)} rows to {INPUT_FILE}")
print()
for label in ["analysis", "hot_take", "reaction", "news"]:
    print(f"  {label:10s}: {counts.get(label, 0)}")
print()
print(f"  Changed labels : {changed_count}")
print(f"  Agreed labels  : {sum(1 for r in rows if r.get('changed') == 'False')}")
print(f"  User-added rows: {sum(1 for r in rows if r.get('changed') == '')}")
