import pandas as pd
import os

columns = ['Country','Type','Serial','CEFR','Upper/lower/students/teachers/others','Grammar',\
'Spelling','Word Count','Average Sentence Length','Function Word Count','FWratio']


for files in os.listdir('Outputs'):
	# print files
	data = pd.read_csv('Outputs/'+files,sep=',|[,\(]|\),|\_',names=columns,engine='python')

	data.to_csv('Outputs/Base.csv',header=False,sep=',', mode='a',columns=columns)
