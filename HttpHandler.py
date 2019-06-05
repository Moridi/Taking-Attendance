import requests 

def HttpHandler():
    def __init__(self):
        self.url = "http://142.93.134.194:8088/api/attendance"
    
    def getExams(self):
        exams = requests.get(url = self.url) 
        return exams.json()

    def postAttendanceResult(self, data):
        response = requests.post(url = self.url, data = data) 
        
        # extracting response text  
        pastebin_url = response.text
        print("The pastebin URL is:%s"%pastebin_url)