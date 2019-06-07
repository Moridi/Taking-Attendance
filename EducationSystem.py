from HttpHandler import HttpHandler
from Exam import Exam
from Professor import Professor
from Professors import Professors
from Student import Student
from Students import Students
from Exams import Exams

class EducationSystem(object):
   __instance = None
   @staticmethod 
   def getInstance():
      if EducationSystem.__instance == None:
         EducationSystem()
      return EducationSystem.__instance

   def __init__(self):
      if EducationSystem.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         EducationSystem.__instance = self
         self.exams = Exams()
         self.students = Students()
         self.professors = Professors()

   def initializeSystem(self):
      self.getAttendanceList()
      self.setStatus()
      self.setDate()
      self.setExams()

   def getAttendanceList(self):
      httpHandler = HttpHandler.getInstance()
      self.attendanceList = httpHandler.getAttendanceList()

   def setStatus(self):
      self.status = self.attendanceList["status"]

   def setDate(self):
      self.date = self.attendanceList["date"]

   def setProfessor(self, professorElement):
      professor = Professor(professorElement["first_name"], \
            professorElement["last_name"], \
            professorElement["id"])
      
      self.professors.addProfessor(professor)
      return professor.getId()

   def setStudent(self, studentElement):
      student = Student(studentElement["first_name"],\
            studentElement["last_name"],\
            studentElement["id"])
      
      self.students.addStudent(student)
      return (student.getId(), \
            studentElement["chair_number"])

   def setExam(self, examElement):

      professorId = self.setProfessor(examElement["professor"])

      exam = Exam(examElement["exam_id"], \
            examElement["room_number"], \
            examElement["start_at"], \
            examElement["end_at"],\
            examElement["course_name"],\
            professorId)

      jsonStudents = examElement["students"]

      for index, studentElement in enumerate(jsonStudents):
         student = self.setStudent(studentElement)
         exam.addStudent(student)
      
      return exam

   def setExams(self):
      jsonExams = self.attendanceList["classes"]
      for index, examElement in enumerate(jsonExams):
         exam = self.setExam(examElement)
         self.exams.addExam(exam)

   def printDatabase(self):
      print("status:" + str(self.status))
      print("date:" + str(self.date))
      print("classes:")
      for exam in self.exams.exams:
         print("******")
         print("examId:" + str(exam.examId))
         print("roomNumber:" + str(exam.roomNumber))
         print("startAt:" + str(exam.startAt))
         print("endAt:" + str(exam.endAt))
         print("courseName:" + exam.courseName)
         print("professor.firstName:" + self.professors.professors[exam.professorId].firstName)
         print("professor.lastName:" + self.professors.professors[exam.professorId].lastName)
         print("professor.id:" + self.professors.professors[exam.professorId].id)
         print()
         print("Students:")
         for student in exam.students:
            print("######")
            print("student.firstName:" + str(self.students.students[student[0]].firstName))
            print("student.lastName:" + str(self.students.students[student[0]].lastName))
            print("student.id:" + str(self.students.students[student[0]].id))
            print("student.chairNumber:" + str(student[1]))
         print("$$$$$")

   def printExams(self):
      print("status:" + str(self.status))
      print("date:" + str(self.date))
      for exam in self.exams.exams:
         print("******")
         print("examId:" + str(exam.examId))
         print("roomNumber:" + str(exam.roomNumber))
         print("courseName:" + exam.courseName)
         print("professor.firstName:" + self.pro[exam.professorId].firstName)
         print("professor.lastName:" + self.pro[exam.professorId].lastName)
         print("professor.id:" + self.pro[exam.professorId].id)
         print()

   def examIdIsValid(self, exam_id):
      for exam in self.exams.exams:
         if str(exam.examId) == exam_id:
            return True

      return False

   def studentIsInExam(self, exam_id, student_id):
      current_exam = None

      for exam in self.exams.exams:
         if str(exam.examId) == exam_id:
            current_exam = exam
            break
         
      if current_exam is None:
         return False

      for student in self.students.students:
         if str(student.id) == student_id:
            return True


      return False
      
