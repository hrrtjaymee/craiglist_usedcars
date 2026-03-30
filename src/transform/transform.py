import pandas as pd
import numpy as np
import re
from datetime import datetime

#add data to database by batch (100 rows per batch)
##rename columns /
#clean data

#separate model year and car model in label column
MIN_YEAR = 1950
CURR_YEAR = datetime.today().year

CAR_MODELS = {'chevrolet', 'ford', 'honda', 'acura', 'gmc',
            'toyota', 'mercedes', 'subaru', 'nissan', 'chrysler',
            'hyundai', 'corvette', 'volkswagen', 'mazda', 'land rover',
            'audi', 'kia', 'dodge', 'tesla','bmw', 'jeep',
            'lexus', 'porsche', 'austin', 'chevy'}
#todo: clean titles so that the capitalization is uniform & chevy == chevrolet
def clean_batch(data: pd.DataFrame):
    clean_title(data)

    final_data = data[['year', 'make', 'model']]
    return final_data

def clean_title(data: pd.DataFrame):
    print('Cleaning label column')
    data['label'] = data['label'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x)) #removes symbols
    data['year_raw'] = data['label'].str.extract(r'\b(\d{4})\b') #takes 4 digit numbers 
    data['year_raw'] = pd.to_numeric(data['year_raw'], errors='coerce').astype('Int64') #turn values to float then int64
    data['year'] = data['year_raw'].where((data['year_raw'] >=  MIN_YEAR) & (data['year_raw'] <= CURR_YEAR)) #validating year

    pattern = '|'.join(CAR_MODELS)
    data['make'] = data['label'].str.extract(f'({pattern})', flags=re.IGNORECASE) #extracting make
    data['model'] = data['label'].str.replace(pattern, repl='', case=False, regex=True) #removing the make from the model
    data['model'] = data['label'].str.replace(r'\b(\d{4})\b', '', case=False, regex=True) #removing the year from the model



