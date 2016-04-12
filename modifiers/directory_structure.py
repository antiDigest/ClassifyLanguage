import glob
import os
# import shutil
from shutil import copy
import random

var = ['ENS','HKG','PAK','PHL','SIN','CHN','IDN','JPN','KOR','THA','TWN']

def move():

	if not os.path.exists("icnale_201302/Main/"):
	    os.makedirs("icnale_201302/Main")
	if not os.path.exists("icnale_201302/Main/TRAIN"):
	    os.makedirs("icnale_201302/Main/TRAIN")
	if not os.path.exists("icnale_201302/Main/DEV"):
	    os.makedirs("icnale_201302/Main/DEV")
	if not os.path.exists("icnale_201302/Main/TEST"):
	    os.makedirs("icnale_201302/Main/TEST")

	k = []
	k1 = []
	k2 = []
	k3 = []

	for cont in var:
		i = 0
		for f in glob.glob("icnale_201302/Base/*.txt"):
			
			if cont in f and 'PTJ' in f:
				k+=[f]
				if i<70:
					filepath = f
					copypath = "icnale_201302/Main/TRAIN/"
					copy(filepath,copypath)
					k1 += [f]
				elif 90>i>=70 and i<90:
					filepath = f
					copypath = "icnale_201302/Main/DEV/"
					copy(filepath,copypath)
					k2 += [f]
				elif i>=90 and i<100:
					filepath = f
					copypath = "icnale_201302/Main/TEST/"
					copy(filepath,copypath)
					k3 += [f]

			elif cont in f and 'SMK' in f:
				k += [f]
				if i<70:
					filepath = f
					copypath = "icnale_201302/Main/TRAIN/"
					copy(filepath,copypath)
					k1 += [f]
				elif i>=70 and i<90 :
					filepath = f
					copypath = "icnale_201302/Main/DEV/"
					copy(filepath,copypath)
					k2 += [f]
				elif i>=90 and i<100:
					filepath = f
					copypath = "icnale_201302/Main/TEST/"
					copy(filepath,copypath)
					k3 += [f]

			i += 1

			if i>=100:
				i=0

	return len(k), len(k1),len(k2),len(k3)

if __name__ == "__main__":
	move()
	