#This is created by Emiliano Chavez De La Torre and Kenyou Teoh
#This is the main file of Scedulio, it is the file that will be run to start the program

import sys

#Since we don't have the BEO_Editor directory in the same directory as this file
#We need to add the path to the BEO_Editor directory ourselves
print("You need to input a path for the Beo Editor Directory")
print("For Emiliano the diretory is /Users/Echav/Documents/ANC_Root/")
print("For Kenyou the directory is (Your directory here)")
print("For Josh the directory is (Your directory here)")
print("If you know the directory then input (e), (k), or (j) for the corresponding person")

path_Emiliano = "/Users/Echav/Documents/ANC_Root/"
path_Kenyou = ""
path_Josh = ""
path_Input = input("Input the path here: ")
if path_Input == "e":
    path_Beo = path_Emiliano
elif path_Input == "k":
    path_Beo = path_Kenyou
elif path_Input == "j":
    path_Beo = path_Josh
else:
    path_Beo = path_Input
sys.path.append(path_Beo)


#Import the Employee class from the employee.py file
from Employee import Employee
#Import the Event class from the Event.py file. It's importing the class Event as a package
from BEO_Editor import BEO
from BEO_Editor import Event


#The display_Skelaton function will display the skelaton of the schedule
#It will take in an array of BEOs and display them in a skelaton
#Which will return the output of the skelaton, so we can use on the GUI/Schedule
def display_Skelaton(array_of_BEOs):

    #This is the header of the skelaton
    print("This is the display_Skelaton function")

    #This for loop will loop through the array of BEOs
    #and dispaly the corresponding factors needed fore the skelaton
    for beo in array_of_BEOs:
        print(f"{beo.get_function_room()} {beo.get_event_class()}")
        print(f"{beo.get_hour()}:{beo.get_minutes()}     {beo.get_people()}")


#This is the main function of the program
def main():

    #This is the welcome message that will be displayed when the program is run
    print("Welcome to Schedulio!")

    #Calling an instance of an Event
    my_event1 = Event.Event(event_name="Wedding Reception", event_date="2023-08-15")

    #Calling an instance of a BEO
    # Creating an instance of the BEO class
    my_beo1 = BEO.BEO(
        price=2500.00,
        hour=18,
        minutes=30,
        people=100,
        event=my_event1,
        menu_item="Beef Wellington",
        function_room="Ballroom",
        event_class="Buffet",
        comments="Allergies: No nuts, vegetarian options required."
    )

    my_event2 = Event.Event(event_name="Group Breakfast", event_date="2023-08-15")
    
    my_beo2 = BEO.BEO(
        price=1500.00,
        hour=18,
        minutes=30,
        people=300,
        event=my_event2,
        menu_item="Filet Mignon",
        function_room="Foyer",
        event_class="Buffet",
        comments="Allergies: No nuts, vegetarian options required."
    )


    #Creating an array of BEOs so that we can pass it into the display_Skelaton function
    beo_array = [my_beo1, my_beo2]

    #Calling the display_Skelaton function
    display_Skelaton(beo_array)

    


if __name__ == "__main__":
    main()


