import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
df = pd.read_csv('mydata.csv')
plt.xlabel('area')
plt.ylabel('prices')
plt.title("HOUSE PRICE PREDICTION")
plt.scatter(df.area,df.prices,color='red',marker='+')
area = df[['area']]
price = df.prices
price
reg = linear_model.LinearRegression()
reg.fit(area,price)
reg.predict(1499)
