import os
from GrammarCheck import GrammarCheck, SpellCheck
from WordCount import WordCount, FunctionWordCount, SentenceLength
from StyleCheck import posgrams

def FromDatabase():
    
    for path, subdirs, files in os.walk(".", topdown=True):
        if "Base" in path:
            for filen in files:
                if 'ENS' in filen:
                    print filen
                    print 'Grammar :', GrammarCheck('icnale_201302/Base/'+filen)
                    print 'Spelling :', SpellCheck('icnale_201302/Base/'+filen)
                    print 'Word Count :', WordCount('icnale_201302/Base/'+filen)
                    print 'Average Sentence Length :', SentenceLength('icnale_201302/Base/'+filen)
                    print 'Function Word Count :',FunctionWordCount('icnale_201302/Base/'+filen)
                    print 'POSGRAMS :', posgrams('icnale_201302/Base/'+filen)
                    break
                    


if __name__ == '__main__':
    FromDatabase()