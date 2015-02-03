
from ga4gh_models import * 

class GA4GH_API(object):
    def getReference(self, id):
        pass
    def getReferenceBases(self, id):
        pass
    def getReferenceSEt(self, id):
        pass
    def searchCallSets(self, name, variantIds, pageSize, pageOffset):
        pass
    def searchReadGroupSets(self, name, datasetIds, pageSize, pageOffset):
        pass
    def searchReads(self, readGroupIds, referenceName, referenceId, start, end, pageSize, pageOffset):
        pass
    def searchReferenceSets(self, md5checksums, accessions, assemblyId, pageSize, pageOffset):
        pass
    def searchReferences(self, md5checksums, accessions, pageSize, pageOffset):
        pass
    def searchVariantSets(self, datasetIds, pageSize, pageOffset):
        pass
    def searchVariants(self, variantSetIds, variantName, callSetIds, referenceName, start, end, pageSize, pageOffset):
        pass

