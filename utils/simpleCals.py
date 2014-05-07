# Third Party Imports
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
from pandas.io.data import DataReader
import pylab as P

def movingAverage(data, window_size = 20):
	MA = pd.rolling_mean(data, window_size)
	return MA

def plotMA(stock,  window_size = 20, txt = "Adj Close"):
	'''
	Function to plot the Moving Average with a defauly window size of 20.
	'''
	plt.plot(stock[txt], 'b-')	
	indexMA = range( window_size, stock[txt].size-window_size)
	print len(indexMA)
	MA = movingAverage2( stock[txt],  window_size)
	print len(MA)
	plt.plot(indexMA, MA[window_size:-window_size], 'rx-')
	plt.show()
	

def normalizedPrice(price):
	normalizedPrice = price / price[0]
	return normalizedPrice
		
def computeDailyReturn(nPrice):
    """
    @summary: Computes stepwise (usually daily) returns relative to 0, where
    0 implies no change in value.
    @return: the array is revised in place
    """
    nPrice = nPrice[:]
    daily_ret = (nPrice[1:] / nPrice[0:-1]) - 1
    return daily_ret
	
def return_sharpe_ratio( rets, risk_free = 0.00):
    """
    @summary Returns the daily Sharpe ratio of the returns.
    @param rets: 1d numpy array or fund list of daily returns (centered on 0)
    @param risk_free: risk free returns, default is 0%
    @return Annualized rate of return, not converted to percent
    """
    f_dev = np.std( rets, axis = 0)
    f_mean = np.mean( rets, axis = 0)
    
    f_sharpe = (f_mean *252 - risk_free) / ( f_dev * np.sqrt(252) )
    
    return f_sharpe


