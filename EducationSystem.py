from HttpHandler import HttpHandler
from Course import Course
from Exam import Exam

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

   def setExam(self, examElement):
      
      newExam = Exam(examElement["exam_id"], \
            examElement["room_number"], \
            examElement["start_at"], \
            examElement["end_at"])

   def setExams(self):
      jsonExams = self.attendanceList["classes"]
      for index, examElement in enumerate(jsonExams):
         self.setExam(examElement)