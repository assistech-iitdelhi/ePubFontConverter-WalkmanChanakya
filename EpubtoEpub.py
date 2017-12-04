import os
import sys

path = os.getcwd() 
#print "Path: ",path

#folder = sys.argv[1]
#print "Folder: " , folder
#file_name = "sahitya"

#command = "./epubToEpub.sh " +file_name +" 1"
#print command

DIR_LIST =  os.listdir(path) 
print "files in  dir: " ,DIR_LIST

for files in DIR_LIST:
	#print files
	if(files.split(".")[-1]=="epub"):
		print 'epubs: ' , files
		file_name = files.split(".")[0]
		command = "./epubToEpub.sh " + file_name +" 1"
		print "*******************CONVERTING file  " + str(files) + " \n\n\n"
		os.system(command)


