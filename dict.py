# coding=utf8
# encoding=utf8
import sys
separator = ' '
def checkFormat():
	inp = open(sys.argv[1], 'r')

	feed = inp.readlines()
	i = 0
	l = len(feed)
	for f in feed:
		temp = f.replace("\n","").split(separator)
		if (len(temp) < 2):
			print "A"
			return False
		i = i+1
	inp.close()
	return True

def writeToDictPy():
	inp = open(sys.argv[1], 'r')
	out = open("userdict.py", 'w')
	feed = inp.readlines()
	out.write('# coding=utf8\n')
	out.write("dict = [\n")
	i = 0
	l = len(feed)
	for f in feed:
		print "C"
		temp = f.replace("\n","").split(separator)
		#temp = temp.decode('utf-8')
		if i == l-1:
			out.write('"'+temp[0]+'"')
			out.write(",")
			out.write('"'+temp[1]+'"')
		else:
			temp[1] = temp[1]#.strip(U+000D)
			#print temp[1]
			out.write('"'+temp[0]+'"')
			out.write(",")
			out.write('"'+temp[1]+'"')
			out.write(",\n")
		i = i+1
	out.write("\n]")
	inp.close()
	out.close()

def writeDefault():
	out = open("userdict.py", 'w')
	out.write("dict = []")

if checkFormat():
	print "B"
	writeToDictPy()
else:
	writeDefault()