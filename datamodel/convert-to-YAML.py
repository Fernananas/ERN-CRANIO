import csv
import yaml
import os

date = '20250101'
# List of input and output file paths
file_pairs = [
    (f'files/{date}/molgenis.csv', f'data/schema.yaml'),
    (f'files/{date}/molgenis_settings.csv', f'data/settings.yaml')
]

# Convert CSV to YAML
for csv_file, yaml_file in file_pairs:
    if os.path.exists(csv_file):
        with open(csv_file, 'r', encoding='latin1') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        with open(yaml_file, 'w', encoding='utf-8') as yamlfile:
            yaml.dump(rows, yamlfile, default_flow_style=False)

        print(f"Converted {csv_file} to {yaml_file}")
    else:
        print(f"File {csv_file} does not exist.")