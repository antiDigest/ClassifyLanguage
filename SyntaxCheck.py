from nltk import tag

def BrillTag(input):
	print tag.brill.BrillTagger(input)