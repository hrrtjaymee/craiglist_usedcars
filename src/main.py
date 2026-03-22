import pandas as pd
import numpy as np
import os

## INITIAL VIEW ON DATA ##
path = os.getcwd()
data = pd.read_csv(f'{path}/../used_cars_craiglist.csv', nrows = 100)
# print(data.info())
# print(data.describe())
[print(x) for x in data['priceinfo'][2:76]]

## all columsn are TYPE STR
## assume all columns have missing values
## [main href ] = posting link
## [swipe-wrap src] = image path
## [label] = posting title (could be year and car model
## [meta] = car mileage
## [result-posted-date] = how recent the posting was (in hrs based on when the data was retrieved)
## [location] = location (contains incorrect values)
## [priceinfo] = selling price (in US dollars)

