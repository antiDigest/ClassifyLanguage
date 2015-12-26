import os
from GrammarCheck import GrammarCheck, SpellCheck
from WordCount import WordCount, FunctionWordCount, SentenceLength, paragraphs
from StyleCheck import posgrams

def FromDatabase():
    
    print 'Filename,(Grammar,Spelling),Word Count,Average Sentence Length,Function Word Count,FWratio\n'

    for path, subdirs, files in os.walk(".", topdown=True):
        if "Base" in path:
            for filen in files:
                if "JPN" in filen:    
                    w = WordCount('icnale_201302/Base/'+filen)
                    f = FunctionWordCount('icnale_201302/Base/'+filen)
                    print filen+','+str(GrammarCheck('icnale_201302/Base/'+filen))+','\
                        +str(w)+','+str(SentenceLength('icnale_201302/Base/'+filen))+','+str(f)+','+\
                        str(float(float(f)/float(w)))


if __name__ == '__main__':
    FromDatabase()