# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: sklearn_multi_linear_model.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/6 下午5:15

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/6 下午5:15
"""

from numpy.linalg import inv
from numpy import dot, transpose
from numpy.linalg import lstsq
from sklearn.linear_model import LinearRegression

X = [[1,1,1],[1,1,2],[1,2,1]]
y = [[6],[9],[8]]

print(dot(inv(dot(transpose(X), X)), dot(transpose(X), y)))
print(lstsq(X, y)[0])

model = LinearRegression()
model.fit(X, y)
x_pre = [[1, 3, 5]]
y_pre = model.predict(x_pre)
print(y_pre)
