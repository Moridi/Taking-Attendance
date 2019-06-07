from EducationSystem import EducationSystem


class CommandHandler():
    __instance = None

    @staticmethod
    def getInstance():
        if CommandHandler.__instance is None:
            CommandHandler()
        return CommandHandler.__instance

    def __init__(self):
        if CommandHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CommandHandler.__instance = self

    def getExamId(self):
        educationSystem = EducationSystem.getInstance()
        print("Enter your demanded ExamId:")

        input_res = input()
        return input_res
    
    def getStudentId(self):
        print("Enter studentId:")

        input_res = input()
        return input_res

    def getExams(self):
        input_res = input()
        return input_res

    def getTeacherSignStatus(self):
        print("Is it teacher signed?[Y/N]")
        input_res = input()
        if input_res == "Y" or input_res == "y":
            return "true"
        return "false"
