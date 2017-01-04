from dataprep import *
from loaddata import *
class neuralnetwork:
	from sklearn.neural_network import MLPClassifier
	from sknn.mlp import Regressor, Layer
	import theano
	import pandas as pd
	import os
	import csv
	import glob
	import numpy as np
	import warnings
	warnings.filterwarnings("ignore", category=DeprecationWarning) 
	
	weather = weatherprep()
	crime = crimeprep()
	load = loaddata()
	
	df = load.df_merged[['TMAX  ','TMIN  ']]
	df = pd.DataFrame(df.values);
	df = df.head(10)
	X = np.array(df)
	X = X[2:]
	print(X) 
	print( "\n")
	
	df1 = load.df_merged[['Crime']]
	df1 = pd.DataFrame(df1.values);
	df1 = df1.head(8)
	y = np.array(df1)
	print(y)
	print( "\n")
	
	clf = MLPClassifier(solver='lbgfs', alpha=1e-5,hidden_layer_sizes=(15,), random_state=1)
	clf.fit(X, y.ravel())        
	print("The crime count for TMAX and TMIN values of [200., 150.] is:")
	print(clf.predict([200., 150.]))
	print( "\n")
	



