
with open('EnglishAuxiliaryVerbs.txt','r') as f:
	lines = f.read().split('\n')
	auxverbs = [line for line in lines if not "//" in line] 

with open('EnglishConjunctions.txt','r') as f:
	lines = f.read().split('\n')
	conjunctions = [line for line in lines if not "//" in line] 

with open('EnglishDeterminers.txt','r') as f:
	lines = f.read().split('\n')
	determiners = [line for line in lines if not "//" in line] 

with open('EnglishPrepositions.txt','r') as f:
	lines = f.read().split('\n')
	prepositions = [line for line in lines if not "//" in line] 

with open('EnglishPronouns.txt','r') as f:
	lines = f.read().split('\n')
	pronouns = [line for line in lines if not "//" in line] 

with open('EnglishQuantifiers.txt','r') as f:
	lines = f.read().split('\n')
	quantifiers = [line for line in lines if not "//" in line] 

allwords = auxverbs + conjunctions + determiners +prepositions+pronouns+quantifiers
print allwords

def WordCount(filename):
	with open(filename,'r') as f:
		return len(f.read().split(' '))

def FunctionWordCount(filename):
	with open(filename,'r') as f:
		filewords = f.read().split(' ')
	count =0
	for i in filewords:
		if i in allwords:
			count += 1

	return count
