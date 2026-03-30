from pathlib import Path

COLUMN_NAMES = ['posting_link', 'image_link', 'label', 'mileage', 'meta', 'location', 'price']
ROOT = Path(__file__).resolve().parents[1]
FILENAME = '/used_cars_craiglist.csv'