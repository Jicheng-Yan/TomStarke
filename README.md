Daily Return and Moving Average Based Trading Strategy
=========

Daily return computation and Moving Average based trading strategy inspired by quantstart.com.

### Daily Return of a stock
The _dailyReturn.py_ calculates the daily return of an asset and plots a histogram of the daily return data. The stock data is downloaded from yahoo finance. 
Other than the python imports, some basic functions used in _dailyReturn.py_ can be found in _utils.simpleCals.py_.

### Moving average based strategy
This is mostly copied from quantstart.com.
_movingAverage.py_ starts with a portfolio of 100,000 in Jan, 1, 1990 and runs till Jan 1, 2012. It buys and sells 100 shares of Apple inc. (AAPL) everytime the 100 day moving average crosses the 400 day moving average.

The buy and sell signals are indicated in the magenta and black triangles respectively in the plots. The plots are otherwise self explanatory in nature.