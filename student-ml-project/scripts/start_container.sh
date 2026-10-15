#!/bin/bash
cd /home/ubuntu/student-ml-project
docker build -t student-app .
docker run -d --name student-app -p 80:5000 student-app
