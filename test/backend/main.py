from bson import json_util
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

uri = "mongodb+srv://choigod1023:1SibcMITMJ2KYspL@cluster0.j54w0lw.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
mydb = client['wheelsafe']
mycol = mydb['wheelsafe']

x = mycol.find()[0]
print(type(x))


@app.route('/arduino')
def arduino():
    parameter = request.args.to_dict()
    if len(parameter) == 0:
        return 'No parameter'
    parameters = ''
    for key in parameter.keys():
        parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
    print(parameters)
    return parameters


@app.route('/marker')
def show_marker():

    return json.loads(json_util.dumps(x))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
