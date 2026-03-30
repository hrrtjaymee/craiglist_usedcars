import pandas as pd
from settings import COLUMN_NAMES, ROOT, FILENAME

def get_data(chunksize = 100):
    try:
        data = pd.read_csv(f'{ROOT}{FILENAME}', names=COLUMN_NAMES, header=None, chunksize=chunksize)
        print('Successfully retrieved data')
    except FileNotFoundError:
        print(f'Error: The file {FILENAME} was not found in path {ROOT}')
    except Exception as e:
        print(f'An unexpcted error occurred: {e}')

    return data
        

    

