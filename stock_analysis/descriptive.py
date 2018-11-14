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

	def __init__(self, start, end,col_to_analysis):
		self.start_date = start
		self.end_date = end
		self.col=col_to_analysis
		 


	def plot(self):
		
		df2 = self.df.copy()
		fig, ax = plt.subplots(figsize=(12, 6))
		ax.plot(df2)
		# df2.plot()
		ax.grid()
		code_name = {"AMZN": 'Amazon', "BABA": 'Alibaba'}
		ax.legend(df2.columns.map(code_name))
		ax.set_title('Stock Price Trends')
		ax.set_xlim(self.start_date, self.end_date)
		plt.show()
		
	def read_data(self):
		tickers = ["AMZN", "BABA"]
		self.data = yf.download(tickers=tickers,
								start=self.start_date, end=self.end_date)
		self.df = self.data[self.col]  # could be
		# changed into open, high, low data
		print(self.df)
		# self.df.plot()

	def print_descriptive(self):
		data_describe = pd.DataFrame(self.df)
		print("Description of Dataset:\n",data_describe.describe())
		print("Range:\n", max(data_describe.max()) - min(data_describe.min()))
		print("Coefficient of variation:\n", variation(data_describe))
		print("---------End of Description Result-----------")



