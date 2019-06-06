import requests
import json

class HttpHandler():
    __instance = None
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


    @staticmethod
    def getInstance():
        if HttpHandler.__instance == None:
            HttpHandler()
        return HttpHandler.__instance

    def __init__(self):
        if HttpHandler.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            HttpHandler.__instance = self
            self.url = "http://142.93.134.194:8088/api/attendance"
            self.send_buffer = []
        
    def getAttendanceList(self):
        exams = requests.get(url = self.url) 
        return exams.json()

    def postAttendanceResult(self, data):
        payload = json.dumps(data)
        self.send_buffer.append(payload)

        send_idx = 0
        while send_idx < len(self.send_buffer):
            try:
                response = requests.post(url=self.url, data=self.send_buffer[send_idx], headers=self.headers, timeout=2)
                if response.status_code >= 200 and response.status_code < 300:
                    self.send_buffer.pop(send_idx)
                    print("Post Success")
                else:
                    send_idx += 1
                    print("Post : something bad!")

            except requests.exceptions.RequestException:
                print("Post Failed")
                break
