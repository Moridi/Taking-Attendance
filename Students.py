from Student import Student

class Students():
    def __init__(self):
        self.students = {}

    def addStudent(self, student):
        if (student.getId() in self.students):
            pass
        else:
            self.students[student.getId()] = student
        