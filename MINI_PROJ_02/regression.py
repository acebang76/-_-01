# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:15:30 2021

@author: chban

선형회귀
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

dataset = pd.read_csv('innocar_dev_test.csv').to_numpy()

plt.scatter(dataset[:,0],dataset[:,1]) #데이터위치의 산포도 출력
plt.title("Linear Regression")
plt.xlabel("date")
plt.ylabel("battery volt")
plt.axis([0, 20000, 12.5, 15])

x = dataset[:,0].reshape(-1,1) #입력
y = dataset[:,1].reshape(-1,1) #출력

model = LinearRegression()
model.fit(x,y)  #모델학습

y_pred = model.predict(x)   #예측값 계산
plt.plot(x, y_pred, color='r')
plt.show()







