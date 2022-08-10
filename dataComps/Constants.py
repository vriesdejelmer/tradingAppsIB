#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:52:13 2019

@author: vriesdejelmer
"""

class Constants:

    SYMBOL_CHANGE = 0
    SYMBOL_SUBMIT = 1
    SYMBOL_SUBMIT2 = 2

    SYMBOL_SEARCH_REQID = 2
    STK_PRICE_REQID = 3
    OPTION_CONTRACT_REQID = 4
    PNL_REQID = 5
    ACCOUNT_SUMMARY_REQID = 6
    BASE_OPTION_STRIKE_REQID = 100000
    BASE_OPTION_EXP_REQID = 200000
    BASE_HIST_MIN_MAX_REQID = 300000
    BASE_HIST_DATA_REQID = 400000
    BASE_HIST_BARS_REQID = 500000
    BASE_MKT_STOCK_REQID = 600000
    BASE_PNL_REQID = 700000
    REQID_STEP = 100000
    
    
    LOCAL_ADDRESS = "127.0.0.1"

    TRADING_SOCKET = 7496
    PAPER_SOCKET = 7497

    CALL_TYPE = "C"
    PUT_TYPE = "P"

    OPTION_DATA_EXP = "Expiration Type"
    OPTION_DATA_STRIKE = "Strike Type"

    POSITIONS_RETRIEVED = "Positions retrieved"
    OPTION_INFO_LOADED = "Options info loaded"
    OPTION_PRICE_UPDATE = "Option Price Updated"
    UNDERLYING_PRICE_UPDATE = "Underlying Price Updated"
    CONTRACT_DETAILS_RETRIEVED = "Contract details retrieved"
    CONTRACT_DETAILS_FINISHED = "Contract details finished"
    CONNECTION_OPEN = "Connection open"
    CONNECTION_CLOSED = "Connection closed"
    CONNECTION_STATUS_CHANGED = "Connection Status Changed"
    HISTORICAL_MIN_MAX_FETCH_COMPLETE = "Historical MinMax Fetch Complete"
    HISTORICAL_DATA_FETCH_COMPLETE = "Historical Data Fetch Complete"
    PRICE_COLLECTION_COMPLETE = "Prices Fetched"
    LIST_SELECTION_UPDATE = "List Selection Updated"
    PNL_RETRIEVED = "PNL Updated"
    IND_PNL_COMPLETED = "Individual PnLs retrieved"

    VOLATILE_LIST = ["AAL", "AFRM", "AMC", "AMD" ,"BABA","BMBL", "BROS", "BYND", "CCL", "CGC", "COIN", "DASH", "DKNG", "DOCS","DOCU", "DPRO", "EVLV", "GME", "HOOD", "INTC", "IOT", "KSS", "LAC", "LCID", "MARA", "MU", "NCLH","NIO","NKLA","PLTR", "PSFE", "PTON", "PYPL", "RBLX", "RCL", "RIOT","RIVN", "ROKU", "SHOP", "SNAP", "SNOW", "SOFI", "SQ", "TDOC","TSLA", "TLRY", "TWLO", "TWTR", "U", "UAL", "UPST","WISH"]

# importing enum for enumerations
import enum
    
# creating enumerations using class
class OrderType(enum.Enum):
    single = "Single Option"
    butterfly = "Butterfly"
    vertical_spread = "Vertical Spread"
    bw_butterfly = "BW Butterfly"
 

 # creating enumerations using class
class TradingPriority(enum.Enum):
    daily = "Daily"
    swing = "Swing"
    long_term = "Long Term"