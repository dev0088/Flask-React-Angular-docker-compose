import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] =  "mongodb://mongodb:27017/flaskdb"
#app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
mongo = PyMongo(app)
db = mongo.db

@app.route("/", methods=["GET"])
def hello():
    return "<h1>Falsk: Hello World!</h1>"

@app.route('/users', methods=['GET'])
def users():
    if request.method == 'GET':
        users = db.user.find()
        print('==== users: ', users)
        data = []
        for user in users:
          data.append(user)
        return jsonify(data), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
