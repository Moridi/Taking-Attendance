from Professor import Professor

class Professors():
    def __init__(self):
        self.professors = {}

    def addProfessor(self, Professor):
        if (Professor.getId() in self.professors):
            pass
        else:
            self.professors[Professor.getId()] = Professor
        