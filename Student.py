from Human import Human

class Student(Human):
    def __init__(self, firstName, lastName, id):
        Human.__init__(self, firstName, lastName, id)