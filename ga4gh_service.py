#!/usr/bin/env python

# flask-specific imports
from flask import Flask, request

from service_models import * 

# ga4gh-specific imports
from json_models import * 

app = Flask(__name__)

@app.route('/callsets/search', methods=['POST'])
def hello_world():
    callsets_request = GASearchCallSetsRequest_from_json(request.get_json())
    return callsets_response()

if __name__ == '__main__':
    app.run()
