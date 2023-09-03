# curl Browser ![Chrome](https://raw.githubusercontent.com/alrra/browser-logos/main/src/chrome/chrome_24x24.png "Chrome") 
#### Description:

Welcome to the cURL Browser Impersonator project! This specialized build of  [curl](https://github.com/curl/curl) that  aims to mimic the behavior of major web browsers, such as Chrome, during TLS and HTTP handshakes.This version of cURL is wrapped in Python, allowing you to conveniently test and interact with it in a browser environment while capturing and analyzing responses.

### Key Features

- **Browser Emulation:** This custom cURL build replicates the TLS and HTTP handshake behaviors of popular web browsers, providing an invaluable tool for studying web communication protocols and security measures.
  
  [Learn more](https://www.browserling.com/browser-emulator-simulator)

- **Python Integration:** By wrapping cURL in Python, you can easily create scripts and applications to test web services, APIs, and websites while leveraging the power and flexibility of Python for analysis and automation.

- **Browser Testing:** Emulate user agent strings, request headers, and other browser-specific settings to test how web servers and applications respond to different client behaviors.

- **Capture and Analyze Responses:** With Python integration, you can capture and analyze HTTP responses, enabling detailed examination of web interactions and debugging.

  ![Capture and Analyze Responses](https://example.com/capture-analyze.png)
  


### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/flask)

### Python/Flask application

Project structure:
```
.
├── compose.yaml
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
    
```

[_compose.yaml_](compose.yaml)
```
services: 
  web: 
    build:
     context: app
     target: builder
    ports: 
      - '8000:8000'
```

## Deploy with docker compose

```
$ docker compose up -d
[+] Building 1.1s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                                       0.0s
    ...                                                                                                                                         0.0s
 => => naming to docker.io/library/flask_web                                                                                                                                                                                               0.0s
[+] Running 2/2
 ⠿ Network flask_default  Created                                                                                                                                                                                                          0.0s
 ⠿ Container flask-web-1  Started
```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker compose ps
NAME                COMMAND             SERVICE             STATUS              PORTS
flask-web-1         "python3 app.py"    web                 running             0.0.0.0:8000->8000/tcp
```

After the application starts, navigate to `http://localhost:8000` in your web browser or run:
```
$ curl localhost:8000
Hello World!
```

Stop and remove the containers
```
$ docker compose down
```
