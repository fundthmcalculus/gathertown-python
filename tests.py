import json
import os
import unittest

from gatherhttp import get_map, get_map_v2


class TestGatherHttp(unittest.TestCase):
    def setUp(self) -> None:
        self.api_key: str = os.getenv('GATHER_API_KEY')
        self.space_id: str = os.getenv('GATHER_SPACE_ID')
        self.map_id: str = os.getenv('GATHER_MAP_ID')

    def test_get_map(self):
        map_data = get_map(self.api_key, self.space_id, self.map_id)
        self.assertTrue(map_data is not None)
        with open('map_data.json', 'w') as fid:
            fid.write(json.dumps(map_data, indent=2))

    def test_get_map_v2(self):
        map_data = get_map_v2(self.api_key, self.space_id, self.map_id)
        self.assertTrue(map_data is not None)
        with open('map_data_v2.json', 'w') as fid:
            fid.write(json.dumps(map_data, indent=2))


if __name__ == '__main__':
    unittest.main()
