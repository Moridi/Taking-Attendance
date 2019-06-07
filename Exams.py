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

    def printExams(self):
        for exam in self.exams.values():
            print("******")
            print("examId:" + str(exam.examId))
            print("roomNumber:" + str(exam.roomNumber))
            print("courseName:" + exam.courseName)
            print("professor.id:" + exam.professorId)
