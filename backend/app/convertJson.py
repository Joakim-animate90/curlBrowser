import json
import re
class ConvertJson(object):
    def __init__(self, headers, body):
        self.headers = headers
        self.body = body
        self.jsonObject = {}
        
    def extract_status_code(self, string):
        pattern = r'^HTTP/\d+\s+(\d+)\s+'
        match = re.match(pattern, string)

        if match:
            status_code = match.group(1)
            return int(status_code)
        else:
            return None 

    def splitLines(self, string):
        return string.splitlines()
    
    def detectColon(self, string):
        parts = string.split(":", 1)  
        if len(parts) == 2:
            key = parts[0].strip() 
            value = parts[1].strip() 
            return key, value
        else:
            return None, None 


    def getHeaders(self):
        print("PRINT  SELF HEADERS: f'{self.headers}'")
        self.jsonObject["status_code"] = self.extract_status_code(self.headers)
        
        for header in self.splitLines(self.headers):
            key, value = self.detectColon(header)
            self.jsonObject[key] = value
        self.jsonObject["body"] = self.body
        return self.jsonObject
    

    def getPrettyJSON(self):
        return json.dumps(self.jsonObject, indent=4)
