from stemming.porter2 import stem
from textblob import TextBlob
from MinEditDist import dist
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')


def check_word(var):
    a = TextBlob(var)
    new = a.correct()
    
    if var == new:
        print "Word = '"+var+"'"
        x = var 
        nearlist = []
        with open("bigger.txt") as myfile:
            for line in myfile:
                y= line.strip()
                k = dist(x,y)
                if k == 1 or k==2:
                    nearlist += [y]
                else:
                    ind =  words.index(x)
        # print nearlist
        print "Current word : ",words[ind]
        print "Previous Word : ",words[ind-1]
        print "Next Word : ",words[ind+1]

    else:
        x = var
        y = new
        print 'MinEditDist = {%s} for {%s} and {%s}' % (dist(x, y), x, y)


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
        # if var is not None or var is not ' ':
        check_word(var)


def main():
    file1 = open('icnale_201302/Categorized/CHN/A20  (N=50)/CHN_PTJ_021_A2_0.txt', 'r')
    xyz = file1.read().decode("utf-8-sig")
    global words
    words = re.split('[\s?\.!,:; ]+', xyz)[:-1]

    for word in words:

        flag = check_spelling(word.strip())

        if flag == -1:
            check(word)

if __name__ == "__main__":
    main()
