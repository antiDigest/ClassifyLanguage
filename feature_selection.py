import numpy as np
import pandas as pd
import math


header = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP','NNPS','PDT',\
    'POS','PRP','PRPD','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT',\
    'WP','WPD','WRB','SentenceLength','WordCount',\
    'FunctionWordCount',\
    'count_errors','Sentiment',\
    'Polarity','Result']

X = pd.read_csv('Outputs/train.csv',usecols=header)
y = pd.read_csv('Outputs/train.csv',usecols=['Result'])

total = X.shape[0]


def probability(val):
    if val==1:
        return y.sum()/y.shape[0]
    else:
        return (1 - y.sum()/y.shape[0])

def InformationGain(a,split=5):

    g = X.as_matrix([a])

    def _info(split):
        split1 = 0
        split2 = 0
        num1=0
        num2=0

        g = X.as_matrix([a,'Result'])

        for i in g:
            if i[0] < split:
                split1 += i[1]
                num1 += 1
            else:
                split2 += i[1]
                num2 += 1

        if split1 == 0:
            info2,info1 = split2/num2, 0
        elif split2 == 0:
            info2,info1 = 0, split1/num1    
        else:
            info2,info1 = split2/num2, split1/num1
        
        entropy = 0

        for i in range(1):
            pi = probability(i)
            entropy -= pi * math.log(pi)

        gain = entropy - info1 - info2

        # print gain
        return math.fabs(gain)

    def _split():
        maxgain = 0
        maxsplit = 0
        for i in np.sort(g,axis=0):
            k = _info(i)
            if k > maxgain:
                maxgain = k
                maxsplit = i

        return maxsplit,maxgain

    return _split()


def correlation(A,B):
    meanA = X[A].sum()/X.shape[0]
    meanB = X[B].sum()/X.shape[0]

    r = 0
    g = X.as_matrix([A,B])
    for i in xrange(X.shape[0]):
        # print (g[i][1]-meanB) * (g[i][0]-meanA)
        r += (g[i][1]-meanB) * (g[i][0]-meanA)
        # break

    # print r

    r = r / X.shape[0]

    g1 = X.as_matrix([A])
    g2 = X.as_matrix([B])

    r = r/np.std(g1, axis=0)
    r = r/np.std(g2, axis=0)

    return r

def mutual_info(A,B):
    return 0

if __name__ == '__main__':
    for i in xrange(len(header)):
        for j in xrange(len(header)):
            print header[i],"\t",header[j],"\t",correlation(header[i],header[j])
        print '\n'

    mutual_info(1,2)