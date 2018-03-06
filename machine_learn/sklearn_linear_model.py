# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: sklearn_linear_model.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/6 下午4:52

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/6 下午4:52
"""

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = [[1], [2], [3], [4], [5], [6]]
y = [[1], [2.1], [2.9], [4.2], [5.1], [5.9]]
model = LinearRegression()
model.fit(x, y)
predicted = model.predict([[13]])[0]
print(predicted)

# 画图
plt.figure()
plt.title('Linear_Regression')
plt.xlabel('X_label')
plt.ylabel('Y_label')
plt.grid(True)
plt.plot(x, y, 'r-')
plt.show()
