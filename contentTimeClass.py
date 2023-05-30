#This is the content and time class for the Schedulio program
#This class is used to store the content and time of the schedule

#This class is used to store the content and it is also the parent class of the time class
class fileContent:

    def __init__(self, content):
        self.content = content
    
    #This is our setter function
    def setContent(self, content):
        self.content = content

    #This is our getter function
    def getContent(self):
        return self.content
    
    #This function is used to print the content
    #We just have to use print(fileContent) to print the content
    def __str__(self):
        return self.content
    
#This class is used to store the time and it is the child class of the content class
class fileTime(fileContent):

    def __init__(self, content, time):
        #We use super() to inherit the content from the parent class
        super().__init__(content)
        #We set the time
        self.time = time



