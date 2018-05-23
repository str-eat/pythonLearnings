import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

data = pd.read_csv('kc_house_data.csv')

data.info()
data.describe()
data.head()
data.tail()

data['date'] = pd.to_datetime(data['date'])

plt.hist(data['price'])
plt.hist(np.log(data['price']))

data['bedrooms'].unique()
data['bedrooms'].nunique()
data[data['bedrooms'] == 0]

plt.scatter(data['sqft_living'], data['price'])

# Use .corr() to see which variables hav ea strong relationship
# Predictors/predicting
# test, train, split
# Fit
# Predict
# Calculate error
data.corr()

dataCopy = data.copy()

data['Year'] = data['date'].apply(lambda x: x.year)

#data['Recession'] = data['Year'].apply(lambda x: 1 if x == 2014 else 0)

print(data[data['Recession'] == 1])

predict_house_price = stats.linregress(data['sqft_living'], data['price'])
print(predict_house_price)

data['renovated'] = data['yr_renovated'].apply(lambda x: 1 if x > 0 else 0)
print(data['renovated'])

def predict(x):
    return predict_house_price.slope * x + predict_house_price.intercept

predict(4000)
predict(750)

