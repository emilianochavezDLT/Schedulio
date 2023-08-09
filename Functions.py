
from Employee import *
from Suggestion import *

def displayHelp():
	print("\nadd\t(adds new employee)\nrm\t(removes an employee)\nevent\t(creates a new event)\nview\t(view employee)")

def validYN(yesNo):
	validAns = False
	while(not validAns):

		if(str(yesNo) == "y"):

			validAns = True
			return True
		#}

		elif(str(yesNo) == "n"):


			validAns = True
			return False
		#}

		else:

			print("please enter 'y' or 'n'")
			yesNo = input()


def addEmployee():
	print("You are now adding a new employee")
	employee = None

	no = True
	while(no):
		print("\nPlease enter their name: ")
		name = input()
		if(str(name) == "x"):
			break
		print("\nPlease enter their status (Fulltime/Partime): ")
		status = input()
		if(str(status) == "x"):
			break
		print("\nPlease enter their seniority: ")

		seniority = input()
		if(str(seniority) == "x"):
			break

		print("\nYou are now adding employee:\n----------------------------\nName:\t\t" + name +"\nStatus:\t\t" + status +"\nSenority:\t" + seniority)
		print("\nIs this information correct [y/n]?")		
		#validAns = False
		yesNo = input()
		if(validYN(yesNo) == True):
			employee = Employee(name, seniority, status)

			no = False
		else:

			print("\nPlease make corrections")

		#while(not validAns):
			#yesNo = input()
			#if(str(yesNo) == "y"):

				#employee = Employee(name, seniority, status)

				#no = False
				#validAns = True
			#}

			#elif(str(yesNo) == "n"):

				#print("\nplease make corrections\n")

				#validAns = True
			#}

			#else:

				#print("please enter 'y' or 'n'")

		
	#}


	return employee
#}


def availability(employee):
	print("Showing shifts for: " + employee.getName())
	employee.setAvail()
	#print("to add availability function later")


def displayEmployee(userIn, emp):
	print("\nInformation for employee " + str(userIn))
	print("----------------------------\nName:\t\t" + emp.getName() +"\nStatus:\t\t" + emp.getStatus() +"\nSenority:\t" + emp.getSeniority())

	print("\nAvailability for employee " + str(userIn) + "\n---------------------------")
	emp.getAvail()
	print()

