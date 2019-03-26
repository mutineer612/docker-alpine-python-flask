# docker-alpine-python-flask
This Dockerfile creates a simple container for running Python and Flask using the latest Alpine base, and copies a flask-website.py file into the working directory.  The python script enables simple access for http header info, IP addressing and environment variables for testing load balancing, container failure, and orchestration.   

## Usage
Build the container image from current directory and publish to docker hub.
1. `docker build -t mutineer612/flask-website .`  
2. `docker push mutineer612/flask-website`

* The Dockerfile does not expose a specific port enabling change without rebuilding the container. 

Run the container locally passing the MY_PORT environment variable to the flask-website.py script.  With MacOS and Windows need to use the -p switch and map the port to the container.  With Linux you can optionally use the 'host' network driver.    
- ```docker run -e MY_PORT=8888 -p 8888:8888 --rm --name flask mutineer612/flask-website```

* By running the container and remaining attached to the console you can see the http requests/responses
 
## Site Navigation
The flask-website.py script creates the following URL's
1. `/` Displays 'Hello World! Running on container ID: {hostname}'
2. `/health-check` Is an empty directory that returns HTTP_204 to satisfy load balancing health checks
3. `/headers` Returns http header content showing client IP, browser, and OS 
4. `/ips`  Returns a list of container and host IP addresses by interface
5. `/env` Returns a list of the containers environment variables
6. `/stop` Executes a function call to shutdown the Werkzeug Server (i.e. Flask Development Web Server)

* Navigating to /stop will stop the container.  This is a function of the built in dev Flask web server.
##
Based on original work located here: https://github.com/yafernandes
