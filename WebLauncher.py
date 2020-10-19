#Web Launcher

import webbrowser
import urllib.request	

#This method is for checking internet connection
def Connection_Established():
	try:
		urllib.request.urlopen('http://216.58.192.142',timeout = 5)
		#print(url)
		#If we connect with specified url,then return True otherwise throw Exception.
		return True
	except Exception as eobj:
		return False

def main():

	connect = Connection_Established()
	if connect:

		#print(webbrowser.open(url)) prints True
		#Display url using default browser
		webbrowser.open("https://www.hackerrank.com/",new = 2)

		#Open url in a new window of the default browser, if possible, otherwise, open url in the only browser window
		webbrowser.open_new("https://www.geeksforgeeks.org/")

		#Open url in a new page (“tab”) of the default browser, if possible, otherwise equivalent to open_new().
		webbrowser.open_new_tab("https://leetcode.com/")

		webbrowser.open("https://www.deccansociety.com/applicantLogin.htm?a=2&b=3&c=1385",new = 0)
	else:
		print("There is no internet connection...!")
		
if __name__ == "__main__":
	main()
