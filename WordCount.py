

def WordCount(filename):
	with open(filename,'r') as f:
		return len(f.read().split(' '))

