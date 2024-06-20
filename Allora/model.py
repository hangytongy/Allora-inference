import yfinance as yf

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

from prophet.serialize import model_to_json, model_from_json
from prophet import Prophet


def get_inference(argument):

    def train_prophet_model(data):
        model = Prophet(
        changepoint_prior_scale=0.1,
        holidays_prior_scale=0,
        seasonality_prior_scale=5,            
        weekly_seasonality=True,
        yearly_seasonality=True,
        daily_seasonality=True)
    
        model.fit(data)
        return model

    def gen_forcast(model, period = 2):
        future = model.make_future_dataframe(periods = period)
        forcast = model.predict(future)
        return forcast

    today = date.today().strftime('%Y-%m-%d')

    if argument in ["SOL","ETH","BTC"]:
        ticker = argument+'-USD'
        try:
            df = yf.download(ticker, start = '2021-01-01',end = today)
            df =df.reset_index().drop(columns = ['Adj Close','Open','High','Low','Volume'])
            df_new = df.copy()
            df_new.rename(columns = {'Date' : 'ds', 'Close' : 'y'}, inplace = True)
            model = train_prophet_model(df_new)
            forcast = gen_forcast(model)
            return {"predicted price" : forcast['yhat'].iloc[-1]}
        except:
            return "error in prediction"
    else:
        return "false, argument not in list"


