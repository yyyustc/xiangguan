# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:44:57 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import random
def cov():
    persontype=np.dtype({'names':['name','height','weight'],'formats':['S32','f','f']},align=True)#先创建一个人物类型
    a = np.array([("Huang",175,70),("Hao",170,60),("Li",180,75)],dtype=persontype)
    data = np.array([a["height"],a["weight"]])
    data_cov = np.cov(data)#协方差矩阵
    data_corr = np.corrcoef(data)#相关系数矩阵
    return