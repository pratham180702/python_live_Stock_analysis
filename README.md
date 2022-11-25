# Stock analyser with live data

## PROJECT DESCRIPTION
This project analyse the stocks on live basis. It analyse the stocks considering the deepest analysing points which pro traders uses. The analyzation of the stocks is done here in two ways. We thought of giving the option to the user to decider whether they have to analyse the stock on daily basis or they want it for their intraday trading.
  1. For daily basis, we used the PIVOT POINT calculations.
  Pivots Points are price levels chartists can use to determine intraday support and resistance levels. Pivot Points use the previous days Open, High, and Low to         calculate   a Pivot Point for the current day. If the stock opens above the pivot point, it is predicted that there is 80% chance that the selected stock will show     the uptrend. And if the stock opens above the pivot point, it is predicted that there is 80% chance that the selected stock will show the lower downtrend.
  There are various kinds of Pivot Points, but for instance we considered the STANDARD PIVOT POINT, and WOODIE PIVOT POINT.
  
  2. For Intraday, we used previous minute candle closing percent analysis.
  Traders analyse the candles of the stocks thoroughly for their intraday session, one of the trend is to check the last minute closing change percent for taking the 
  next step for their intraday.
  This will show the changing percent, and if the stock crosses the decided changing percent, then the code will notify the user on user's whatsapp number.(default it     is selected as 0.0004%)

## DATASET LINKS:

### 1. For live data of stocks on daily basis for Pivot Points Analysis:
https://finnhub.io/docs/api/stock-candles
Finnhub provides its module which we need to install and has lot of functionalities to use the realtime stock market data for analysis.
#### About Finnhub
finnhub provides FREE realtime API for stocks, forex and cryptocurrency. With this API, one can access realtime market data from stock exchanges, 10 forex brokers, and 15+ crypto exchanges. They also provide institutional-grade alternative and fundamental data for global companies through our stock API. They make use of state-of-the-art machine learning algorithms to collect, clean, and standardize data across global markets. See why Finnhub is the leader in financial data APIs with this stock APIs comparision.

### 2. For live data of stocks on minutes basis for Intraday Analysis:
https://www.alphavantage.co/documentation/
#### About ALPHA VANTAGE
ALPHA VANTAGE provides its module which has lot of libraries and particularly we imported alpha_vantage.timeseries i.e Timeseries.
The main moto of using the Timeseries of Alpha vantage was to get the real time stocks data for intraday session. To get the data minute by minute, we preferred alpha vantage's timeseries library.

### 3. Stock names with their Symbols. (for the reference of the user)
https://dailypik.com/best-us-stocks/
refering the above site, we created a local excel sheet which we later converted into DataFrame and used in the program.
#### local excel sheet link:
https://github.com/pratham180702/python_live_Stock_analysis/blob/main/stock_list.xlsx

## contributed by 
PRATHAM KAKKAD,
JAYDEEP SHARMA
