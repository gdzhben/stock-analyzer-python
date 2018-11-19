import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use('ggplot')

#validate the date

#validate the symbol

company_name = input ('please enter the company\'s symbol: ')

startdate_entry = input('please choose your start date (YYYY,MM,DD): ').split(',')
enddate_entry = input('please choose your end date (YYYY,MM,DD): ').split(',')
start = dt.datetime(int(startdate_entry[0]),int(startdate_entry[1]),int(startdate_entry[2]))
end = dt.datetime(int(enddate_entry[0]),int(enddate_entry[1]),int(enddate_entry[2]))

df = web.DataReader(company_name, 'yahoo', start, end)

print (df.head())

def date_validation: