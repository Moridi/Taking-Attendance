class EducationSystem(object):
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if EducationSystem.__instance == None:
         EducationSystem()
      return EducationSystem.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if EducationSystem.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         EducationSystem.__instance = self