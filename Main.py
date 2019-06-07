from EducationSystem import EducationSystem
from CommandHandler import CommandHandler
from HttpHandler import HttpHandler


current_exam_id = None

if __name__ == "__main__":
    educationSystem = EducationSystem.getInstance()
    educationSystem.initializeSystem()


    while True:
        exam_id = None
        if CommandHandler.getInstance().getExams() == "get_exams":
        	educationSystem.printExams()

        while True:
            exam_id = CommandHandler.getInstance().getExamId()
            if educationSystem.examIdIsValid(exam_id) or exam_id == "done":
                break
        
        if exam_id == "done":
            break

        students_list = []
        while True:
            student_id = CommandHandler.getInstance().getStudentId()
            if student_id == "done":
                break
            if educationSystem.studentIsInExam(exam_id, student_id):
                students_list.append(int(student_id))
            else:
                print("given student_id not found")

        is_teacher_signed = CommandHandler.getInstance().getTeacherSignStatus()
        httpHandler = HttpHandler.getInstance()
        httpHandler.postAttendanceResult(
            data={
                "exam_id": int(exam_id),
                "is_teacher_signed": is_teacher_signed,
                "present_students_list": students_list
            })
