import numpy as np

x = 'intention'
y = 'execution'

mind = np.ndarray(shape=(len(x)+1,len(y)+1),dtype=int)

def min(a, b, c):
	m = a if a < b else b
	m = m if m < c else c
	return m

def MinDist(n, m):
	for i in range(m+1):
		mind[0,i] = i

	for i in range(n+1):
		mind[i,0] = i

	for i in range(1,n+1):
		for j in range(1,m+1):
			
			a = mind[i-1,j] + 1
			b = mind[i,j-1] + 1
			
			if x[i-1] == y[j-1]:
				c=mind[i-1,j-1]
			else:
				c=mind[i-1,j-1]+2

			mind[i,j]=min(a, b, c)

	return mind[n,m]

def main(x,y);

	n=len(x)
	m=len(y)

	k=MinDist(n, m)

	for i in range(0,n+1):
		for j in range(0,m+1):
			print mind[i,j],
		print '\n'
	
	print 'Minimum Edit Distance :',k 


if __name__ == '__main__':
	main(x,y)
