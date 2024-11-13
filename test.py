# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify

import logging


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/', methods=['POST'])
def dump_request():
    logging.basicConfig(level=logging.DEBUG)
    headers = request.headers
    body = request.get_data()
    logging.debug("Headers of incoming request:")
    logging.debug(headers)
    logging.debug("Body of incoming request:")
    logging.debug(body)
    return jsonify({"message":"log accepted"})

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()