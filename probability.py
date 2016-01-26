import glob
import re

# 1 for Eng, 2 for Non Eng

# 89057 words in ENS

# 1192362 words in Non ENS


class probability:

	def __init__(self, x, word = None):
		self.x = x
		self.y = word
		if self.y == None:
			if self.x == 1:
				prob = 400.0/5600.0
				print round(prob,3)
			elif self.x == 2:
				prob = 5200.0/5600.0
				print round(prob,3)
		else: 
			if self.x == 1:
				count = 0.0
				for file in glob.glob("files/Base/*.txt"):
					a = file.split("\\")
					if 'E' in a[1] and 'N' in a[1] and 'S' in a[1] :
						with open(file) as myfile:
							data = myfile.read().decode('utf-8-sig')

							word = re.split('[\s?\.!,:; ]+', data)[:-1]

							for check in word:								
								if check.lower() == self.y:
									count = count + 1

							myfile.close()	
				prob = count/89057.0
				print round(prob,3)

			elif self.x == 2:
				count = 0.0
				for file in glob.glob("files/Base/*.txt"):
					a = file.split("\\")
					if 'E' not in a[1] :
						with open(file) as myfile:
							data = myfile.read().decode('utf-8-sig')

							word = re.split('[\s?\.!,:; ]+', data)[:-1]

							for check in word:								
								if check.lower() == self.y:
									count = count + 1

							myfile.close()	
				prob = count/1192362.0
				print round(prob,3)


# To find No in words in Non ENS Files
# def count_words_nonENS():   
# 	i = 0
# 	count = 0
# 	for file in glob.glob("files/Base/*.txt"):
# 		a = file.split("\\")
# 		if 'E' not in a[1] :
# 			with open(file) as myfile:
# 				data = myfile.read().decode('utf-8-sig')

# 				word = data.split()

# 				count = count + len(word)

# 				myfile.close()	

# 	return count


# To find No in words in ENS Files
# def count_words_ENS():
# 	i = 0
# 	count = 0
# 	for file in glob.glob("files/Base/*.txt"):
# 		a = file.split("\\")
# 		if 'E' in a[1] and 'N' in a[1] and 'S' in a[1] :
# 			with open(file) as myfile:
# 				data = myfile.read().decode('utf-8-sig')

# 				word = data.split()

# 				count = count + len(word)

# 				myfile.close()

# 	return count 



# b = probability(1)
a = probability(2,"job")

