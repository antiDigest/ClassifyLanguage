from __future__ import division, unicode_literals
from textblob import TextBlob as tb
import math
import glob
import sys

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def filing():
	doc = []
	name = []
	file_names = glob.glob("files/Categorized/ENS1/*.txt")

	files =  map(open,file_names)

	document = [file.read() for file in files]
	[file.close() for file in files]	

	for a in xrange(len(document)):
		doc.append(document[a].decode("utf-8-sig"))

	for names in file_names:
		a = names.split('\\')
		name.append(a)

	bloblist = map(tb,doc)

	for i, blob in enumerate(bloblist):
	    print("Document : {}".format(name[0][1]))
	    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
	    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse = True)
	    for word, score in sorted_words[:1]:
	        score_weight = score * 100 
	        print("\t{}, {}".format(word.encode(sys.stdout.encoding, errors='replace'), round(score_weight, 3)))


if __name__ == "__main__":
    filing()
		