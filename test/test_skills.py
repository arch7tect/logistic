import asyncio
import importlib
import sys
import unittest
from pathlib import Path

import dotenv
from logistics_shipments_v2_impl_test import retrieve_list_of_shipments


class TestSkills(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        dotenv.load_dotenv()
        # sys.path.append(str(Path(__file__).parent.parent / "src"))
        importlib.import_module("_init_db")
        self.kwargs = {"client_id": "C0001"}

    def tearDown(self):
        pass

    async def test_retrieve_list_of_shipments(self):
        result = await retrieve_list_of_shipments(**self.kwargs)
        self.assertIsInstance(result, dict)
        self.assertTrue('result_data' in result)
        self.assertIsInstance(result['result_data'], list)
        self.assertEqual(len(result['result_data']), 3)


if __name__ == '__main__':
    unittest.main()
