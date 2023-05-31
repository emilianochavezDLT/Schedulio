#This is the content and time class for the Schedulio program
#This class is used to store the content and time of the schedule

#importing the time extractor so we can use that logic in our class
import timeExtractor


#This class is used to store the content and it is also the parent class of the time class
class FileContent:

    def __init__(self, content):
        self.content = content
        self.timeIntervals = []
        self.indivdualTimes = []
        self.keyword = ""
        self.keywords = []

    #           Setters             #
    #This is our setter function for setting the content of the file
    def setContent(self, content):
        self.content = content

    #This is our setter function for setting the keyword of the file
    def setKeyword(self, keyword):
        self.keyword = keyword

    #This function is used to add a time interval to the timeIntervals list
    def addTimeInterval(self, timeInterval):
        

        self.timeIntervals.append(timeInterval)
    
    #This function is used to add a keyword to the keywords list
    #This is a just incase function if mulitple keywords pop up
    def addKeywords(self, keyword):
        self.keywords.append(keyword)

    #####
    #####
    #This function is used to add a time to the indivdualTimes list from a time interval
    def addIndivdualTime(self, timeInterval):
        time = ""
        #Add some logic here to get an induvdual time from a time interval
        self.indivdualTimes.append(time)

    #           Getters             #
    #This is our getter function for the content of the file
    def getContent(self):
        return self.content
    
    #This is our getter function for the timeIntervals list
    def getTimeIntervals(self):
        return self.timeIntervals

    def getKeyword(self):
        return self.keyword
    
    def getKeywords(self):
        return self.keywords
    
    #This function is used to print the content
    #We just have to use print(fileContent) to print the content
    def __str__(self):
        return self.content
    