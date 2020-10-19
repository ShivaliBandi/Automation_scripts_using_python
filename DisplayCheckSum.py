#Assignment11_1.py

from sys import *
import os
import hashlib 						#for calculating checksum

def DisplayCheckSum(pathname):
	
	#Checking for absolute path
	if(os.path.isabs(pathname) != True):
		pathname = os.path.abspath(pathname)

	#Checking for directory
	if(os.path.isdir(pathname)):
		for folder, subfolder, filename in os.walk(pathname):
			for fn in filename:
				fn = os.path.join(folder,fn)
				#f1 = open(fn, "rb")
				#f1.read()
				chksum = hashlib.md5(open(fn,"rb").read())
				print("CheckSum of "+os.path.relpath(fn)+" is :\n"+chksum.hexdigest())
				print("\n**************************************")

	else:
		print("Directory not found...!")
		exit()

def main():
	
	print("Application Name is "+argv[0])

	if(len(argv) != 2):
		print("My_Error : Invalid Arguments..!")
		exit()

	if(argv[1] == "-h" or argv[1] == "-H"):
		print("My_Help : This script displays the checksum of all files from given folder.\nFor usage, type -u or -U.")
		exit()

	if(argv[1] == "-u" or argv[1] == "-U"):
		print("My_Usage : Filename.py folder_name")
		exit()

	try:
		DisplayCheckSum(argv[1])
		print("Work is done...!")

	except Exception as eobj:
		print(eobj)



if __name__ == "__main__":
	main()

"""
m = hashlib.md5()
print(m)
"""