import glob
import re
import time

# 1 for Eng, 2 for Non Eng
# 89057 words in ENS
# 1192362 words in Non ENS

class Probability:

	def __init__(self, x, word = None):
		self.x = x
		self.y = word
		if self.y == None:
			print self.single()
		else:
			print self.conditional()
			
	def single(self):
		if self.x == 1:
			prob = 400.0/5600.0
			return '{0:.5f}'.format(prob)
		elif self.x == 2:
			prob = 5200.0/5600.0
			return '{0:.5f}'.format(prob)

	def conditional(self):
		if self.x == 1:
			count = 0.0
			for f in glob.glob("icnale_201302/Base/*.txt"):
				if 'ENS' in f:
					with open(f) as myfile:
						data = myfile.read().decode('utf-8-sig')

						word = re.split('[\s?\.!,:; ]+', data)[:-1]

						for check in word:								
							if check.lower() == self.y:
								count = count + 1

						myfile.close()	
			prob = count/89057.0
			return '{0:.5f}'.format(prob)

		elif self.x == 2:
			count = 0.0
			for f in glob.glob("icnale_201302/Base/*.txt"):
				if 'ENS' not in f:
					with open(f) as myfile:
						data = myfile.read().decode('utf-8-sig')

						word = re.split('[\s?\.!,:; ]+', data)[:-1]

						for check in word:								
							if check.lower() == self.y:
								count = count + 1

						myfile.close()	
			prob = count/1192362.0

			return '{0:.5f}'.format(prob)


# To find No in words in Non ENS Files
def count_words_nonENS():   
	i = 0
	count = 0
	for f in glob.glob("icnale_201302/Base/*.txt"):
		if 'ENS' not in f:
			with open(f) as myfile:
				data = myfile.read().decode('utf-8-sig')

				word = data.split()

				count = count + len(word)

				myfile.close()	

	return count


# To find No in words in ENS Files
def count_words_ENS():
	i = 0
	count = 0
	for f in glob.glob("icnale_201302/Base/*.txt"):
		if 'ENS' in f:
			with open(f) as myfile:
				data = myfile.read().decode('utf-8-sig')

				word = data.split()

				count = count + len(word)

				myfile.close()

	return count 


start = time.time()

Probability(2)
Probability(2,"job")

end = time.time()

print "time",end-start
