# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 20:35:07 2018

@author: Administrator
"""
from pandas import read_csv
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot
# load data
def x5():
    dataframe = read_csv('lags_12months_features.csv', header=0)
    array = dataframe.values
    # split into input and output
    X = array[:,0:-1]
    y = array[:,-1]
    # fit random forest model
    model = RandomForestRegressor(n_estimators=500, random_state=1)
    model.fit(X, y)
    # show importance scores
    print(model.feature_importances_)
    # plot importance scores
    names = dataframe.columns.values[0:-1]
    ticks = [i for i in range(len(names))]
    pyplot.bar(ticks, model.feature_importances_)
    pyplot.xticks(ticks, names)
    pyplot.show()
    return