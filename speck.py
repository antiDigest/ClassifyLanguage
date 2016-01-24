from stemming.porter2 import stem
from textblob import TextBlob
from MinEditDist import dist
import sys,re
reload(sys)
sys.setdefaultencoding('utf-8')

file1 = open('icnale_201302/Categorized/CHN/A20  (N=50)/CHN_PTJ_021_A2_0.txt','r')
xyz = file1.read().decode("utf-8-sig")
words = re.split('[\s?\.!,:;]+',xyz)

def check_word(var):
	a = TextBlob(var)
	new = a.correct()

	if var == new:
		print var,'Added to dictionary'
		with open('bigger.txt','a') as w:
			w.write(var+'\n')
	else:
		x = var
		y = new
		print 'MinEditDist = {%s} for {%s} and {%s}' % (dist(x,y),x,y)

def check_spelling(var):
	with open("bigger.txt") as myfile:
		for line in myfile:
			if line.strip() == var.lower():
				return 1
	return -1

def check(var):

	afs = stem(var)
	flag = check_spelling(afs.strip())
	
	if flag == -1:
		check_word(var)

for word in words:
	
	flag = check_spelling(word.strip())
		
	if flag == -1:
		check(word)

