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
mycol2 = mydb['wheel']
mycol3 = mydb['myplayer']
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


@app.route('/use')
def used():
    parameter = request.args.to_dict()
    if len(parameter) == 0:
        return 'No parameter'
    parameters = ''
    x = request.args['x']
    y = request.args['y']
    name = request.args['name']
    mycol3.update_one({"name": name}, {"$set": {"x": x, "y": y}})
    return {"x": x, "y": y, "name": name}


@app.route('/players')
def use_players():
    try:
        response = mycol3.find()
        return json.loads(json_util.dumps(response))
    except:
        return {"done": 0}


@app.route('/register')
def register():
    parameter = request.args.to_dict()
    if len(parameter) == 0:
        return 'No parameter'
    parameters = ''
    name = request.args['name']
    vulnerablility = request.args['vul']
    print(name, vulnerablility)
    find = mycol3.find_one({"name": name})
    print(find)
    if(find == None):
        mycol3.insert_one(
            {"name": name, "vulnerability": vulnerablility})
        return {"done": 1}
    else:
        return {"done": 0}


@app.route('/marker')
def show_marker():
    return json.loads(json_util.dumps(x))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
