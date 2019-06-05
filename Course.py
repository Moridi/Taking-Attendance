class Course():
    def __init__(self, courseName, professor):
        self.courseName = courseName
        self.professor = professor
        self.students = []

    def getCourseName(self):
        return self.courseName

    def addStudent(self, newStudent):
        self.students.append(newStudent)