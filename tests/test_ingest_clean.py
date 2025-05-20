import json
import os
import unittest

from data_pool import ingest_data, clean_data


class TestIngestClean(unittest.TestCase):
    def setUp(self):
        self.csv_file = "sample.csv"
        with open(self.csv_file, "w", newline='', encoding='utf-8') as f:
            f.write("id,name\n1,Alice\n2,Bob\n")

        self.json_file = "sample.json"
        with open(self.json_file, "w", encoding='utf-8') as f:
            json.dump([{"id": "1", "name": "Alice"}, {"id": "1", "name": "Alice"}], f)

    def tearDown(self):
        os.remove(self.csv_file)
        os.remove(self.json_file)

    def test_ingest_csv(self):
        data = ingest_data(self.csv_file)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["id"], "1")

    def test_clean_data(self):
        data = ingest_data(self.json_file)
        cleaned = clean_data(data)
        self.assertEqual(len(cleaned), 1)


if __name__ == '__main__':
    unittest.main()
