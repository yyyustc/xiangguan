# -*- coding: utf-8 -*-

from pandas import Series
from pandas import DataFrame
# load dataset
def x4():
    series = Series.from_csv('seasonally_adjusted.csv', header=None)
    # reframe as supervised learning
    dataframe = DataFrame()
    for i in range(12,0,-1):
        dataframe['t-'+str(i)] = series.shift(i)
        dataframe['t'] = series.values
    print(dataframe.head(13))
    dataframe = dataframe[13:]
    # save to new file
    dataframe.to_csv('lags_12months_features.csv', index=False)
    return