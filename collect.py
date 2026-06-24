import requests
import csv
import time
import random
from pathlib import Path

SUBREDDIT = "nba"
OUTPUT_FILE = Path("data/dataset.csv")
SUBMISSION_URL = "https://api.pullpush.io/reddit/search/submission/"
COMMENT_URL = "https://api.pullpush.io/reddit/search/comment/"


def fetch(url, params, retries=3):
    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, timeout=20)
            r.raise_for_status()
            return r.json().get("data", [])
        except requests.RequestException as e:
            print(f"  Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(3)
    return []


def is_valid(text, min_len=30):
    if not text or not text.strip():
        return False
    if text.strip().lower() in {"[deleted]", "[removed]"}:
        return False
    if len(text.strip()) < min_len:
        return False
    return True


def collect_submissions(target=150):
    results = []
    params = {"subreddit": SUBREDDIT, "size": 100, "sort_type": "score", "sort": "desc"}

    while len(results) < target:
        batch = fetch(SUBMISSION_URL, params)
        if not batch:
            break
        for post in batch:
            body = (post.get("selftext") or "").strip()
            title = (post.get("title") or "").strip()
            if body and is_valid(body):
                text = f"{title}\n{body}" if title else body
            elif is_valid(title, min_len=20):
                text = title
            else:
                continue
            results.append(text)
        params["before"] = batch[-1]["created_utc"]
        time.sleep(1.5)

    return results[:target]


def collect_comments(target=150):
    results = []
    params = {"subreddit": SUBREDDIT, "size": 100, "sort_type": "score", "sort": "desc"}

    while len(results) < target:
        batch = fetch(COMMENT_URL, params)
        if not batch:
            break
        for comment in batch:
            body = (comment.get("body") or "").strip()
            if is_valid(body):
                results.append(body)
        params["before"] = batch[-1]["created_utc"]
        time.sleep(1.5)

    return results[:target]


def main():
    print("Collecting r/NBA submissions...")
    submissions = collect_submissions(target=150)
    print(f"  Collected {len(submissions)} submissions")

    print("Collecting r/NBA comments...")
    comments = collect_comments(target=150)
    print(f"  Collected {len(comments)} comments")

    all_texts = submissions + comments
    random.shuffle(all_texts)

    rows = [{"text": t, "label": "", "notes": ""} for t in all_texts]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "label", "notes"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSaved {len(rows)} candidates to {OUTPUT_FILE}")
    print("Next: open the CSV and manually fill in the 'label' column.")
    print("Valid labels: analysis, hot_take, reaction, news")
    print("Delete rows that don't fit any label. Target: ~250 labeled rows.")


if __name__ == "__main__":
    main()
