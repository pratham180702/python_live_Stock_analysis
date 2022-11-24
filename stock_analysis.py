import finnhub
import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries
import time
import pywhatkit
import plotly.graph_objs as go

finnhub_client = finnhub.Client(api_key="cdn6fb2ad3ibs2gsvl4gcdn6fb2ad3ibs2gsvl50")

# stock symbols with name
csv_file = pd.read_excel('stock_list.xlsx')
df_list = pd.DataFrame(csv_file)
# print(df_list.head(25)[df_list.columns[0:2]])
print(csv_file)

#enter the stock name you want to search
stock = input("Enter the Stock symbol : ")


choice1 = input("What you want to analyze : \n1. Daily pivot point.\n2. Intraday candle closing percent analysis. : ")

if(choice1 == '1'):
    currentDateTime = datetime.now()
    timestamp = int(datetime.timestamp(currentDateTime))

    basic = finnhub_client.stock_candles(stock, 'D', (timestamp-13286000), timestamp) 
    df = pd.DataFrame(basic)
    df.rename(columns = {'c':'closing', 'h':'High', 'l':'low'}, inplace = True)
    pd.set_option('display.max_rows', None)
    # df[['closing', 'High', 'low']]

    choice = (input("What you want to calculate : \n 1. Standard Pivot point.\n2.   Woodie Pivot point.\n(select 1/2) :"))

    if(choice == '1'):
        # pivot point
        df['Pivot point']= (df['closing']+df['High']+df['low'])/3
        # R1=(P×2)−Low
        df['Resistance 1'] = (df['Pivot point'] * 2) - df['low']
        # R2=P+(High−Low)
        df['Resistance 2'] = df['Pivot point'] + (df['High']- df['low'])
        # R3= High+2(PP - low)
        df['Resistance 3'] = df['High'] + 2* (df['Pivot point']- df['low'])
        # S1=(P×2)−High
        df['Support 1']= (df['Pivot point']*2)- df['High']
        # S2=P−(High−Low)
        df['Support 2'] = df['Pivot point']- (df['High']- df['low'])
        # S3=low−2(High−PP)
        df['Support 3'] = df['low']- 2*(df['High']- df['Pivot point'])

        print(df[['closing', 'High', 'low', 'Pivot point','Resistance 1', 'Resistance 2',   'Resistance 3',
                  'Support 1', 'Support 2','Support 3']])

        plt.plot(df.index, df['Pivot point'],"-b", label = 'Pivot point') 
        plt.legend(loc="upper left")
        current_date = str(datetime.fromtimestamp(timestamp))
        last_date = str(datetime.fromtimestamp(timestamp-(13286000)))
        plt.xlabel("From "+str(last_date[0:10])+" TO "+str(current_date[0:10])+ "---->")
        plt.ylabel("Price in USD")

        plt.title("For upcoming intraday Pivot Point = "+str("%.2f" % df['Pivot point'].    iloc[-1]))

        plt.show()

        plt.plot(df.index, df['closing'],"black",label = 'Closing')
        plt.plot(df.index, df['High'],"g", label='High')
        plt.plot(df.index, df['low'],"r",label = 'low')
        plt.legend(loc="upper left")
        plt.show()



        plt.axhline(y=df['Pivot point'].iloc[-1], color='black', linestyle='-')
        plt.axhline(y=df['Resistance 1'].iloc[-1], color='g', linestyle='--')
        plt.axhline(y=df['Resistance 2'].iloc[-1], color='g', linestyle='--')
        plt.axhline(y=df['Resistance 3'].iloc[-1], color='g', linestyle='--')
        plt.axhline(y=df['Support 1'].iloc[-1], color='r', linestyle='--')
        plt.axhline(y=df['Support 2'].iloc[-1], color='r', linestyle='--')
        plt.axhline(y=df['Support 3'].iloc[-1], color='r', linestyle='--')
        plt.show()

    else:
        # 2. Woodie pivot point
        df['Woodie PP']= ((2*df['closing'])+df['High']+df['low'])/4
        # R1: (2 x pivot) – previous low
        df['WR1']= (2*df['Woodie PP'])- df['low']
        # R2: Pivot + high - low
        df['WR2'] = df['Woodie PP'] + df['High'] - df['low']
        # R3: High + 2 x (Pivot – low)
        df['WR3'] = df['High'] + (2*(df['Woodie PP'] - df['low']))
        # S1: (2 x pivot) – Previous high
        df['WS1'] = (2* df['Woodie PP']) - df['High']
        # S2: Current pivot – (R1 – S1)
        df['WS2'] = df['Woodie PP'] - (df['WR1']- df['WS1'])
        # S3: Low – 2 x (High – pivot)
        df['WS3'] = df['low'] - (2*(df['High']- df['Woodie PP']))


        print(df[['closing', 'High', 'low', 'Woodie PP','WR1', 'WR2','WR3',
                  'WS1', 'WS2','WS3']])

        plt.plot(df.index, df['Woodie PP'],"-b", label = 'Woodie PIVOT POINT') 
        plt.legend(loc="upper left")
        current_date = str(datetime.fromtimestamp(timestamp))
        last_date = str(datetime.fromtimestamp(timestamp-(13286000)))
        plt.xlabel("From "+str(last_date[0:10])+" TO "+str(current_date[0:10])+ "---->")
        plt.ylabel("Price in USD")

        plt.title("For upcoming intraday Pivot Point = "+str("%.2f" % df['Woodie PP'].  iloc[-1]))

        plt.show()

        plt.plot(df.index, df['closing'],"black",label = 'Closing')
        plt.plot(df.index, df['High'],"g", label='High')
        plt.plot(df.index, df['low'],"r",label = 'low')
        plt.legend(loc="upper left")
        plt.show()



        plt.axhline(y=df['Woodie PP'].iloc[-1], color='black', linestyle='-')
        plt.axhline(y=df['WR1'].iloc[-1], color='g', linestyle='--')
        plt.axhline(y=df['WR2'].iloc[-1], color='g', linestyle='--')
        plt.axhline(y=df['WR3'].iloc[-1], color='g', linestyle='--')
        plt.axhline(y=df['WS1'].iloc[-1], color='r', linestyle='--')
        plt.axhline(y=df['WS2'].iloc[-1], color='r', linestyle='--')
        plt.axhline(y=df['WS3'].iloc[-1], color='r', linestyle='--')
        plt.show()



#intraday change percent alert analysis 
else:
    api_key = 'RNZPXZ6Q9FEFMEHM'

    ts = TimeSeries(key=api_key, output_format='pandas')
    # stock = input("Enter the symbol of the stock : ")

    phone = input("Enter the phone number in the form +91xxxxxxxxxx : ")
    data, meta_data = ts.get_intraday(symbol=stock, interval = '1min', outputsize =     'full')
    df_test = pd.DataFrame(data)
    df = df_test.head(390)
    print(df.head(5))

    # candle figure of day
    fig=go.Figure()

    fig.add_trace(go.Candlestick(x=df.index,
                    open=df['1. open'],
                    high=df['2. high'],
                    low=df['3. low'],
                    close=df['4. close'], name = 'market data'))

    fig.update_layout(
        title= str(stock)+' Live Share Price:',
        yaxis_title='Stock Price (USD per Shares)')               

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=24, label="1D", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.show()
    # change percent analysis
    close_data = data['4. close']
    percentage_change = close_data.pct_change()

    print(percentage_change)

    last_change = percentage_change[-1]

    #for current date and time
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    hour = int(current_time[0:2])

    min = int(current_time[3:5])

    # pywhatkit.sendwhatmsg('+919512817811', 'autogenerated text',hour, min+1)

    if abs(last_change) > 0.0004:
        print(stock+" Alert:" + str(last_change)[0:10])
        pywhatkit.sendwhatmsg(phone, stock+" Alert: last minute closing of your stock has crossed your stop loss closing limit by the change percent of : " + str(last_change)[0:10] + "%"+"\n -regards, PK & Company",hour,min+1)

    else:
        print("Stock still above stock loss percent")
