from flask import jsonify
from google.cloud import storage

def getFiles():
    client = storage.Client()
    bucket = client.bucket('fb-events2')

    blobs = list(bucket.list_blobs())
    return blobs

def gets(r):
    filecontent = {}
    for f in getFiles():
        if f.name.endswith(".json"):
        	filecontent[f.name] = str(f.download_as_string())
    return jsonify(filecontent)