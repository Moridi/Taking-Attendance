from Human import Human

class Student(Human):
    def __init__(self, firstName, lastName, id, chairNumber):
        Human.__init__(self, firstName, lastName, id)
        self.chairNumber = chairNumber