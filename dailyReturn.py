# Third Party Imports
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
from pandas.io.data import DataReader
import pylab as P


# my utils imports
import utils.simpleCals as sc



def main():
	''' Main Function'''
	# Start and End date of the charts
	dt_start = dt.datetime(2011, 1, 1)
	dt_end = dt.datetime(2012, 12, 31)
	
	#goog = pd.io.data.get_data_yahoo("GOOG",  dt_start, dt_end) # not working
	SPY = DataReader("SPY",  "yahoo", dt_start, dt_end)
	#YHOO = DataReader("YHOO",  "yahoo", dt_start, dt_end)
	
	# normalize prices
	nPrice = sc.normalizedPrice(SPY['Adj Close'].values)
	
	#daily return
	daily_ret = sc.computeDailyReturn(nPrice)
	plt.subplot(1,2,1)
	plt.plot(daily_ret*100, 'b-')
	plt.ylabel('Daily return (%)')
	plt.legend(['SPY-Daily Return based on Adjuested close'])
	
	#daily return histogram
	plt.subplot(1,2,2)
	n, bins, patches = plt.hist(daily_ret, 100, normed=1, facecolor='green', alpha=0.5)
	mean = np.mean(daily_ret)
	sigma = np.std(daily_ret)
	y = P.normpdf( bins, mean, sigma)
	plt.plot(bins, y, 'k--', linewidth=1.5)

	plt.ylabel('Probability')
	plt.legend(['normal distribution approximation','SPY-hostogram of daily return'])
	
	plt.show()
	
	


if __name__ == '__main__':
    main()
