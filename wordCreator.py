#This is word creater that will create a doc, pdf and text file
#It is a program that will randomly generate words, special characters, and numbers

#importing the libraries
import random
import string
from docx import Document
from fpdf import FPDF


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
####Random Word Generator####

###Pattern Generator for times###
def generate_Time_Pattern():
    #This is the string that will be returned
    randomString = ""

    #Generating the random hour and minute
    randomHour = str(random.randint(1, 12))
    randomMinute = str(random.randint(0, 59))


    #Generating a leading zero for the minute
    #if the length of the minute is 1, then we add a leading zero
    if len(randomMinute) == 1:
        #Adding a leading zero
        randomMinute = "0" + randomMinute

    #Generating a random AM or PM
    randomAMPM = random.choice(["AM", "PM"])

    #This is the string that will be returned
    randomString = randomHour + ":" + randomMinute + " " + randomAMPM
    print(randomString)
    return randomString
    



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

            width = 100
            height = 10

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 12)
            pdf.cell(width, height, txt = content, ln = 1, align = 'C')
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


    #This is the loop that will concatenate the random words, string, and numbers
    for i in range(randomCount):

        #Random words are being concatenated and a space is being added
        randomWordsString += randomWords[i] + " "
        randomWordsString += randomString + " "
        randomWordsString += randomNumbers + " "
        randomWordsString += generate_Time_Pattern() + " "
            
        


    #This is the string that will hold the random words, string, and numbers
    print("This is the random words String that was generated \n",randomWordsString)

    #This is the name of the file that will be created
    filename = "randomWords"

    #This is the file extension that will be used
    fileExtensionText = ".txt"
    fileExtensionDocx = ".docx"
    fileExtensionPdf = ".pdf"

    #This is the file name that will be used for the text file
    filenameText = filename + fileExtensionText
    filenameDocx = filename + fileExtensionDocx
    filenamePdf = filename + fileExtensionPdf
     
    #This is the content that will be saved to the file
    content = randomWordsString

    #This is the function that will save the content to the file
    save_to_text(content, filenameText)

    #This is the function that will save the content to the file
    save_to_docx(content, filenameDocx)

    #This is the function that will save the content to the file
    save_to_pdf(content, filenamePdf)     
    

if __name__ == "__main__":
    main()
