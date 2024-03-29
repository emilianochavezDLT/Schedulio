#This is word creater that will create a doc, pdf and text file
#It is a program that will randomly generate words, special characters, and numbers

#importing the libraries
import random
import string
from docx import Document
from fpdf import FPDF
from datetime import datetime, timedelta

####Random Word Generator####

#This function will generate a random string of characters
def generate_random_string(length):
    #This is the string that will be returned
    randomString = ""

    #This is the list of characters that will be used to generate the string, 
    #which includes letters, numbers, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    #This is the loop that will generate the string
    for i in range(length):
        randomString += random.choice(characters)
    
    #This is the string that will be returned
    return randomString

#This is the function that will generate a random word from the list
def generate_random_word():

    #This is the list of words that will be used to generate the string
    words = ['apple', 'banana', 'cherry', 'orange', 
             'pear', 'grape', 'pineapple', 'kiwi', 'mango',
             'watermelon', 'apricot', 'avocado', 'blueberry',
             'coconut', 'cranberry', 'fig', 'grapefruit', 'guava',
             'lemon', 'lime', 'lychee', 'papaya', 'peach', 'plum',
             'pomegranate', 'raspberry', 'strawberry', 'tangerine', 'blackberry',
             'boysenberry', 'cantaloupe', 'honeydew', 'kiwifruit', 'mandarin',
             'nectarine', 'passionfruit', 'persimmon', 'rhubarb', 
             'starfruit', 'cucumber', 'eggplant', 'tomato', 'bell pepper', 'carrot',
             'celery', 'cabbage', 'broccoli', 'cauliflower', 'spinach', 
             'kale', 'lettuce', 'peas', 'green beans', 'corn', 'potato', 
             'sweet potato', 'yam', 'pumpkin', 'squash', 'zucchini', 
             'onion', 'garlic', 'ginger', 'turmeric', 'cinnamon', 'nutmeg', 
             'cloves', 'coriander', 'cumin', 'paprika', 'thyme', 'rosemary', 'sage', 
             'basil', 'oregano', 'parsley', 'dill', 'chives', 'bay leaves', 'lemon grass', 
             'vanilla', 'chocolate', 'caramel', 'honey', 'maple syrup', 'peanut butter', 
             'almond butter', 'cashew butter', 'hazelnut spread', 'jam', 'jelly', 'marmalade', 
             'mustard', 'ketchup', 'mayonnaise', 'relish', 'salsa', 'hot sauce', 'soy sauce', 
             'teriyaki sauce', 'barbecue sauce']

    #This is the word that will be returned
    return random.choice(words)

def generateKeyWords():
     
     keywords = ['Breakfast', 'Lunch', 'Dinner', 'Break']
     return random.choice(keywords)

def generateTimeSlots():
    
    #for testing purposes only generate the 2 time slot
    return 2
    
    
    #timeSlots = [1, 2]
    #return random.choice(timeSlots) 

####Random Word Generator####


#This the extreme case function that will indicate 
#if a time that is being added is going over the extreme case
#Example: For breakfastes the latest time is 10:00 AM
#If the time is 10:30 AM then it will be changed to 10:00 AM
#This done for all the events
def extremeCase(currentTime , extremeCaseTime):
    
    #This is the string that will be returned
    correctedTime = ""

    #Converting the time to a time object
    time_obj = datetime.strptime(currentTime, '%I:%M %p').time()
    #Converting the extreme case time to a time object
    extremeCase_obj = datetime.strptime(extremeCaseTime, '%I:%M %p').time()

    #Checking if the time is greater than the extreme case time
    if time_obj > extremeCase_obj:
        #Converting the time back to a string
        correctedTime = time_obj.strftime('%I:%M %p')
    else:
        #Converting the extreme case time back to a string
        correctedTime = extremeCase_obj.strftime('%I:%M %p')

    return correctedTime




###Pattern Generator for times###
def generate_Time_Pattern(keyword, timeInbetween):
    #This is the string that will be returned
    randomTime = ""



    return randomTime
    
def leadingZero(minute):
    #This is the string that will be returned
    correctedTime = ""

    #Generating a leading zero for the minute
    #if the length of the minute is 1, then we add a leading zero
    if len(minute) == 1:
        #Adding a leading zero
        correctedTime = "0" + minute

    return correctedTime


#These are the event time function that will determine the times of the events
#Based on the keywords
#hasATimeGenerated is a bool that will determine if a time has been generated
#timeGenerated is the time that was previously generated
def breakFast(hasATimeGenerated, timeGenerated):
    #This is the string that will be returned
    randomTime = ""

    #Checking if a time has been generated
    if hasATimeGenerated == True:
        #Converting the time to a time object
        time_obj = datetime.strptime(timeGenerated, '%I:%M %p').time()
        #Creating a random number generater. If the time is even then we add 30 minutes
        #If the time is odd then we add 1hour
        randomNum = random.randint(0, 1)
        
        #We are going to add another if statment saying if the time
        # equals to 3:30pm then that will the latest time it can be 
        # and if it is 3:30pm then we will not add any more time to it
        
        if randomNum == 0:
            #Adding 30 minutes to the time object
            time_obj += timedelta(minutes=30)
            time_obj = extremeCase(time_obj.strftime('%I:%M %p'), "10:00 AM")
        else:
            #Adding 1 hour to the time object
            time_obj += timedelta(hours=1)
            time_obj = extremeCase(time_obj.strftime('%I:%M %p'), "10:00 AM")
        
        #Converting the time back to a string
        randomTime = time_obj.strftime('%I:%M %p')


    else:
        #Generating the random hour and minute
        randomHour = str(random.randint(2, 10))
        randomMinute = str(random.randint(0, 59))
        #Generating a leading zero for the minute
        randomMinute = leadingZero(randomMinute)


        ##This is the string that will be returned
        randomTime = randomHour + ":" + randomMinute + " " + "AM"

    return randomTime

def lunch(hasATimeGenerated, timeGenerated):
    #This is the string that will be returned
    randomTime = ""

    #Checking if a time has been generated
    if hasATimeGenerated == True:
        #Converting the time to a time object
        time_obj = datetime.strptime(timeGenerated, '%I:%M %p').time()
        #Creating a random number generater. If the time is even then we add 30 minutes
        #If the time is odd then we add 1hour
        randomNum = random.randint(0, 1)
        
        #We are going to add another if statment saying if the time
        # equals to 3:30pm then that will the latest time it can be 
        # and if it is 3:30pm then we will not add any more time to it
        
        if randomNum == 0:
            #Adding 30 minutes to the time object
            time_obj += timedelta(minutes=30)
            time_obj = extremeCase(time_obj.strftime('%I:%M %p'), "3:30 PM")
        else:
            #Adding 1 hour to the time object
            time_obj += timedelta(hours=1)
            time_obj = extremeCase(time_obj.strftime('%I:%M %p'), "3:30 PM")
        
        am_pm = "AM"
        #Checking if the hour is greater than 12
        if time_obj.hour > 12:
            #Subtracting 12 from the hour
            time_obj.hour -= 12
            #Setting the am/pm to pm
            am_pm = "PM"
        

        #Converting the time object back to a string
        randomTime = time_obj.strftime('%I:%M ') + am_pm
    
    #If a time has not been generated then we generate a random time
    else:
        #Generating the random hour and minute
        randomHour = str(random.randint(10, 2))
        randomMinute = str(random.randint(0, 59))
        randomMinute = leadingZero(randomMinute)

        if randomHour == '10' or randomHour =='11':
             randomHour = randomHour + ":" + randomMinute + " " + "AM"
        else:
             randomHour = randomHour + ":" + randomMinute + " " + "PM"

    ##This is the string that will be returned
    return randomTime

def dinner(hasATimeGenerated, timeGenerated):
    #This is the string that will be returned
    randomTime = ""



    if hasATimeGenerated == True:
        #Converting the time to a time object
        time_obj = datetime.strptime(timeGenerated, '%I:%M %p').time()
        #Creating a random number generater. If the time is even then we add 30 minutes
        #If the time is odd then we add 1hour
        randomNum = random.randint(0, 1)
        
        #We are going to add another if statment saying if the time
        # equals to 3:30pm then that will the latest time it can be 
        # and if it is 3:30pm then we will not add any more time to it
        
        if randomNum == 0:
            #Adding 30 minutes to the time object
            time_obj += timedelta(minutes=30)
            #Converting the time object back to a string, but it will return
            #The correct time if the time is greater than 3:30pm
            time_obj = extremeCase(time_obj.strftime('%I:%M %p'), "3:00 AM")
        else:
            #Adding 1 hour to the time object
            time_obj += timedelta(hours=1)
            time_obj = extremeCase(time_obj.strftime('%I:%M %p'), "3:00 AM")
        
        am_pm = "AM"
        #Checking if the hour is greater than 12
        if time_obj.hour > 12:
            #Subtracting 12 from the hour
            time_obj.hour -= 12
            #Setting the am/pm to pm
            am_pm = "PM"
        

        #Converting the time object back to a string
        randomTime = time_obj.strftime('%I:%M ') + am_pm

    else:
        #we are going to assume that hour is 4 
        #We do not want the hour to be 4 if it is then we will generate a new time
        wasFourGenerated = True
        while wasFourGenerated:
            #Generating the random hour and minute
            randomHour = str(random.randint(1, 12))
            #If the hour is not 4 then we stop the loop
            if randomHour != '4' and randomHour != '04':
                wasFourGenerated = False
            randomMinute = leadingZero(str(random.randint(0, 59)))


        #If the hour equals 12, 1, 2, or 3 then we add AM
        #using 'in' creates a tuple and we are checking if the hour is in the tuple
        #this does a linear search. It will go to 12, 1, 2, 3 and evualte them 
        # until one of them is true. If all of them are false 
        #it will go to our else statement
        if randomHour in ('12', '1', '2', '3'):
            randomTime = randomHour + ":" + randomMinute + " " + "AM"

        #If the hour does not equal 12, 1, 2, or 3 then we add PM
        else:
            randomTime = randomHour + ":" + randomMinute + " " + "PM"

    return randomTime



####This is the File Creator####

#Save to text file
def save_to_text(content, filename):

    with open(filename, "w") as file:
        file.write(content)

#Save to docx file
def save_to_docx(content, filename):
    
        document = Document()
        document.add_paragraph(content)
        document.save(filename)

#Save to pdf file
def save_to_pdf(content, filename):

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 12)
            pdf.multi_cell(0, 10, txt = content, align = "L")
            pdf.output(filename)


##################################

#This is the main function of the program
def main():

    #Changing the length of the random string
    randomCount = 10

    #The array that will hold the random words
    randomWords = []

    
    #We need to generate at least 10 random words and put them into an array
    for i in range(randomCount):
        randomWords.append(generate_random_word())
    
    #This is generating the random string which will give us randome characters, letters, and special characters
    randomString = generate_random_string(randomCount)

    #This is generating the random numbers
    randomNumbers = str(random.randint(0, 100))
    
    #Now we have to cocatenate the random words, string, and numbers
    #This is the string that will hold the random words, string, and numbers
    randomWordsString = ""

    #We only want to generate the keywords once
    keywordsGererator = 0
    keyWordGenerated = generateKeyWords()
    timeSlotted = generateTimeSlots()


    #This is the loop that will concatenate the random words, string, and numbers
    for i in range(randomCount):

        #Random words are being concatenated and a space is being added
        randomWordsString += randomWords[i] + " "
        randomWordsString += randomString + " "
        randomWordsString += randomNumbers + " "
        randomWordsString += generate_Time_Pattern(keyWordGenerated, timeSlotted) + " "

        #An if statement to generate the keywords only once
        if keywordsGererator == 0:
            randomWordsString += generateKeyWords() + " "
            keywordsGererator += 1
            
        


    #This is the string that will hold the random words, string, and numbers
    print("This is the random words String that was generated \n",randomWordsString)

    
    
    
    
    
    
    
    
    
    
    #This is the name of the file that will be created
    #filename = "randomWords"

    #This is the file extension that will be used
    #fileExtensionText = ".txt"
    #fileExtensionDocx = ".docx"
    #fileExtensionPdf = ".pdf"

    #This is the file name that will be used for the text file
    #filenameText = filename + fileExtensionText
    #filenameDocx = filename + fileExtensionDocx
    #filenamePdf = filename + fileExtensionPdf
    # 
    #This is the content that will be saved to the file
    #content = randomWordsString


    #This is the function that will save the content to the file
    #save_to_text(content, filenameText)

    ##This is the function that will save the content to the file
    #save_to_docx(content, filenameDocx)

    ##This is the function that will save the content to the file
    #save_to_pdf(content, filenamePdf)     
    

if __name__ == "__main__":
    main()
