import os
import socket
from flask import Flask, Response, request
from flask_api import status
import ifaddr

#Create an instance of the Flask class for the website
app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return f'Hello World! Running on container ID: {hostname}\n'

#Function for load balancer health check
@app.route('/health-check')
def health():
    return ('', status.HTTP_204_NO_CONTENT)

#Function for inspecting http headers
@app.route('/headers')
def headers():
    result = ""
    for header in request.headers:
        result = result + f'{header[0]}:\t{header[1]}\n'
    return Response(result, mimetype='text/plain')

#Function for displaying IP addressing
@app.route('/ips')
def ips():
    result = ""
    for adapter in ifaddr.get_adapters():
        result = result + f'IP addressing of network adapter {adapter.nice_name}\n'
        for ip in adapter.ips:
            result = result + f'  - {ip.ip}/{ip.network_prefix}\n'
    return Response(result, mimetype='text/plain')

#Function for displaying OS environment variables
@app.route('/env')
def environment():
    result = ""
    for env in os.environ:
        result = result + f'{env}: {os.environ.get(env)}\n'
    return Response(result, mimetype='text/plain')

#Function for stopping the website.
@app.route('/stop')
def crash():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return Response("Stopping server...\n", mimetype='text/plain')

#Main function to listen on any IP and use port from MY_PORT environment variable or default to 80
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=float(os.getenv('MY_PORT', '80')))
#app.run(host='0.0.0.0', port=float(os.getenv('MY_PORT', '80')), debug=True)
