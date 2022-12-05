import argparse
from datetime import date, timedelta, datetime

class Config:

    API_KEY = 'hpYHVJpQN3dXPGb8YKXxtFueBOX8PA9gfrf8Lco1'
    CACHE_PATH = './cached_photos'

    def __init__(self):
        self.start_date = date.today() - timedelta(days=9)
        self.end_date = date.today()
        self.camera = 'NAVCAM'
        self.rover = 'curiosity'
        self.days_lookback = 10
        self.day_limit = 3

    def parse(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--last-date', type=str)
        parser.add_argument('--camera', type=str)
        parser.add_argument('--rover', type=str)
        parser.add_argument('--day-limit', type=int)
        parser.add_argument('--days-lookback', type=int)

        args = parser.parse_args()

        if args.days_lookback is not None:
            self.days_lookback = args.days_lookback
        if args.last_date is not None:
            self.end_date = datetime.strptime(args.last_date, '%Y-%m-%d').date()
            self.start_date = self.end_date - timedelta(days=self.days_lookback-1)
        if args.camera is not None:
            self.camera = args.camera
        if args.rover is not None:
            self.rover = args.rover
        if args.day_limit is not None:
            self.day_limit = args.day_limit







