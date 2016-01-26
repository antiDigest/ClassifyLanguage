import glob
import os
import shutil
import random

def main():
	for file in glob.glob("files/Base/*.txt"):
		a = file.split("\\")
		if not os.path.exists("files/Main/"):
		    os.makedirs("files/Main")
		path = 'files/Main/%s' %a[1]
		shutil.copy(file, path)

def ENS():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('ENS') > -1 :	
			files.append(a[1])

	for i in xrange(280):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(40):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]


def HKG():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('HKG') > -1 :	
			files.append(a[1])

	for i in xrange(140):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(40):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(20):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]


def PAK():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('PAK') > -1 :	
			files.append(a[1])

	for i in xrange(280):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(40):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]


def PHL():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('PHL') > -1 :	
			files.append(a[1])

	for i in xrange(280):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(40):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]
	
	
def SIN():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('SIN') > -1 :	
			files.append(a[1])

	for i in xrange(280):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(40):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]


def CHN():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('CHN') > -1 :	
			files.append(a[1])

	for i in xrange(560):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(160):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]


def IDN():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('IDN') > -1 :	
			files.append(a[1])

	for i in xrange(280):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(40):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]


def JPN():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('JPN') > -1 :	
			files.append(a[1])

	for i in xrange(560):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(160):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]



def KOR():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('KOR') > -1 :	
			files.append(a[1])

	for i in xrange(420):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(120):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(60):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]


def THA():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('THA') > -1 :	
			files.append(a[1])

	for i in xrange(560):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(160):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]


def TWN():
	files = []
	for file in glob.glob("files/Main/*.txt"):
		a = file.split("\\")
		if a[1].find('TWN') > -1 :	
			files.append(a[1])

	for i in xrange(280):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TRAIN"):
			    os.makedirs("files/Main/TRAIN")
		path = 'files/Main/TRAIN/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(80):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/DEV"):
			    os.makedirs("files/Main/DEV")
		path = 'files/Main/DEV/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

	for i in xrange(40):	
		a = random.randint(0,len(files)-1)
		source = 'files/Main/%s' %files[a]
		if not os.path.exists("files/Main/TEST"):
			    os.makedirs("files/Main/TEST")
		path = 'files/Main/TEST/%s' %files[a]
		shutil.copy(source, path)
		del files[a]

def remove():
	for file in glob.glob("files/Main/*.txt"):
		os.remove(file)

if __name__ == "__main__":
main()
ENS()
HKG()
PAK()
PHL()
SIN()
CHN()
IDN()
JPN()
KOR()
THA()
TWN()
remove()