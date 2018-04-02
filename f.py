# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 20:36:36 2018

@author: Administrator
"""

from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot
# load dataset
def x6():
    dataframe = read_csv('lags_12months_features.csv', header=0)
    # separate into input and output variables
    array = dataframe.values
    X = array[:,0:-1]
    y = array[:,-1]
    # perform feature selection
    rfe = RFE(RandomForestRegressor(n_estimators=500, random_state=1), 4)
    fit = rfe.fit(X, y)
    # report selected features
    print('Selected Features:')
    names = dataframe.columns.values[0:-1]
    for i in range(len(fit.support_)):
    	if fit.support_[i]:
    		print(names[i])
    # plot feature rank
    names = dataframe.columns.values[0:-1]
    ticks = [i for i in range(len(names))]
    pyplot.bar(ticks, fit.ranking_)
    pyplot.xticks(ticks, names)
    pyplot.show()
    return