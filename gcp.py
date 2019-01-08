from flask import jsonify
from google.cloud import storage

def getFiles():
    client = storage.Client()
    bucket = client.bucket('fb-events2')

    blobs = list(bucket.list_blobs())
    return blobs

def clean(pages):
    pages = pages.replace('b\'', '')
    pages = pages.replace('\'', '"')
    pages = pages.replace('}"', '}')
    return pages

def gets(r):
    filecontent = {}
    for f in getFiles():
        if f.name.endswith(".json"):
                content = str(f.download_as_string())
                filecontent[f.name] = clean(content)
    return jsonify(filecontent)