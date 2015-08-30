

def FromDatabase():
	
	for path, subdirs, files in os.walk(".", topdown=True):

        subdirs[:] = [i for i in subdirs if i not in exclude]

        if "ham" in path:

            for filen in files:
                with open(path+'/'+filen,'r') as f:

                    # Remove the subject from the body                  
                    subject = re.split('Subject: ',f.readline())[1]
                    
                    body = f.read().decode('utf8', errors='ignore')
                    #print body
                    tokens = word_tokenize(body)
                    #print tokens
                    for word in tokens:
                        #print word
                        if word in filedist:
                            filedist.setdefault(word,[])[0] += 1
                        else:
                            filedist.setdefault(word,[]).append(1)
                            filedist.setdefault(word,[]).append(0)
                            filedist.setdefault(word,[]).append(0)
                        #print filedist

if __name__ == '__main__':
	FromDatabase()