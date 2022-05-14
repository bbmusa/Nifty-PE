# -*- coding: utf-8 -*-
"""
Created on Sat May 14 09:53:52 2022

@author: KaptanSab
"""

from datetime import date
from nsepy import get_index_pe_history, get_history


nifty_pe = get_index_pe_history(symbol="NIFTY",
                                start=date(2021,10,1),
                                end=date(2022,4,13))
nifty = get_history(symbol="NIFTY",
                    start=date(2021,10,1),
                    end=date(2022,4,13),
                    index=True)

nifty_pe.to_pickle("nifty_pe.pkl")
nifty.to_pickle("nity.pkl")
nifty['P/E'] = nifty_pe['P/E']
nifty['Shifted'] = nifty['Close'].shift(periods=-252)
nifty['ForwardReturns'] = (nifty['Shifted']-nifty['Close'])*100/nifty['Close']
nifty[['Close', 'Shifted', 'ForwardReturns','P/E']].head()
nifty[['ForwardReturns', 'P/E']].plot.scatter(x='P/E',y='ForwardReturns', figsize=(20,10), grid=True)
nifty['P/E'].plot(figsize=(20,10), grid=True)