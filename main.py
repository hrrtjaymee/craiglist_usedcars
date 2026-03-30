import pandas as pd
import numpy as np
from src.extract import get_data
from src.transform import clean_batch
import re

## INITIAL VIEW ON DATA ##
# from pathlib import Path
# ROOT = Path(__file__).resolve().parents[1]
# data = pd.read_csv(f'{ROOT}/used_cars_craiglist.csv')
# print(data.info())
# print(data.describe())
# [print(x) for x in data['label'].unique()]

# for x in data['label']:
    # match = re.search(r'\b(\d{4})\b', x)
    # print(match.group())

## all columsn are TYPE STR
## assume all columns have missing values
## [main href ] = posting link
## [swipe-wrap src] = image path
## [label] = posting title (could be year and car model
## [meta] = car mileage
## [result-posted-date] = how recent the posting was (in hrs based on when the data was retrieved)
## [location] = location (contains incorrect values)
## [priceinfo] = selling price (in US dollars)

def main():
    ##hore: add db connection function
    BATCHSIZE = 100
    data = get_data(BATCHSIZE)
    for batch, chunk in enumerate(data, start=1):
        print(f'PROCESSING BATCH NUMBER {batch} | READ {len(chunk)} ROWS')
        cleaned_batch = clean_batch(chunk)

        print(cleaned_batch)

main()