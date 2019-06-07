class Exam():
    def __init__(self, examId, roomNumber,\
            startAt, endAt, courseName, professorId):
        self.examId = examId
        self.roomNumber = roomNumber
        self.startAt = startAt
        self.endAt = endAt
        self.courseName = courseName
        self.professorId = professorId
        self.students = []

    def addStudent(self, newStudent):
        self.students.append(newStudent)

    def getId(self):
        return self.examId

    def printStudents(self):
        SID = 0
        for student in self.students:
            print(student[SID])
