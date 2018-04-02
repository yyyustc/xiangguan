# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:45:19 2018

@author: Administrator
"""
def x1():
# line plot of time series

    from pandas import Series
    
    from matplotlib import pyplot
    
    # load dataset
    
    series = Series.from_csv('monthly-car-sales-in-quebec-1960.csv', header=0)
    
    # display first few rows
    
    print(series.head(5))
    
    # line plot of dataset
    
    series.plot()
    
    pyplot.show()
    return









