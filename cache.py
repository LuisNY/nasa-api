import os


class Cache(object):

    size = 0

    def __init__(self, config):
        self.config = config
        self.compute_size()

    def compute_size(self):
        for path in os.listdir(self.config.CACHE_PATH):
            if os.path.isfile(os.path.join(self.config.CACHE_PATH, path)):
                self.size += 1

    def cache_photos(self, day, photos):
        # check that cache is not full - if it is full empty cache
        if self.size >= self.config.CACHE_CAPACITY:
            for f in os.listdir(self.config.CACHE_PATH):
                os.remove(os.path.join(self.config.CACHE_PATH, f))
            self.size = 0

        f = open(f"{self.config.CACHE_PATH}/{day}", 'w')
        for photo in photos:
            f.write('%s\n' % photo)
        f.close()

        self.size += 1

    def load_from_cache(self, day):
        try:
            file_name = f"{self.config.CACHE_PATH}/{day}"
            f = open(file_name)
            array = []
            for line in f:
                array.append(line)
            f.close()
            return True, array
        except FileNotFoundError:
            return False, []
