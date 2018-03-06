# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: DBSCAN.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/6 上午10:47

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/6 上午10:47
"""

"""
    密度聚类的思想：通过计算样本点的密度大小来实现一个簇/类别的形成，样本点密度越大，越容易形成一个类，从而形成聚类
    密度聚类算法可以克服基于距离的聚类算法只能发现凸型集合的缺点，其可根据密度的分布发现任意形状的聚类，且对噪声数据不敏感
    
    DBSCAN算法：有代表性的基于密度的聚类算法，它将簇定义为密度项链的样本点的最大集合，可在有噪声样本的样本集中发现任意形状的簇
        名词解释：
            对象：样本点
            对象的邻域：给定对象在半径内的区域
            核心对象：给定一个数目m，如果一个对象的邻域至少包含m个对象，则称该对象为核心对象
            直接密度可达：如果对象p是在对象q的邻域内，且对象q是一个核心对象，我们可以说从对象q出发，对象p是直接密度可达的
            密度可达：如果对象p是从对象q出发关于和m（含义同上）直接密度可达的；又有如果对象r是从对象p出发关于和m直接密度可达的，
                那么对象r是从对象q出发关于和m密度可达的
            密度相连：若存在一个对象o，使得对象p和q是从对象o关于和m密度可达的，那么对象p和q是关于和m密度相连的
            簇：最大的、密度相连对象的集合
            噪声：不包含在任何簇里面的对象
        算法流程：
            a. 如果一个样本点的 - 邻域包含多于m个对象，则创建一个p作为核心对象的新簇。
            b. 寻找核心对象的直接密度可达的对象，被合并为一个新的簇。
            c. 直到没有点可以更新簇时算法结束。
            注意：非核心对象是没有直接密度可达的对象的，它们一般构成了簇的边缘。每个簇可包含多个核心对象。
"""

from sklearn.datasets.samples_generator import make_moons
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.datasets.samples_generator import make_circles
import matplotlib.pyplot as plt
import time

# 月亮形展示
x, y_true = make_moons(n_samples=1000, noise=0.15)
plt.scatter(x[:, 0], x[:, 1], c=y_true)
plt.show()

# KMeans
start = time.time()
kmeans = KMeans(init='k-means++', n_clusters=2, random_state=8).fit(x)
end = time.time()
interval = end - start
plt.scatter(x[:, 0], x[:, 1], c=kmeans.labels_)
plt.title('time: %f' % interval)
plt.show()

# DBSCAN
start = time.time()
dbscan = DBSCAN(eps=.1, min_samples=6).fit(x)
end = time.time()
interval = end - start
plt.scatter(x[:, 0], x[:, 1], c=dbscan.labels_)
plt.title('time: %f' % interval)
plt.show()

# 圆形展示
x, y_true = make_circles(n_samples=1000, factor=0.45, noise=0.15)
plt.scatter(x[:, 0], x[:, 1], c=y_true)
plt.show()

# KMeans
start = time.time()
kmeans = KMeans(init='k-means++', n_clusters=2, random_state=8).fit(x)
end = time.time()
interval = end - start
plt.scatter(x[:, 0], x[:, 1], c=kmeans.labels_)
plt.title('time: %f' % interval)
plt.show()

# DBSCAN
start = time.time()
dbscan = DBSCAN(eps=.1, min_samples=6).fit(x)
end = time.time()
interval = end - start
plt.scatter(x[:, 0], x[:, 1], c=dbscan.labels_)
plt.title('time: %f' % interval)
plt.show()
