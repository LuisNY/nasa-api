from datetime import timedelta
import requests

class PhotoFetcher:

    photo_collection = {}

    def __init__(self, config):
        self.config = config

    def fetch_photos(self):
        day = self.config.start_date

        while day <= self.config.end_date:
            day_str = str(day)
            if not self._found_in_cache(day_str):
                self._get_photos(day_str)
                self._cache_photos(day_str)

            day += timedelta(days=1)

        return self.photo_collection

    def _cache_photos(self, day):
        f = open(f"{self.config.CACHE_PATH}/{day}", 'w')
        if day in self.photo_collection.keys():
            for photo_img in self.photo_collection[day]:
                f.write('%s\n' % photo_img)
        f.close()

    def _found_in_cache(self, day):
        try:
            file_name = f"{self.config.CACHE_PATH}/{day}"
            f = open(file_name)
            self.photo_collection[day] = []
            for line in f:
                self.photo_collection[day].append(line)

            f.close()
            return True

        except FileNotFoundError:
            # photos not found in cache
            return False

    def _get_photos(self, day):
        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{self.config.rover}/photos?earth_date={day}&camera={self.config.camera}&api_key={self.config.API_KEY}'
        response = requests.get(url)
        photos_array = response.json()['photos'][0:self.config.day_limit]
        self.photo_collection[day] = []

        for photo in photos_array:
            self.photo_collection[day].append(photo['img_src'])
