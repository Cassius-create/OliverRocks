import argparse
import json
from data_pool import ingest_data, clean_data


def main():
    parser = argparse.ArgumentParser(description="Ingest and clean data files")
    parser.add_argument("input_file", help="Path to the input data file")
    parser.add_argument("-o", "--output", help="Optional path to write cleaned data")
    args = parser.parse_args()

    data = ingest_data(args.input_file)
    cleaned = clean_data(data)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(cleaned, f, indent=2)
    else:
        print(json.dumps(cleaned, indent=2))


if __name__ == "__main__":
    main()
