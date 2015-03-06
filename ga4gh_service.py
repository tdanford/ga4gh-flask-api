#!/usr/bin/env python

# flask-specific imports
from flask import Flask, request

from service_models import * 

# ga4gh-specific imports
from json_models import * 

app = Flask(__name__)

@app.route('/callsets/search', methods=['POST'])
def search_callsets():
    callsets_request = GASearchCallSetsRequest_from_json(request.get_json())
    return callsets_response()

@app.route('/variants/search', methods=['POST'])
def search_variants():
    pass

@app.route('/variantsets/search', methods=['POST'])
def search_variant_sets():
    pass

if __name__ == '__main__':
    app.run()
