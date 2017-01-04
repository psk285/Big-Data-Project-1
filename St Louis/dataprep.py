class crimeprep:
	import pandas as pd
	import os
	import csv
	import glob

	path_ = "//Users/pratikkamath30/Documents/Big Data Ind/MinorityReportCrimeAnalysis/raw_data/raw_data_crime"
	allFile = glob.glob(path_ +"/*.csv")
	crimeframe = pd.DataFrame()
	alist = []
	for file_ in allFile:
		df_ = pd.read_csv(file_,index_col= None, header=0, usecols=['MonthReportedtoMSHP','DateOccured','Count','Crime','District','Neighborhood','XCoord','YCoord'])
    	alist.append(df_)
	crimeframe = pd.concat(alist)
	crimeframe['DateOccured'] = pd.to_datetime(crimeframe['DateOccured'])
	crimeframe['DateOccured'] = crimeframe['DateOccured'].dt.date
	crimeframe.to_csv('//Users/pratikkamath30/Documents/f_crime.csv')

class weatherprep:
	import pandas as pd
	import os
	import csv
	import glob
	import time
	path = "//Users/pratikkamath30/Documents/Big Data Ind/MinorityReportCrimeAnalysis/raw_data/raw_data_weather/raw_data_weather.csv"

	allFiles = glob.glob(path)
	weatherframe = pd.DataFrame()
	list_ = []
	for file_ in allFiles:
    		df_ = pd.read_csv(file_,index_col=None, header=0, usecols=['DATE  ', 'TMAX  ','TMIN  '])
    		list_.append(df_)
	weatherframe = pd.concat(list_)
	weatherframe['DATE  '] = pd.to_datetime(weatherframe['DATE  '], format='%Y%m%d')
	weatherframe=weatherframe.rename(columns = {'DATE  ':'DateOccured'})
	weatherframe.to_csv('//Users/pratikkamath30/Documents/f_weather.csv')
	





