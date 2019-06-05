import requests 

def HttpHandler():
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if HttpHandler.__instance == None:
            HttpHandler()
        return HttpHandler.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if HttpHandler.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            HttpHandler.__instance = self
            self.url = "http://142.93.134.194:8088/api/attendance"
        
    def getExams(self):
        exams = requests.get(url = self.url) 
        return exams.json()

    def postAttendanceResult(self, data):
        response = requests.post(url = self.url, data = data) 
        
        pastebin_url = response.text
        print("Response: %s"%pastebin_url)