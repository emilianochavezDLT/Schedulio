
import Employee
import Suggestion
from Functions import *

running = True

employees = []

print("\nWelcome to Schedulio what would you like to do? Enter '?' for help or x to Exit")
user = "currentUser>"
while(running):
	userIn = input(user)

	current = 0;

	if(str(userIn) == "?" ):
		displayHelp()

	elif(str(userIn) == "x"):
		running = False

	elif(str(userIn) == "add"):
		tempEmp = addEmployee()

		if(tempEmp is None):
			print("(No employee added)")

		else:
			employees.append(tempEmp)

			current = len(employees) - 1

			print("Would you like to set their availaiblity [y/n]?")
			yesNo = input()

			if(str(yesNo) == "y"):
				availability(employees[current])

	elif(str(userIn) == "view"):

		if(len(employees) == 0):
			print("There are currently no employees, would you like to add one [y/n]")
			yesNo = input()
			if(validYN(yesNo) == True):
				tempEmp = addEmployee()

				if(tempEmp is None):
					print("(No employee added)")

				else:
					employees.append(tempEmp)

					current = len(employees) - 1

				print("Would you like to set their availaiblity [y/n]?")
				yesNo = input()

				if(validYN(yesNo) == True):
					availability(employees[current])
				else:
					print("Employee " + employees[current].getName() + " added")


		else:

			print("Enter the ID of the employee you wish to view")
			valid = False
			userIn = input()
			while(not valid):
				try:
					userIn = int(userIn)
					valid = True
				except ValueError:
					print("Please enter a valid employee ID")
					userIn = input()

			valid = False
			while(not valid):
				try:
					current = employees[int(userIn - 1)]
					valid = True
					displayEmployee(userIn, current)

				except IndexError:
					print("Error: Employee does not exist")
					userIn = input()

	


	else:
		print("Unrecognized command enter ? for help.")


