from HttpHandler import HttpHandler
from Course import Course
from Exam import Exam
from Professor import Professor
from Student import Student

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
            studentElement["id"],\
            studentElement["chair_number"])
      return student

   def setCourse(self, exam):
      professor = self.setProfessor(exam["professor"])
      course = Course(exam["course_name"], professor)

      jsonStudents = exam["students"]

      for index, studentElement in enumerate(jsonStudents):
         student = self.setStudent(studentElement)
         course.addStudent(student)
      
      return course

   def setExam(self, examElement):
      exam = Exam(examElement["exam_id"], \
            examElement["room_number"], \
            examElement["start_at"], \
            examElement["end_at"])
   
      course = self.setCourse(examElement)
      exam.setCourse(course)

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
         print("courseName:" + exam.course.courseName)
         print("professor.firstName:" + exam.course.professor.firstName)
         print("professor.lastName:" + exam.course.professor.lastName)
         print("professor.id:" + exam.course.professor.id)
         print()
         print("Students:")
         for student in exam.course.students:
            print("######")
            print("student.firstName:" + str(student.firstName))
            print("student.lastName:" + str(student.lastName))
            print("student.id:" + str(student.id))
            print("student.chairNumber:" + str(student.chairNumber))
         print("$$$$$")
