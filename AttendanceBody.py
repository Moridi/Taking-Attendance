class AttendanceBody():
    def __init__(self, examId):
        self.examId = examId
        self.isTeacherSigned = False
        self.presentStudentsList = []
    
    def addStudent(self, newId):
        self.presentStudentsList.append(newId)
    
    def teacherSigned(self):
        self.isTeacherSigned = True

    def getAttendanceBody(self):
        return {
            "exam_id" : self.examId,
            "is_teacher_signed" : str(self.isTeacherSigned).lower(),
            "present_students_list" : str(self.presentStudentsList)
        }