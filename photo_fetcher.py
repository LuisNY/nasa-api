from datetime import timedelta
import requests

class PhotoFetcher:

    photo_collection = {}

    def __init__(self, config, cache):
        self.config = config
        self.cache =  cache

    def fetch_photos(self):
        day = self.config.start_date

        while day <= self.config.end_date:

            day_str = str(day)

            in_cache, cached_photos = self.cache.load_from_cache(day_str)
            if in_cache:
                self.photo_collection[day_str] = cached_photos
            else:
                self._get_photos(day_str)
                self.cache.cache_photos(day_str, self.photo_collection[day_str])

            day += timedelta(days=1)

        return self.photo_collection

    def _get_photos(self, day):
        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{self.config.rover}/photos?earth_date={day}&camera={self.config.camera}&api_key={self.config.API_KEY}'
        response = requests.get(url)
        photos_array = response.json()['photos'][0:self.config.day_limit]
        self.photo_collection[day] = []

        for photo in photos_array:
            self.photo_collection[day].append(photo['img_src'])
