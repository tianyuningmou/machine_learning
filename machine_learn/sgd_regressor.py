# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: sgd_regressor.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/7 下午3:37

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/7 下午3:37
"""

import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

plt.figure()
plt.title('single variable')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

X_scaler = StandardScaler()
y_scaler = StandardScaler()
X = [[50], [100], [150], [200], [250], [300]]
y = [[150], [200], [250], [280], [310], [330]]
X = X_scaler.fit_transform(X)
y = y_scaler.fit_transform(y)
X_test = [[40], [400]]
X_test = X_scaler.transform(X_test)
plt.plot(X, y, 'k.')

model = SGDRegressor()
model.fit(X, y.ravel())
y_result = model.predict(X_test)
plt.plot(X_test, y_result, 'g-')

plt.show()
