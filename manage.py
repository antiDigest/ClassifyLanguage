import glob
import os
from shutil import copy
import random
from WordCount import *
from text_parsing import *
from speck import *
from sentiment import sentiment, Polarity
# from polarity import Polarity
import pandas as pd
import time

var = ['ENS','HKG','PAK','PHL','SIN','CHN','IDN','JPN','KOR','THA','TWN']

def create():

	start = time.time()

	header = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP','NNPS','PDT',\
	'POS','PRP','PRPD','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT',\
	'WP','WPD','WRB','past tense','present tense','Plural','Singular','SentenceLength','WordCount',\
	'FunctionWordCount',\
	'count_errors','Sentiment',\
	'Polarity','Result']

	df = pd.DataFrame(columns=header)

	for cont in var:
		for f in glob.glob("icnale_201302/Main/TRAIN/*.txt"):
			if cont in f:
				myfile = open(f,'r')
				text = myfile.read()
				CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
					RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,past,present,plural,\
					singular = parse(text)
				data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
								RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,past,present,\
								plural,singular,SentenceLength(text),\
								WordCount(text),FunctionWordCount(text),count_errors(text),\
								sentiment(text),\
								Polarity(text),cont]

				df = df.append(pd.Series(data, index=header), ignore_index=True)
				end = time.time()

				if end-start > 60:
					print df
					start =time.time()

	df.to_csv('Outputs/train_all.csv',header=True,index=False)

	test_df = pd.DataFrame(columns=header)

	for cont in var:
		for f in glob.glob("icnale_201302/Main/TEST/*.txt"):
			if cont in f:
				myfile = open(f,'r')
				text = myfile.read()
				CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
					RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,past,present,plural,\
					singular = parse(text)
				data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
								RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,past,present,\
								plural,singular,SentenceLength(text),\
								WordCount(text),FunctionWordCount(text),count_errors(text),\
								sentiment(text),\
								Polarity(text),cont]
				test_df = test_df.append(pd.Series(data, index=header), ignore_index=True)
				end = time.time()

				if end-start > 60:
					print test_df
					start =time.time()

	for cont in var:
		for f in glob.glob("icnale_201302/Main/DEV/*.txt"):
			if cont in f:
				myfile = open(f,'r')
				text = myfile.read()
				CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
					RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,past,present,plural,\
					singular = parse(text)
				data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
								RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,past,present,\
								plural,singular,SentenceLength(text),\
								WordCount(text),FunctionWordCount(text),count_errors(text),\
								sentiment(text),\
								Polarity(text),cont]
				test_df = test_df.append(pd.Series(data, index=header), ignore_index=True)
				end = time.time()

				if end-start > 60:
					print test_df
					start =time.time()

	test_df.to_csv('Outputs/test_all.csv',header=True,index=False)

if __name__ == "__main__":
	create
