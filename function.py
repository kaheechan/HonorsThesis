
import pandas as pd
import sqlite3 as sq
from dataclasses import dataclass
from datetime import datetime
file_path = 'C:/Users/larai/OneDrive/Desktop/ARE 107/AMZN_Simple.xlsx'
df = pd.read_excel(file_path)

# SMA Indicator
def golden_cross_signal(self):
    SMA50= self.MainDF['SMA50']
    SMA200= self.MainDF['SMA200']
    GoldenCrossSignal= SMA50>SMA200
    return GoldenCrossSignal

def death_cross_signal(self):
    SMA50 = self.MainDF['SMA50']
    SMA200 = self.MainDF['SMA200']
    DeathCrossSignal = SMA50 < SMA200
    return DeathCrossSignal

#RSI Indicator
def RSI_indicator(self, period=14): #data needed for indicator
    close_data= self.close_data()
    #price differences between each day's closing price
    #and the previous day's closing price
    price_diff= close_data.diff(1)

    #calculate the capital gains and losses
    gains = price_diff.where(price_diff>0,0)
    losses= -price_diff.where(price_diff<0,0)

    #Calculate average gains and losses over 14 dats
    #(typical measure for this strategy)
    avg_gain= gains.rolling(window=14).mean()
    avg_loss= losses.rolling(window=14).mean()

    #Calculate relative strength (RS)
    rs= avg_gain/avg_loss

    #calculate RSI
    rsi=100- (100/(1+rs))
    return rs


def rsi_bollinger_strategy(self):
    #calculate rsi of stock
    rsi=self.rsi
    #calcuate the lower bollinger band based on 20-day SMA
    # and 2 times the 20 day SD
    sma20= self.sma20()
    std20=self.std_twenty()
    upper_bollinger= sma20 + 2 * std20
    lower_bollinger= sma20 - 2 * std20
    return lower_bollinger
    return upper_bollinger

#combined bollinger bands and RSI
def combined_strategy(self):
    rsi= self.rsi() #calculate rsi from a scale of 0 to 100
    upper_bollinger= self.upper_bollinger()
    lower_bollinger= self.lower_bollinger
    if rsi<= 30 and stock_price<= lower_bollinger:
        strategy= "Buy"
    elif rsi>=70 and strock_price<=upper_bollinger:
        strategy= "Sell"

#True Strength Index Indicator
def True_Strength_Index:

    if rsi <= 30:
        strategy = True
        else strategy = False
















