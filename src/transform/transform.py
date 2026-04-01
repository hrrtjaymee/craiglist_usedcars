import pandas as pd
import numpy as np
import re
from datetime import datetime

#add data to database by batch (100 rows per batch)
##rename columns 
#clean data

#separate model year and car model in label column
MIN_YEAR = 1950
CURR_YEAR = datetime.today().year

CAR_MODELS = {'chevrolet', 'ford', 'honda', 'acura', 'gmc',
            'toyota', 'mercedes', 'subaru', 'nissan', 'chrysler',
            'hyundai', 'corvette', 'volkswagen', 'mazda', 'land rover',
            'audi', 'kia', 'dodge', 'tesla','bmw', 'jeep',
            'lexus', 'porsche', 'austin', 'chevy', 'cadillac'}

def clean_batch(data: pd.DataFrame):
    data.drop_duplicates(inplace=True)
    clean_title(data)
    clean_mileage(data)

    final_data = data
    return final_data

def clean_title(data: pd.DataFrame):
    print('Cleaning label column')
    data['label'] = data['label'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x)) #removes symbols
    data['year_raw'] = data['label'].str.extract(r'\b(\d{4})\b') #takes 4 digit numbers 
    data['year_raw'] = pd.to_numeric(data['year_raw'], errors='coerce').astype('Int64') #turn values to float then int64
    data['year'] = data['year_raw'].where((data['year_raw'] >=  MIN_YEAR) & (data['year_raw'] <= CURR_YEAR)) #validating year

    pattern = '|'.join(CAR_MODELS)
    data['make'] = data['label'].str.extract(f'({pattern})', flags=re.IGNORECASE) #extracting make
    data['make'] = data['make'].str.replace('chevy', repl='Chevrolet', case=False)
    data['make'] = data['make'].str.upper()

    data['model'] = data['label'].str.replace(pattern, repl='', case=False, regex=True) #removing the make from the model
    data['model'] = data['label'].str.replace(r'\b(\d{4})\b', '', case=False, regex=True) #removing the year from the model

    data['needs_reviewing'] = (data['make'].isna()) | (data['year'].isna())

    data.drop(['year_raw', 'label'], axis=1, inplace = True)

def clean_mileage(data: pd.DataFrame):
    data['mileage'] = data['mileage'].str.extract(r'([\d]+k)', flags=re.IGNORECASE) ##removes comma and ml, returns num(k)

    data['mileage'] = data['mileage'].apply(normalize_values)
    
def normalize_values(mileage: str):
    if pd.isna(mileage):
        return None
    if 'k' in mileage:
        mileage = mileage.replace('k', '')
        mileage = int(mileage) * 1000
        return mileage
    return int(mileage)

