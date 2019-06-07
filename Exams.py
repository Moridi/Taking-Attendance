class Exams():
    def __init__(self):
        self.exams = {}

    def addExam(self, exam, examId):
        if (examId in self.exams):
            pass
        else:
            self.exams[examId] = exam

    def printExam(self, examId):
        self.exams[examId].printStudents()
            