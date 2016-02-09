import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.metrics import f1_score
import scipy as sp

header = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP','NNPS','PDT',\
	'POS','PRP','PRPD','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT',\
	'WP','WPD','WRB','SentenceLength','WordCount',\
	'FunctionWordCount',\
	'count_errors','Sentiment',\
	'Polarity']

x = pd.read_csv('Outputs/train.csv',usecols=header)

x2 = pd.read_csv('Outputs/test.csv',usecols=header)

y = pd.read_csv('Outputs/train.csv',usecols=['Result'])
y2 = pd.read_csv('Outputs/test.csv',usecols=['Result'])

#Classifier takes input x and y
clf = LogisticRegression()
clf.fit(x, y)

# Predict y on x2
y_pred = clf.predict_proba(x2)[:,1]

def absolute(z):
	if z > 0.5:
		return 1
	return 0

# for i in y2.iteritems():
# 	print i

y_new = []
for i in y_pred:
	y_new += [absolute(i)]

print f1_score(y2, y_new)


clf = svm.LinearSVC()
clf.fit(x,y)

y_pred = clf.predict(x2)
# print y_pred

y_new = []
for i in y_pred:
	# print i
	y_new += [absolute(i)]

print f1_score(y2, y_pred)

