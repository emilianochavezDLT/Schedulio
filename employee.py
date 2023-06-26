class Car:
    def __init__(self, ID, name, context, statues, availability, payRate):
        self.ID = ID
        self.name = name
        self.context = context
        self.statues = statues
        self.availability = availability
        self.payRate = payRate

    # getters
    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_context(self):
        return self.context

    def get_statues(self):
        return self.statues

    def get_availability(self):
        return self.availability

    def get_payRate(self):
        return self.payRate

    # setters
    def set_ID(self, ID):
        self.ID = ID

    def get_name(self, name):
        self.name = name

    def get_context(self, context):
        self.context = context

    def get_statues(self, statues):
        self.statues = statues

    def get_availability(self, availability):
        self.availability = availability

    def get_payRate(self, payRate):
        self.payRate = payRate
