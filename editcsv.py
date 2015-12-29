import pandas as pd
import os

columns = ['Country','Type','Serial','CEFR','Upper/lower/students/teachers/others','Grammar',\
'Spelling','Word Count','Average Sentence Length','Function Word Count','FWratio']


# for files in os.listdir('Outputs'):
	
data = pd.read_csv('Outputs/Base.csv',names=columns,engine='python')

CEFR = []
for i in data.itertuples():
	CEFR += [i[4]+'_'+i[5]]

data['Upper/lower/students/teachers/others'] = pd.DataFrame(CEFR)

print data

data.to_csv('Outputs/Base(1).csv',header=False, mode='a',columns=columns)
