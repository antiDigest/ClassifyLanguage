from textblob import TextBlob
import glob

def polarity():
	polarity = []
	for f in glob.glob("files/Base/*.txt"):
		with open(f) as myfile:
			b = myfile.read().decode('utf-8-sig')
			text = TextBlob(b)
			pol = text.sentiment.polarity
			polarity.append(pol)
			myfile.close()
	print polarity

if __name__ == "__main__":
	polarity()