import unittest
from data_pool.notion import NotionClient


class TestNotionClient(unittest.TestCase):
    def test_create_page_not_implemented(self):
        client = NotionClient(token="token", database_id="db")
        with self.assertRaises(NotImplementedError):
            client.create_page({"field": "value"})


if __name__ == '__main__':
    unittest.main()
