#Assignment10_3.py

from sys import *
import os
import shutil

def FileCopy(pathname1,pathname2):
	
	if(os.path.isabs(pathname1) == False):				
		pathname = os.path.abspath(pathname1)

	chkdir = os.path.isdir(pathname1)

	if(chkdir):										#If my first directory is present then only consider another directory name
		if(os.path.isdir(pathname2) == False):
			os.mkdir(pathname2)
			
			for folder,subfolder,fname in os.walk(pathname1):
				#for sub in subfolder:

				for fn in fname :
					filen1 = os.path.join(folder,fn)
					shutil.copy(filen1,pathname2)
		else:
			print("Directory is already exits...!")
			exit()			
	else:
		print("Directory not found..!")

	print("Changes updated...!")
def main():
	if(len(argv) > 3):
		print("My_Error : Invalid no of Arguments...!")
		exit()

	if(len(argv) == 2):
		if(argv[1] == "-h" or argv[1] == "-H"):			##This option is for help.
			print("My_Help : This Scripts display files with the given extension.")
			exit()

		elif (argv[1] == "-u" or argv[1] == "-U"):		#This option is for demonstrating the syntax that user want to enter.
			print("My_Usage : Filename.py Directory_Name Specific_Extension")
			exit()

		else:
			print("My_Error : Wrong Arguments...!")
			exit()

	try:
		FileCopy(argv[1],argv[2])

	except Exception as eobj:
		print(eobj)


if __name__ == "__main__":
	main()
