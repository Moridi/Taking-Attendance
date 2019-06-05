class AttendanceBody():
    def __init__(self, examId):
        self.examId = examId
        self.isTeacherSigned = False
        self.presentStudentsList = []
    
    def addStudent(self, newId):
        self.presentStudentsList.append(newId)
    
    def teacherSigned(self):
        self.isTeacherSigned = True
    
    def getFormattedExamId(self):
        return "exam_id:" + str(self.examId) + ",\n"

    def getFormattedIsTeacherSigned(self):
        return "is_teacher_signed:\"" + \
                str(self.isTeacherSigned).lower() + ",\n"

    def getFormattedPresentStudentsList(self):
        return "is_teacher_signed:\"" + \
                str(self.presentStudentsList) + "\n"

    def getAttendanceBody(self):
        return "{\n" +\
                    self.getFormattedExamId() +\
                    self.getFormattedIsTeacherSigned() +\
                    self.getFormattedPresentStudentsList +\
                "}"