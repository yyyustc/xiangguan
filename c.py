# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:52:44 2018

@author: Administrator
"""


from pandas import Series
from statsmodels.graphics.tsaplots import plot_acf
from matplotlib import pyplot
def x3():
    series = Series.from_csv('seasonally_adjusted.csv', header=None)
    plot_acf(series)
    pyplot.show()
    return