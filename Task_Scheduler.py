#Task_Scheduler

import time
import schedule
import datetime

def MinSchedule():
	print("Scheduling at minute..!")

def HourSchedule():
	print("Scheduling at hour..!")

def DaySchedule():
	print("Scheduling at Day..!")

def Hello():
	print("Mumbai..!")

def main():

	print(datetime.datetime.now().strftime("[%d-%m-%Y]"))
	schedule.every(1).minutes.do(MinSchedule)				#Scheduling task for minutes.

	schedule.every().hours.do(HourSchedule)					#Scheduling task for hours.

	schedule.every().day.at("17:00").do(DaySchedule)		#Scheduling task for every day.

	schedule.every(5).to(10).seconds.do(Hello)				#Scheduling task for random second between 5 to 10 seconds.

	schedule.every().tuesday.do(Hello)						#Scheduling task on every tuesday.

	schedule.every().tuesday.at("00:00").do(Hello)			#Scheduling task on every tuesday at 12.00 am.

	while True:												#This while is for scheduling multiple tasks
		schedule.run_pending()								#For running remaining tasks
		time.sleep(2)										#Time Gap between each pending scheduling

if __name__ == "__main__":
	main()