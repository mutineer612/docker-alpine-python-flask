#Use the Python base image with Alpine Linux
FROM python:alpine

#Set a default directory for application install
WORKDIR /usr/src/app

#Upgrade pip
RUN pip install --upgrade pip

#Install python modules and don't cache install files to save space
RUN pip install --no-cache-dir flask flask-api ifaddr

#Copy the application to the working directory
COPY flask-website.py ./

#Start the website
CMD [ "python", "flask-website.py"]
