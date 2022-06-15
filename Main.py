import os
import csv
import sys

data = "AllStatisticLines.csv"
fields = []
rows = []

with open(data, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(f"\nRow Count: {len(rows)}")
print()

print("\nField Names: " + ", ".join(field for field in fields))
print()

for row in rows:
    if row[1] == "Draymond Green":
        print(row)
