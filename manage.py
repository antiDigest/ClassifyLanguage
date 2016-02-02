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

def create_train():

	start = time.time()

	header = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP','NNPS','PDT','POS','PRP','PRPD','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WPD','WRB','SentenceLength','WordCount','FunctionWordCount','count_errors','Sentiment','Polarity','Result']

	df = pd.DataFrame(columns=header)

	for f in glob.glob("icnale_201302/Main/TRAIN/*.txt"):
		if 'ENS' in f:
			myfile = open(f,'r')
			text = myfile.read()
			CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
				RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB = parse(text)
			data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
							RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,SentenceLength(text),\
							WordCount(text),FunctionWordCount(text),count_errors(text),sentiment(text),Polarity(text),1]
			
		else:
			myfile = open(f,'r')
			text = myfile.read()
			CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
				RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB = parse(text)
			data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
							RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,SentenceLength(text),\
							WordCount(text),FunctionWordCount(text),count_errors(text),sentiment(text),Polarity(text),2]

		df = df.append(pd.Series(data, index=header), ignore_index=True)
		end = time.time()

		if end-start > 60:
			print df
			start =time.time()

	df.to_csv('Outputs/train.csv',header=True,index=False)

	test_df = pd.DataFrame(columns=header)

	for f in glob.glob("icnale_201302/Main/TEST/*.txt"):
		if 'ENS' in f:
			myfile = open(f,'r')
			text = myfile.read()
			CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
				RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB = parse(text)
			data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
							RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,SentenceLength(text),\
							WordCount(text),FunctionWordCount(text),count_errors(text),sentiment(text),Polarity(text),1]
			
		else:
			myfile = open(f,'r')
			text = myfile.read()
			CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
				RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB = parse(text)
			data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
							RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,SentenceLength(text),\
							WordCount(text),FunctionWordCount(text),count_errors(text),sentiment(text),Polarity(text),2]

		test_df = test_df.append(pd.Series(data, index=header), ignore_index=True)
		end = time.time()

		if end-start > 60:
			print test_df
			start =time.time()

	for f in glob.glob("icnale_201302/Main/DEV/*.txt"):
		if 'ENS' in f:
			myfile = open(f,'r')
			text = myfile.read()
			CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
				RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB = parse(text)
			data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
							RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,SentenceLength(text),\
							WordCount(text),FunctionWordCount(text),count_errors(text),Sentiment(text),Polarity(text),1]
			
		else:
			myfile = open(f,'r')
			text = myfile.read()
			CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
				RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB = parse(text)
			data = [CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,\
							RP,SYM,TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,SentenceLength(text),\
							WordCount(text),FunctionWordCount(text),count_errors(text),Sentiment(text),Polarity(text),2]

		test_df = test_df.append(pd.Series(data, index=header), ignore_index=True)
		end = time.time()

		if end-start > 60:
			print test_df
			start =time.time()

	test_df.to_csv('Outputs/test.csv',header=True,index=False)

if __name__ == "__main__":
	create_train()
