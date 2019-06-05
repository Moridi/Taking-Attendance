class Exam():
    def __init__(self, examId, roomNumber, startAt, endAt):
        self.examId = examId
        self.roomNumber = roomNumber
        self.startAt = startAt
        self.endAt = endAt

    def setCourse(self, course):
        self.course = course