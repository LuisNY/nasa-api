from config import Config
from cache import Cache
from photo_fetcher import PhotoFetcher

def start_application():

    config = Config()
    config.parse()

    cache = Cache(config)
    photo_fetcher = PhotoFetcher(config, cache)
    photo_collection = photo_fetcher.fetch_photos()

    print(photo_collection)

if __name__ == '__main__':
    start_application()
