from textblob import TextBlob
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def search(list, ground):
    for (i, v) in enumerate(list):
        if v == ground:
            return "none"
    return ground

def spell_check():
	file1 = open("icnale_201302/Categorized/ENS1/ENS_PTJ_001_XX_0.txt")
	
	a = file1.read().decode("utf-8-sig")
	b = TextBlob(a)
	
	string1 = b.split()

	# print string1

	new = b.correct()
	string2 = new.split()

	if b == new:
		print "Correct"
	else :
		print new
		for i in xrange(len(string1)):
			flag = search(string2, string1[i])
			if flag is not "none":
				print flag


if __name__ == "__main__":
    spell_check()

