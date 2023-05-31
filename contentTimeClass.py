#This is the content and time class for the Schedulio program
#This class is used to store the content and time of the schedule

#importing the time extractor so we can use that logic in our class
import timeExtractor


#This class is used to store the content and it is also the parent class of the time class
class File_Content:

    def __init__(self, content):

    #       Attributes              #
        self.content = content
        self.time_Intervals = []
        self.individual_Times = []
        self.keyword = ""
        self.keywords = []

    #           Setters             #
    #This is our setter function for setting the content of the file
    def set_Content(self, content):
        self.content = content

    #           Getters             #
    # The Getters will have logic tied to them and assigined to 
    # the appropiate attributes. 

    #This is our getter function for the content of the file
    def get_Content(self):

        #Returns the content in its string form
        return self.content
    
    #This is our getter function for the time_Intervals list
    def get_Time_Intervals(self):

        #Calling the time extractor to get the time intervals
        times_found = timeExtractor.extract_time_ranges(self.content)
        
        # A for loop needed to go through the list
        for time_Intervals_Found in times_found:
            
            # Append those times into the array
            self.time_Intervals.append(time_Intervals_Found)
    
        # Returning the array/list
        return self.time_Intervals
    

    # This is function for returning the indivdual times 
    # from the time intervals.
    def get_individual_times(self):

        # Raising an error to make sure that 
        # individual times is intilized first     
        if not self.individual_Times:
            raise ValueError("This is an empty array. Please initialize it before calling get_individual_times method")

        # This will continue to execute the rest of the function as normal
        try:
            # Calling the time extractor to get the time intervals
            times_found = timeExtractor.extract_time_ranges(self.content)

            # A for loop to iterate through the time intervals
            for time_interval in times_found:
                parts = time_interval.split('-')
                self.individual_Times.extend(part.strip() for part in parts)

            return self.individual_Times
        
        # Prints the error to the person who's coding with this class
        except ValueError as e:
            print("Error:", str(e))

    def get_Keyword(self):
        return self.keyword
    
    def get_Keywords(self):
        return self.keywords
    
    #This function is used to print the content
    #We just have to use print(fileContent) to print the content
    def __str__(self):
        return self.content
    