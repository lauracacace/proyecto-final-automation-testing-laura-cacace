import csv
import os


def read_csv(path):
    """Return list of dicts from a CSV file path."""
    full = os.path.abspath(path)
    rows = []
    with open(full, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({k: v.strip() for k, v in r.items()})
    return rows
