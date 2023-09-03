import subprocess
import concurrent.futures

class FetchCurl(object):
    def __init__(self, url):
        self.url = url
        self.commandToGetHeaders = [
            "docker", "run", "--rm", "--privileged",
            "-v", "/var/run/docker.sock:/var/run/docker.sock",
            "lwthiker/curl-impersonate:0.5-chrome",
            "curl_chrome110", "-IsS", self.url
        ]
        self.commandToGetBody = [
            "docker", "run", "--rm", "--privileged",
            "-v", "/var/run/docker.sock:/var/run/docker.sock",
            "lwthiker/curl-impersonate:0.5-chrome",
            "curl_chrome110","-sS", self.url
        ]

    def execute_command(self, command):
        try:
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
            return result
        except subprocess.CalledProcessError as e:
            return e.output

    def getHeaders(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            header_result = executor.submit(self.execute_command, self.commandToGetHeaders)
            body_result = executor.submit(self.execute_command, self.commandToGetBody)

            # Wait for both tasks to complete
            header_result = header_result.result()
            body_result = body_result.result()

        #return a list
        return [header_result, body_result]


            
    

   