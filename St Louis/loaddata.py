from dataprep import *
class loaddata:
	import pandas as pd
	import os
	import csv
	import glob
	import numpy as np

	weather = weatherprep()
	crime = crimeprep()
	frames = [crime.crimeframe, weather.weatherframe]
	result = pd.concat(frames)
	print(weatherprep.weatherframe)
	print(crimeprep.crimeframe)
	df_merged = pd.DataFrame()
	weatherprep.weatherframe.set_index('DateOccured', inplace = True)
	crimeprep.crimeframe.set_index('DateOccured', inplace = True)
	df_merged = crime.crimeframe.join(weatherprep.weatherframe)
	df_merged = df_merged.dropna()
	df_merged.to_csv('//Users/pratikkamath30/Documents/tp.csv')
	weather.weatherframe.to_csv('//Users/pratikkamath30/Documents/formatted_weather.csv')
	crime.crimeframe.to_csv('//Users/pratikkamath30/Documents/formatted_crime.csv')
	print(df_merged)
	
