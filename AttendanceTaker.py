from EducationSystem import EducationSystem
from CommandHandler import CommandHandler
from HttpHandler import HttpHandler

class AttendanceTaker():
    __instance = None
    @staticmethod 
    def getInstance():
        if AttendanceTaker.__instance == None:
            AttendanceTaker()
        return AttendanceTaker.__instance

    def __init__(self):
        if AttendanceTaker.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AttendanceTaker.__instance = self
        self.educationSystem = EducationSystem.getInstance()
        self.educationSystem.initializeSystem()
        self.commandHandler = CommandHandler.getInstance()

    def run(self):
        
        while True:
            exam_id = None
            if self.commandHandler.getExams() == "get_exams":
                self.educationSystem.printExams()

            while True:
                exam_id = self.commandHandler.getExamId()
                if self.educationSystem.examIdIsValid(exam_id) or exam_id == "done":
                    break
            
            if exam_id == "done":
                break

            students_list = []
            while True:
                student_id = self.commandHandler.getStudentId()
                if student_id == "done":
                    break
                if self.educationSystem.studentIsInExam(exam_id, student_id):
                    students_list.append(int(student_id))
                else:
                    print("given student_id not found")

            is_teacher_signed = self.commandHandler.getTeacherSignStatus()
            httpHandler = HttpHandler.getInstance()
            httpHandler.postAttendanceResult(
                data={
                    "exam_id": int(exam_id),
                    "is_teacher_signed": is_teacher_signed,
                    "present_students_list": students_list
                })
