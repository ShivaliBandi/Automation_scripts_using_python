#Assignment11_4.py
import sys
import os
import hashlib
from datetime import date
import time

def DeleteDuplicateFiles(pathname):

	if os.path.isabs(pathname):
		pathname = os.path.abspath(pathname)

	if os.path.isdir(pathname):

		dict1 = {}
		for folder,subfolder,filename in os.walk(pathname):
			with open("DeleteDuplicateFiles1_log.txt","a") as fd:
				fd.write("----------------------------------------------------\n")
				fd.write(date.today().strftime('[%d-%m-%Y]')+" : ")
				for fn in filename:
					fn = os.path.join(folder,fn)
					chksum = hashlib.md5(open(fn,"rb").read()).hexdigest()

					if dict1.get(chksum) == None:
						dict1[chksum] = [fn]
						#fd.write("New Entry..!"+str(fn)+"\n")

					else:
						dict1[chksum].append([fn])
						fd.write("Duplicate file found and will be deleted : "+str(fn)+"\n")
						os.remove(fn)

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
		start_time = time.time()
		DeleteDuplicateFiles(sys.argv[1])
		end_time = time.time()

		print("Total time required for running script :",(end_time - start_time))
		print("work is done...!")

	except Exception as eobj:
		print(eobj)

if __name__ == "__main__":
	main()