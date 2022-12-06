import unittest
from photo_fetcher import PhotoFetcher
from config import Config
from cache import Cache
from datetime import datetime


class TestFetchFile(unittest.TestCase):
    def setUp(self):
        config = Config()
        cache = Cache(config)
        self.photo_fetcher = PhotoFetcher(config, cache)

    def test_get_photos(self):
        day = datetime(2020, 5, 17).date()
        self.photo_fetcher._get_photos(day)
        assert len(self.photo_fetcher.photo_collection) == 10


if __name__ == '__main__':
    unittest.main()

