from HttpHandler import HttpHandler
from Exam import Exam
from Professor import Professor
from Student import Student
from Students import Students

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
         self.exams = []
         self.students = Students()

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
      return professor

   def setStudent(self, studentElement):
      student = Student(studentElement["first_name"],\
            studentElement["last_name"],\
            studentElement["id"])
      
      self.students.addStudent(student)
            # studentElement["chair_number"])
      return student.getId()

   def setExam(self, examElement):

      professor = self.setProfessor(examElement["professor"])

      exam = Exam(examElement["exam_id"], \
            examElement["room_number"], \
            examElement["start_at"], \
            examElement["end_at"],\
            examElement["course_name"],\
            professor)

      jsonStudents = examElement["students"]

      for index, studentElement in enumerate(jsonStudents):
         studentId = self.setStudent(studentElement)
         exam.addStudent(studentId)
      
      return exam

   def setExams(self):
      jsonExams = self.attendanceList["classes"]
      for index, examElement in enumerate(jsonExams):
         exam = self.setExam(examElement)
         self.exams.append(exam)

   def printDatabase(self):
      print("status:" + str(self.status))
      print("date:" + str(self.date))
      print("classes:")
      for exam in self.exams:
         print("******")
         print("examId:" + str(exam.examId))
         print("roomNumber:" + str(exam.roomNumber))
         print("startAt:" + str(exam.startAt))
         print("endAt:" + str(exam.endAt))
         print("courseName:" + exam.courseName)
         print("professor.firstName:" + exam.professor.firstName)
         print("professor.lastName:" + exam.professor.lastName)
         print("professor.id:" + exam.professor.id)
         print()

      print("Students:")
      for studentId in self.students.students:
         print("######")
         print("student.firstName:" + str(self.students.students[studentId].firstName))
         print("student.lastName:" + str(self.students.students[studentId].lastName))
         print("student.id:" + str(self.students.students[studentId].id))
         # print("student.chairNumber:" + str(student.chairNumber))
      print("$$$$$")

   
   def printExams(self):
      print("status:" + str(self.status))
      print("date:" + str(self.date))
      for exam in self.exams:
         print("******")
         print("examId:" + str(exam.examId))
         print("roomNumber:" + str(exam.roomNumber))
         print("courseName:" + exam.courseName)
         print("professor.firstName:" + exam.professor.firstName)
         print("professor.lastName:" + exam.professor.lastName)
         print("professor.id:" + exam.professor.id)
         print()

   def examIdIsValid(self, exam_id):
      for exam in self.exams:
         if str(exam.examId) == exam_id:
            return True

      return False

   def studentIsInExam(self, exam_id, student_id):
      current_exam = None

      for exam in self.exams:
         if str(exam.examId) == exam_id:
            current_exam = exam
            break
         
      if current_exam is None:
         return False

      for student in self.students.students:
         if str(student.id) == student_id:
            return True


      return False
      
