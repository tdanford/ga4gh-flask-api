
from ga4gh_models import * 

# 
# GASearchCallSetsRequest
# 

class GASearchCallSetsRequest(object):
    def __init__(self, variantSetIds, name, pageSize, pageToken):
        self.variantSetIds = variantSetIds
        self.name = name
        self.pageSize = pageSize
        self.pageToken = pageToken

def decode_GASearchCallSetsRequest(str):
    return JSONDecoder(object_hook = GASearchCallSetsRequest_from_json).decode(str)

def GASearchCallSetsRequest_from_json(json_object):
    return GASearchCallSetsRequest(variantSetIds=json_object['variantSetIds'], 
                                   name=json_object['name'],
                                   pageSize=json_object['pageSize'],
                                   pageToken=json_object['pageToken'])

# 
# GASearchCallSetsResponse
# 

class GASearchCallsetsResponse(object):
    def __init__(self, callsets, nextPageToken):
        self.callsets = callsets
        self.nextPageToken = nextPageToken

