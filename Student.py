from Human import Human

class Student(Human):
    def __init__(self, firstName, lastName, id, chairNumber):
        super.__init__(firstName, lastName, id)
        self.chairNumber = chairNumber