from stemming.porter2 import stem
from textblob import TextBlob
from MinEditDist import main
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file1 = open('icnale_201302/Categorized/CHN/A20  (N=50)/CHN_PTJ_021_A2_0.txt','r')
xyz = file1.read().decode("utf-8-sig")
mat = xyz.split()

def check_word(var):
	a = TextBlob(var)
	new = a.correct()

	if var == new:
		print a,":",
		print 'kuch to galat h'
	else:
		x = var
		y = new
		print 'MinEditDist = {} for {} and {}'.format(main(x,y),x,y)

def check_spelling(var):
	with open("bigger.txt") as myfile:
		for line in myfile:
			if line.strip() == var.lower():
				return 1
	return -1

def check(var):

	for char in var:
		if char == ',':
			a = var.replace(',','')
			afs = stem(a)
			flag = check_spelling(afs.strip())
		elif char == '.':
			b = var.replace('.','')
			afs = stem(b)
			flag = check_spelling(afs.strip())
		else:
			afs = stem(var)
			flag = check_spelling(afs.strip())
	if flag == -1:
		check_word(var)

for word in mat:
	for char in word:
		if char == ',':
			a = word.replace(',','')
			flag = check_spelling(a.strip())
		elif char == '.':
			b = word.replace('.','')
			flag = check_spelling(b.strip())
		else:
			flag = check_spelling(word.strip())

	if flag == -1:
		check(word)

