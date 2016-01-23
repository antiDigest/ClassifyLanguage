x = 'hello'
y = 'yellow'
mind = [[]]


def min(a, b, c):
	min = a if a < b else b
	min = min if min < c else c
	return min


def MinDist(a, b):
	for i in xrange(1, m+1):
		mind[0][i] = i

	for i in xrange(1, n+1):
		mind[i][0] = i

	for i in xrange(n+1):
		for j in xrange(m+1):
			a = mind[i-1][j] + 1
			b = mind[i][j-1] + 1
			if x[i-1]) == y[j-1]:
				c=mind[i-1][j-1]
			else:
				c=mind[i-1][j-1]+2

			mind[i][j]=min(a, b, c)

	return mind;


if __name__ == "__main__":

	n=len(x)
	m=len(y)

	print x
	print y


	k=MinDist(n, m)


	print('Minimum Edit Distance : {}'.format(k))


	for i in xrange(n+1):
		for j in xrange(m+1):
			print mind[i][j]
			print "\t"
		print ''
		print ''
