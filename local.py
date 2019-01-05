from flask import Flask
from flask_restful import Api, Resource
import glob

app = Flask(__name__)
api = Api(app)
class Reader(Resource):
    def get(self):
        filecontent = {}
        for f in glob.glob("events/*.json"):
            f = open(f)
            filecontent[f.name] = f.read()
        return filecontent

api.add_resource(Reader, '/events')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
