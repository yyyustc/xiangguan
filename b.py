# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:55:18 2018

@author: Administrator
"""

from pandas import Series

from matplotlib import pyplot

# load dataset
def x2():

    series = Series.from_csv('car-sales.csv', header=0)
    
    # seasonal difference
    
    differenced = series.diff(12)
    
    # trim off the first year of empty data
    
    differenced = differenced[12:]
    
    # save differenced dataset to file
    
    differenced.to_csv('seasonally_adjusted.csv')
    
    # plot differenced dataset
    
    differenced.plot()
    
    pyplot.show()
    return
