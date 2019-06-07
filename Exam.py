class Exam():
    def __init__(self, examId, roomNumber,\
            startAt, endAt, courseName, professor):
        self.examId = examId
        self.roomNumber = roomNumber
        self.startAt = startAt
        self.endAt = endAt
        self.courseName = courseName
        self.professor = professor
        self.students = []

    def addStudent(self, newStudent):
        self.students.append(newStudent)