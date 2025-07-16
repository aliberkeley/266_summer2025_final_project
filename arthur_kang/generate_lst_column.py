import csv, json
from pathlib import Path

DATASETS = [
    ("climate_dev.csv", "climate_dev_with_lst.csv"),
    ("climate_test.csv", "climate_test_with_lst.csv"),
    ("edu_dev.csv", "edu_dev_with_lst.csv"),
    ("edu_test.csv", "edu_test_with_lst.csv"),
]
TEXT_COLUMN = "source_article"

from construct_logical_structure_tree import construct_logical_structure_tree

for infile, outfile in DATASETS:
    in_path  = Path(infile)
    out_path = Path(outfile)

    with in_path.open(newline="", encoding="utf-8") as fin, \
         out_path.open("w", newline="", encoding="utf-8") as fout:

        reader = csv.DictReader(fin)
        fieldnames = reader.fieldnames + ["lst"]
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            text = row.get(TEXT_COLUMN, "").strip()
            tree = construct_logical_structure_tree(text)
            row["lst"] = json.dumps(tree, ensure_ascii=False)
            writer.writerow(row)

    print(f"Wrote {out_path} with Logical-Structure Trees added.")

print("All complete")