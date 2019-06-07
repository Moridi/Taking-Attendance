from CommandHandler import CommandHandler
from EducationSystem import EducationSystem
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
        # self.educationSystem.printDatabase()
        while True:
            self.getExams()
            self.getExamStudentsList()
            exam_id = self.getExam()
            if exam_id == "done":
                break
            is_teacher_signed, students_list =  self.getStudents(exam_id)
            self.sendResult(exam_id, is_teacher_signed, students_list)

    def getExams(self):
        if self.commandHandler.getExams() == "get_exams":
            self.educationSystem.printExams()

    def getExam(self):
        while True:
            exam_id = self.commandHandler.getExamId()
            if self.educationSystem.examIdIsValid(exam_id) or exam_id == "done":
                break

        return exam_id

    def getStudents(self, exam_id):
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
        return is_teacher_signed, students_list

    def sendResult(self, exam_id, is_teacher_signed, students_list):
        http_handler = HttpHandler.getInstance()
        http_handler.postAttendanceResult(
            data={
                "exam_id": int(exam_id),
                "is_teacher_signed": is_teacher_signed,
                "present_students_list": students_list
            })
    def getExamStudentsList(self):
        command, exam_id = self.commandHandler.getExamsStudentsList()
        while command == "get_students":
            self.educationSystem.printExam(exam_id)
            command, exam_id = self.commandHandler.getExamsStudentsList()
