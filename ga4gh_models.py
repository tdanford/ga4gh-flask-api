
# 
# GAReference
# 

class GAReference(object):
    def __init__(self, id, length, md5checksum, name, sourceURI, sourceAccessions, 
                 isDerived, sourceDivergence, ncbiTaxonId):
        self.id = id
        self.length = length
        self.md5checksum = md5checksum
        self.name = name
        self.sourceAccessions = sourceAccessions
        self.isDerived = isDerived
        self.sourceDivergence = sourceDivergence
        self.ncbiTaxonId = ncbiTaxonId

def GAReference_from_json(json_object):
    return GAReference(id=json_object['id'], 
                       length=json_object['length'],
                       md5checksum=json_object['md5checksum'],
                       name=json_object['name'],
                       sourceURI=json_object['sourceURI'],
                       sourceAccessions=json_object['sourceAccessions'],
                       isDerived=json_object['isDerived'],
                       sourceDivergence=json_object['sourceDivergence'],
                       ncbiTaxonId=json_object['ncbiTaxonId'])

def decode_GAReference(json_string):
    return JSONDecoder(object_hook=GAReference_from_json).decode(json_str)

#
# GACallSet
#
# Reference: 
#  http://ga4gh.org/documentation/api/v0.5.1/ga4gh_api.html#/schema/%2FUsers%2Fkeenan%2FDropbox%2Fgit-checkouts%2Fschemas%2Fsrc%2Fmain%2Fresources%2Favro%2Ftarget%2Fall.avpr/org.ga4gh.GACallSet
# 

class GACallSet(object):
    def __init__(self, id, name, sampleId, variantSetIds, created, updated, info):
        self.id = id
        self.name = name
        self.sampleId = sampleId
        self.variantSetIds = variantSetIds 
        self.created = created
        self.updated = updated
        self.info = info

def GACallSet_from_json(json_object):
    return GACallSet(id=json_object['id'],
                     name=json_object['name'],
                     sampleId=json_object['sampleId'],
                     variantSetIds=json_object['variantSetIds'],
                     created=json_object['created'],
                     updated=json_object['updated'],
                     info=json_object['info'])

def decode_GACallSet(json_str):
    return JSONDecoder(object_hook=GACallSet_from_json).decode(json_str)

#
# GAVariant 
# 

class GAVariant(object):
    def __init__(self, id, variantSetId, names, created, updated, referenceName, start, end, referenceBases, 
                 alternateBases, info, calls):
        self.id = id
        self.variantSetId = variantSetId
        self.names = names
        self.created = created
        self.updated = updated
        self.referenceName = referenceName
        self.start = start
        self.end = end
        self.referenceBases = referenceBases
        self.alternateBases = alternateBases
        self.info = info
        self.calls = calls

# 
# 
# GAVariantSet
# 

class GAVariantSet(object):
    def __init__(self, id, datasetId, metadata): 
        self.id = id
        self.datasetId = datasetId
        self.metadata = metadata

# 
# GAVariantSetMetadata
# 

class GAVariantSetMetadata(object):
    def __init__(self, key, value, id, type, number, description, info):
        self.key = key
        self.value = value
        self.id = id
        self.type = type
        self.number = number
        self.description = description
        self.info = info


