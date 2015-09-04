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
                    # print GrammarCheck('icnale_201302/Base/'+filen)
                    # print SpellCheck('icnale_201302/Base/'+filen)
                    # print WordCount('icnale_201302/Base/'+filen)
                    # print SentenceLength('icnale_201302/Base/'+filen)
                    # print FunctionWordCount('icnale_201302/Base/'+filen)
                    print posgrams('icnale_201302/Base/'+filen)
                    break
                    


if __name__ == '__main__':
    FromDatabase()