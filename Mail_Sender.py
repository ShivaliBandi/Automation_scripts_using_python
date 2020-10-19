#Mail_Sender

from sys import argv
import urllib.request
import smtplib
import time

def Connection_Established():
	try:
		urllib.request.urlopen('http://www.google.com',timeout = 10)
		#print(url)
		return True
	except Exception as eobj:
		return False

def Mail_Sender(sender,password):
	receiver = ['moresmansi@gmail.com','poojasawant9696@gmail.com']

	Subject = "Python Auto Generated Script : Doubt"
	data = repr("""This Script is auto Generated. Sir, What is the meaning of this regex..?  \\b(\\w+)(?:\\W+\\1\\b)+""")

	message = "Subject : {}\n\n{}".format(Subject,data)
	try:
		ss = smtplib.SMTP_SSL('smtp.gmail.com',465)
		#ss.starttls()
		ss.ehlo()
		ss.login(sender,password)
		ss.sendmail(sender,receiver,message)
		ss.quit()

		print("Mail sent successfully..!")
	except Exception as eobj:
		print("Mail sending failed..!\n",eobj)

def main():
	print("Application name is "+argv[0])


	try:
		print("Checking for internet connection...")
		connection = Connection_Established()

		if connection:
			#print("Hello")
			start_time = time.time()
			sender = 'mansimumbai123@gmail.com'
			password = 'Mumbai_Google11'
			Mail_Sender(sender,password)
			end_time = time.time()

			print("Time interval : ",end_time - start_time)
		else:
			print("There is no internet connection..!")
			
	except Exception as eobj:
		print(eobj)

if __name__ == "__main__":
	main()