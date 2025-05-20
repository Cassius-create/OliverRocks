import csv
import json
import os
import xml.etree.ElementTree as ET


def _read_csv(path, delimiter=','):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return [row for row in reader]


def _read_json(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return [data]
    else:
        return [{'value': data}]


def _read_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    records = []
    for item in root:
        record = {}
        for child in item:
            record[child.tag] = child.text
        if record:
            records.append(record)
    return records


def _read_text(path):
    with open(path, encoding='utf-8') as f:
        return [{'value': line.strip()} for line in f if line.strip()]


def ingest_data(file_path):
    """Ingest a data file and return a list of dictionaries."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.csv':
        return _read_csv(file_path, delimiter=',')
    elif ext == '.tsv':
        return _read_csv(file_path, delimiter='\t')
    elif ext == '.json':
        return _read_json(file_path)
    elif ext == '.xml':
        return _read_xml(file_path)
    else:
        return _read_text(file_path)
