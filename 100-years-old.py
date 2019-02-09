import datetime

def calc_age():

	#Importing current date ddmmyyyy
	current_date = datetime.date.today()

	#Find user age

	age = int(input("Enter your age"))

	#Find DOB

	dob = str((input("Enter your Date Of Birth (dd mm yyyy)"))