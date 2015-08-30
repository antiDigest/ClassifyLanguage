import os
from GrammarCheck import GrammarCheck, SpellCheck

def FromDatabase():
    
    for path, subdirs, files in os.walk(".", topdown=True):
        if "Base" in path:
            for filen in files:
                if 'TWN' in filen:
                    print filen
                    GrammarCheck('icnale_201302/Base/'+filen)
                    SpellCheck('icnale_201302/Base/'+filen)
                    break
                    


if __name__ == '__main__':
    FromDatabase()