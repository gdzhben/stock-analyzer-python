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

class descriptive:
	data = None
	df = None
	tickers = None  

	def __init__(self, start, end,col_to_analysis,ticker):
		self.start_date = start
		self.end_date = end
		self.col = col_to_analysis
		self.tickers = ticker
		 


	def plot(self):
		dataframe_df = pd.DataFrame(self.df)
		plt.figure(figsize=(10,6))
		plt.plot(dataframe_df.index, dataframe_df)
		plt.xlabel("Date")
		plt.ylabel("Price")
		plt.legend(self.tickers)
		plt.show()

		
	def read_data(self):
		self.data = yf.download(self.tickers,
								start	=self.start_date, end=self.end_date)
		self.df = self.data[self.col]
		print(self.df)

	def print_descriptive(self):
		data_describe = pd.DataFrame(self.df)
		print("Description of Dataset:\n",data_describe.describe())
		print("Range:\n", max(data_describe.max()) - min(data_describe.min()))
		print("Coefficient of variation:\n", variation(data_describe))
		print("---------End of Description Result-----------")



