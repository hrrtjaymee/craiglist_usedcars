import pandas as pd
from pathlib import Path

'''
COLUMN ORDER:
posting_link
image_link
label
mileage
meta
location
price
'''

ROOT = Path(__file__).resolve().parents[3]
COLUMNS = ['posting_link', 'image_link', 'label', 'mileage', 'meta', 'location', 'price']

def get_batch():
    SKIPPED = 0
    BATCH = 0
    while True:
        SKIPPED += 100
        BATCH += 1
        try:
            data = pd.read_csv(f'{ROOT}/used_cars_craiglist.csv', skiprows=SKIPPED, nrows=100, names=COLUMNS, header=0)
            print(f'BATCH NUMBER: {BATCH}')
        except pd.errors.EmptyDataError:
            print('Insufficient data rows in csv')
            break
    
    return data



