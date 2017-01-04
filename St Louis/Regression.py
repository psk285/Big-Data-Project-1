from dataprep import *
from loaddata import *
from neuralnetwork import *
import pandas as pd
import statsmodels.formula.api as sm
import matplotlib as mp

class LinearRegression:
	import matplotlib as mp
	import numpy as np
	import seaborn as sns

	weather = weatherprep()
	crime = crimeprep()
	load = loaddata()
	nn = neuralnetwork()
	df = load.df_merged

	result = sm.ols(formula = "Crime ~ TMAX + TMIN", data = df ).fit()
	print(result.summary())
	df_main = pd.concat((result.params, result.tvalues), axis = 1)
	df_main.plot()
	fig = mp.pyplot.scatter
	mp.pyplot.savefig("Op.png")


	snss = sns.lmplot(x = 'TMAX', y = 'Crime', data = df, fit_reg = True)
	snss.savefig('Outp.png')
	
	snss1 = sns.lmplot(x = 'TMIN', y = 'Crime', data = df, fit_reg = True)
	snss1.savefig('Outp1.png')


