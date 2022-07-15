from IIFLapis import IIFLClient
from django.http import JsonResponse
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import datetime as dt
from scipy.interpolate import make_interp_spline
import numpy as np
from time import time, sleep
import plotly.graph_objs as go
from plotly.offline import plot

client = IIFLClient(client_code="19370829", passwd="Blaze2489", dob="19890402", email_id="anvesh.raja24@gmail.com",
                        contact_number="9491558535")
client.client_login()  # For Customer Login
# client.partner_login() #For Partner Login

def get_data_static():
    print('calling static')

    req_list_ = [{"Exch": "N", "ExchType": "C", "ScripCode": "3045"}]
    client.jwt_validation("19370829")

    data = client.historical_candles(exch='n', exchType='c', scripcode='3045', interval='5m', fromdate='2022-07-04',
                                     todate='2022-07-04', client_id="19370829")
    key, val = data.popitem()
    candle_list = val.get('candles')
    new_df = pd.DataFrame(candle_list, columns=['date', 'open', 'high', 'low', 'close', 'vol.'])

    # new_df['date'] = pd.to_datetime(new_df['date'])
    
    return plot(
        {
            'data': [
                # go.Candlestick(
                #     x=new_df['date'], 
                #     open=new_df['open'], 
                #     high=new_df['high'],
                #     low=new_df['low'],
                #     close=new_df['close'],
                # ),
                go.Scatter(
                    x=new_df['date'],
                    y=new_df['close'].values,
                    text=new_df['close'],
                    mode='none',
                    fill='tozeroy')
            ],
            'layout': go.Layout(
                title='SBI',
                margin={'l': 40, 'b': 40, 't': 40, 'r': 0},
                hovermode='closest',
                xaxis_rangeslider_visible=True
            )
        },
        output_type='div')
                
                 
                                
                    
                    
                    
      

def get_live_data():
    req_list_ = [{"Exch": "N", "ExchType": "C", "ScripCode": "3045"}]
    client.jwt_validation("19370829")
    full_data = []
    i = 0
    while i < 100:
        data = client.fetch_market_feed(req_list=req_list_, count=2, client_id="19370829")
        full_data.append(data)
    return JsonResponse(full_data)

#while True:
    #sleep(1 - time() % 1)
# def get_data(stock_check:dict):
#     print('calling dynamic')
#     client = IIFLClient(client_code="19370829", passwd="Blaze2489", dob="19890402", email_id="anvesh.raja24@gmail.com",
#                         contact_number="9491558535")
#     client.client_login()  # For Customer Login
#     # client.partner_login() # For Partner Login
#     start_date = stock_check.get('start_date')
#     end_date = stock_check.get('end_date')
#     stock_code = stock_check.get('stock_code')
#     exch_type = stock_check.get('exch_type', "C")
#     exch = stock_check.get('exch', "N")
#     interval = stock_check.get('interval', "1m")
#     print("48", stock_check, "dict")
#     print(exch)


#     req_list_ = [{"Exch": 'n', "ExchType": 'c', "ScripCode": 3045}]
#     # live market data
#     # client.fetch_market_feed(req_list=req_list_, count=2, client_id="19370829")

#     client.jwt_validation("19370829")

#     #client.jwt_validation("19370829")
#     #historical data
#     print(exch_type)
#     data = client.historical_candles(exch=exch, exchType=exch_type, scripcode=stock_code, interval=interval, fromdate=start_date,
#                                     todate=end_date, client_id="19370829")

#     df = pd.DataFrame.from_dict(data)

#     key, val = data.popitem()

#     candle_list = val.get('candles')
#     new_df = pd.DataFrame(candle_list, columns=['date', 'open', 'high', 'low', 'close', 'vol.'])

#     # new_df['date'] = pd.to_datetime(new_df['date'])

#     return new_df


def plot_graph(new_df):
    start_date = pd.to_datetime('2022-07-04T09:15:00')
    end_date = pd.to_datetime('2022-07-04T15:25:00')
    x_axis = new_df['date']
    y_axis = new_df['close']
    spline = make_interp_spline(x_axis, y_axis)
    x_ = np.linspace(start_date.value, end_date.value, 60)
    x_ = pd.to_datetime(x_)
    y_ = spline(x_)
    f = plt.figure()
    f.set_figwidth(50)
    f.set_figheight(10)
    plt.plot(x_, y_)
    plt.xlabel('date')
    plt.ylabel('close')
    plt.show()
    return 
# In[96]:


# df1=pd.read_csv('hist_data.csv',delimiter=",")
# print(df1)


# In[99]:


# python_candlestick_chart.py

# plt.style.use('ggplot')

# Extracting Data for plotting
# data = new_df
# ohlc = data.loc[:, ['date', 'open', 'high', 'low', 'close']]
# ohlc['date'] =pd.to_datetime(ohlc['date'])
# ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num)
# print(ohlc['date'], type(ohlc['date']))
#
# ohlc = ohlc.astype(float)
# print(ohlc.values)
# # Creating Subplots
# fig, ax = plt.subplots()
# candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)
#
# # Setting labels & titles
# ax.set_xlabel('Date')
# ax.set_ylabel('Price')
# fig.suptitle('Daily Candlestick Chart of NIFTY50')
#
# # Formatting Date
# date_format = mpl_dates.DateFormatter('%d-%m-%Y')
# ax.xaxis.set_major_formatter(date_format)
# fig.autofmt_xdate()
#
# fig.tight_layout()
#
# plt.show()
