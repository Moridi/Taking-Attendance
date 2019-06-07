class Exam():
    def __init__(self, examId, roomNumber,\
            startAt, endAt, courseName, professorId):
        self.examId = examId
        self.roomNumber = roomNumber
        self.startAt = startAt
        self.endAt = endAt
        self.courseName = courseName
        self.professorId = professorId
        self.studentIds = []

    def addStudent(self, newStudent):
        self.studentIds.append(newStudent)