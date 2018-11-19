import stock_analysis as sa
import matplotlib
from matplotlib.font_manager import FontProperties
import fix_yahoo_finance as yf
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import variation
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime


def col_switch(i):
    switcher = {
        "O": 'Open',
        "H": 'High',
        "L": 'Low',
        "C": 'Close',
        "A": 'Adj Close',
        "V": 'Volume'
    }
    return switcher.get(i, "Error")


while True:
    try:
        start_date = input("Please enter the start date as (YYYY-MM-DD):\n")
        datetime.strptime(start_date, "%Y-%m-%d")
        break
    except ValueError:
        print("You have to enter numbers")  # Catch int() exception
    except Illegal:
        print("illegal, let's try that again")

while True:
    try:
        end_date = input("Please enter the end date as (YYYY-MM-DD):\n")
        datetime.strptime(end_date, "%Y-%m-%d")
        break
    except ValueError:
        print("You have to enter numbers")  # Catch int() exception
    except Illegal:
        print("illegal, let's try that again")

while True:
    try:
        print("Please enter the col that you want to analysis(one at a time)")
        col_input = input(
            "O for Open Value, H for High,L for Low,C fot Close, A for Adj Close and V for Volume:\n")
        if col_switch(col_input) != "Error":
            col_to_analysis = col_switch(col_input)
            break
        else:
            raise ValueError
    except ValueError:
        print("invaild input")  # Catch int() exception

MAXNUMOFSTOCK=4
ticker = []
counter = 0
exist = False
while True:
    try:
        if counter != MAXNUMOFSTOCK:
            ticker_temp = []
            test_data = []
            print("Please enter the symbols for the stock(s) that you want to proceed(Max",MAXNUMOFSTOCK,")")
            ticker_temp = input("(When you finish, please enter 'End' to exit):\n")
            if ticker_temp in ticker:
                exist = True
                raise ValueError
            if ticker_temp != "End":
                test_data = yf.download(ticker_temp,"2018-01-09", "2018-01-11")
                # print(test_data)
                if len(test_data) > 0:
                    ticker.append(ticker_temp)
                    print('*****',ticker_temp,'added to the list.****')
                    counter += 1  
                else:
                    raise ValueError
            else:
                break  
        else:
            break       
    except ValueError:
        print('*******THE SYMBOL YOU ENTER DOES NOT ASSOCIATED TO ANY STOCK**********')
        print("Invaild ticker, try again:")  # Catch int() exception



print(ticker)
description = sa.descriptive(start_date, end_date, col_to_analysis,ticker)
description.read_data()

while True:
    try:
        action_input = input(
            "Enter 1 for descriptive info, Enter 2 for graph, enter 3 for both:\n")
        if int(action_input) == 1:
            description.print_descriptive()
            break
        if int(action_input) == 2:
            description.plot()
            break
        if int(action_input) == 3:
            description.print_descriptive()
            description.plot()
            break
        else:
            raise ValueError
    except ValueError:
        print("Invaild input, try again:")  # Catch int() exception
