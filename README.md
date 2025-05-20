# OliverRocks

This project provides a simple data pool for ingesting unstructured files and producing a cleaned dataset.

## Features

- Ingest CSV, TSV, JSON, XML or plain text files using the `data_pool` package.
- Normalize keys and remove duplicate records.
- Command line interface to process files and output cleaned data.

## Usage

Run the CLI by specifying the input file and optional output file:

```bash
python main.py path/to/input.csv -o cleaned.json
```

The cleaned data will be written to the specified output file in JSON format. If no output file is given, the result is printed to standard output.

## Tests

To run the test suite:

```bash
python -m unittest discover tests
```
