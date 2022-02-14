import mplfinance as mpf
import pandas as pd
import requests
def crypto(start_time,base_currency,vs_currency,interval):
    url=f'https://dev-api.shrimpy.io/v1/exchanges/binance/candles'
    payload={
        'interval':interval,'baseTradingSymbol':base_currency,'quoteTradingSymbol':vs_currency,'startTime':start_time
    }
    response=requests.get(url,params=payload)
    data=response.json()
    open_p,close_p,high_p,low_p,time_p=[], [], [], [], []
    for candle in data:
        open_p.append(float(candle['open']))
        high_p.append(float(candle['high']))
        low_p.append(float(candle['low']))
        close_p.append(float(candle['close']))
        time_p.append(candle['time'])
    raw_data={

'Date': pd.DatetimeIndex(time_p),
'Open':open_p,
'High':high_p,
'Low':low_p,
'Close':close_p
}
    df=pd.DataFrame(raw_data).set_index('Date')
    print(df)
    mpf.plot(df,type='candle',style='charles',title='BTC',ylabel=f'Price in {vs_currency}')
    mpf.show()
    return df


crypto(start_time='2022-02-11',base_currency='BTC',vs_currency='EUR',interval='1h')   
