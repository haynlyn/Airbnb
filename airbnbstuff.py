import os, pandas as pd, numpy as np, datetime, re
from pandas import Series, DataFrame

airbnbfiles = ['/mnt/c/users/daniel/downloads/airbnb_{}/{}.csv'.format(x, x) for x in ['listings', 'reviews', 'calendar']]

calendar = pd.read_csv(airbnbfiles[-1], header = 0)

### This next part is about preparing the calendar DataFrame for future manipulation. Do also for the listings DataFrame.

# column: dtype-original, dtype-desired

# listing_id: numpy.int64, int
# date: str, datetime.date
# available: str :: '$xxx.xx', float 
# price: str :: '$xxx.xx', float
# adjusted_price: str, float
# minimum_nights: numpy.float64,
# maximum_nights: numpy.float64,


# don't price_to_float1 = lambda price_with_dollar_sign: float(price_with_dollar_sign[1:])

def price_to_float2(price_with_dollar_sign_and_commas):
  try:
    numbers = re.compile(r'([\d.]+)')
    return float(''.join(numbers.findall(str(price_with_dollar_sign_and_commas)))) 
  except:
    return np.nan

def price_to_int(price_with_dollar_sign_and_commas):
  try:
    numbers = re.compile(r'([\d.]+)')
    return int(''.join(numbers.findall(str(price_with_dollar_sign_and_commas)))) 
  except:
    return np.nan


calendar['date'] = calendar['date'].apply(datetime.date.fromisoformat)
calendar['available'] = calendar['available'].map({'f': 0, 't': 1})
## Some of the prices and adjusted_prices are np.na, so drop them. There are about 10k that are np.na, but that's an insignificant fraction.
## Perhaps drop all of any listing_id such that they have any adjusted_/prices that are np.na.
calendar['price'] = calendar['price'].apply(price_to_float1)
calendar['adjusted_price'] = calendar['adjusted_price'].apply(price_to_float1)

def can_be_float(price):
  try:
    number = re.compile(r'([\d.]+)')
    float(''.join(numbers.findall(str(price)))) 
    return True
  except:
    return False

# This shows the listings based on most available.
calendar.groupby(by = 'listing_id').apply(lambda x: x['available'].sum()).sort_values(ascending = False)




listings = pd.read_csv(airbnbfiles[0], header = 0)





