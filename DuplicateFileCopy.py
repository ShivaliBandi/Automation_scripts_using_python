#Assignment11_2.py

import sys
import os
import hashlib
from datetime import date

def DuplicateFileNames(pathname):

	if os.path.isabs(pathname):
		pathname = os.path.abspath(pathname)

	if os.path.isdir(pathname):

		dict1 = {}
		for folder,subfolder,filename in os.walk(pathname):
			with open("DuplicateFileNames_log.txt","a") as fd:
				fd.write("----------------------------------------------------\n")
				fd.write(date.today().strftime('[%d-%m-%Y]')+" : ")
				for fn in filename:
					fn = os.path.join(folder,fn)
					chksum = hashlib.md5(open(fn,"rb").read()).hexdigest()
					#print(chksum)
					if dict1.get(chksum) == None:
						dict1[chksum] = [fn]
						#fd.write("New Entry..!"+str(fn)+"\n")

					else:
						dict1[chksum].append([fn])
						fd.write("Duplicate file found : "+str(fn)+"\n")
					
		#print(dict1)
	else:
		print("Dictionary not found...!")
		exit()

def main():
	print("Application Name : ",sys.argv[0])

	if len(sys.argv) != 2:
		print("My_Error : Invalid no of arguments...!")
		exit()

	if sys.argv[1] == "-h" or sys.argv[1] == "-H":
		print("My_help : This script is for displaying names of duplicate files.\nFor usage : type -u or -U")
		exit()

	if sys.argv[1] == "-u" or sys.argv[1] == "-U":
		print("My_Usage : Filename.py Directory_name")
		exit()

	try:
		DuplicateFileNames(sys.argv[1])
		print("work is done...!")

	except Exception as eobj:
		print(eobj)

if __name__ == "__main__":
	main()
