#This is the Employee class


class Employee:
    class Availability:
        class Day:
            #Day Constructor
            def __init__(self, day, start, end):
            	self.day = day
            	self.start = start
            	self.end = end

            #Getters and Setters for Day class
            def getDay(self):
            	return self.day
            def setStart(self, start):
                self.start = start
                
            def setEnd(self, end):
                self.end = end
                
            def getStart(self):
                return self.start
                
            def getEnd(self):
                return self.end

        #Availabiltiy Constructor        
        def __init__(self):
            self.Monday = self.Day("Monday",0, 0)
            self.Tuesday = self.Day("Tuesday", 0, 0)
            self.Wednesday = self.Day("Wednesday", 0, 0)
            self.Thursday = self.Day("Thursday", 0, 0)
            self.Friday = self.Day("Friday", 0, 0)
            self.Saturday = self.Day("Saturday", 0, 0)
            self.Sunday = self.Day("Sunday",0, 0)

            self.days = [self.Monday, self.Tuesday, self.Wednesday, self.Thursday, self.Friday, self.Saturday, self.Sunday]

        #Getters and Setters for Availabiliy class
        def getDayOfWeek(self, day):
        	return self.days[day].getDay()

        def printAvailability(self, day):
            day_name = self.days[day].getDay()
            start_time = self.days[day].getStart()
            end_time = self.days[day].getEnd()
            
            if (day == 0 or day == 4):
                print(day_name + ":\t\t" + str(start_time)+"-"+str(end_time))
            else:
                print(day_name + ":\t" + str(start_time)+"-"+str(end_time))


        def setAvailability(self, i, start, end):
            self.days[i].setStart(start)
            self.days[i].setEnd(end)

    #Employee Constructor
    def __init__(self, name, seniority, status):
        self.name = name
        self.seniority = seniority
        self.status = status

    #private vairables
    __availability = Availability()

    #Getter and Setter for Employee

    def setAvail(self):
        for i in range(0, 6):
        	print("Set starting time for " + self.__availability.getDayOfWeek(i))
        	start = input()
        	print("Set ending time for " + self.__availability.getDayOfWeek(i))
        	end = input()
        	self.__availability.setAvailability(i, start, end)

    def getAvail(self):
    	for i in range(0,6):
    		self.__availability.printAvailability(i)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSeniority(self):
        return self.seniority

    def setseniority(self, seniority):
        self.seniority = seniority

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

#Emiliano = Employee("Eminiano", 5, "full")


#Emiliano.setAvail()
#Emiliano.getAvail()






