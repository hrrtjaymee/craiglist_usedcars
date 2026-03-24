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
FILENAME = '/used_cars_craiglist.csv'
COLUMNS = ['posting_link', 'image_link', 'label', 'mileage', 'meta', 'location', 'price']

def get_data(chunksize = 100):
    try:
        data = pd.read_csv(f'{ROOT}{FILENAME}', names=COLUMNS, header=None, chunksize=chunksize)
    except FileNotFoundError:
        print(f'Error: The file {FILENAME} was not found in path {ROOT}')
    except Exception as e:
        print(f'An unexpcted error occurred: {e}')

    return data
        

    

