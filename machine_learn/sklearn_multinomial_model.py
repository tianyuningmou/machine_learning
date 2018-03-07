# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: sklearn_multinomial_model.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/7 上午11:59

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/7 上午11:59
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

plt.figure()
plt.title('single variable')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([30, 400, 100, 400])
plt.grid(True)

X = [[50], [100], [150], [200], [250], [300]]
y = [[150], [200], [250], [280], [310], [330]]
X_test = [[250], [300]]
y_test = [[310], [330]]
plt.plot(X, y, 'k.')

# 线性回归
model = LinearRegression()
model.fit(X, y)
x2 = [[30], [400]]
y2 = model.predict(x2)
plt.plot(x2, y2, 'g-')

# 多项式回归
xx = np.linspace(30, 400, 100)
# 实例化一个二次多项式特征实例
quadratic_featurizer = PolynomialFeatures(degree=2)
# 用二次多项式对样本X值做变换
X_train_quadratic = quadratic_featurizer.fit_transform(X)
# 把训练好的X值得多项式特征实例应用到一系列点上，形成矩阵
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))
# 创建一个线性回归实例
regressor_quadratic = LinearRegression()
# 以多项式变换后的x值为输入，带入线性回归模型做训练
regressor_quadratic.fit(X_train_quadratic, y)
# 用训练好的模型作图
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), 'r-')

# 三次回归
cubic_featurizer = PolynomialFeatures(degree=3)
X_train_cubic = cubic_featurizer.fit_transform(X)
regressor_cubic = LinearRegression()
regressor_cubic.fit(X_train_cubic, y)
xx_cubic = cubic_featurizer.transform(xx.reshape(xx.shape[0], 1))
plt.plot(xx, regressor_cubic.predict(xx_cubic))

print('一元线性回归', model.score(X_test, y_test))
X_test_quadratic = quadratic_featurizer.transform(X_test)
print('二 次 回 归', regressor_quadratic.score(X_test_quadratic, y_test))
X_test_cubic = cubic_featurizer.transform(X_test)
print('三 次 回 归', regressor_cubic.score(X_test_cubic, y_test))

plt.show()
