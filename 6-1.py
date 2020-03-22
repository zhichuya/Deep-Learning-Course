# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:02:10 2020

@author: tianrenmi
"""
import numpy as np
import matplotlib.pyplot as plt
A = np.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
P = np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(6,6))
plt.scatter(A, P,s=20,c='r')
plt.xlabel("面积（平方米）",fontsize=14)
plt.ylabel("价格（万元）",fontsize=14)
plt.suptitle("商品房销售记录", fontsize=16,c='b')
plt.show()