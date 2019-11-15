import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from encode import JSONEncoder

app = Flask(__name__)
#app.config["MONGO_URI"] =  "mongodb://root:password@mongodb:27017/flaskdb?authSource=admin"
app.config["MONGO_URI"] = "mongodb://" + os.environ["MONGODB_USERNAME"] + ":" + os.environ["MONGODB_PASSWORD"] + "@" + os.environ["MONGODB_HOSTNAME"] + ":27017/" + os.environ["MONGODB_DATABASE"] + "?" + "authSource=admin"

mongo = PyMongo(app)
db = mongo.db

@app.route("/", methods=["GET"])
def hello():
    return "<h1>Falsk: Hello World!</h1>"

@app.route("/users", methods=["GET"])
def users():
    if request.method == "GET":
        users = db.users.find()
        print("==== users: ", users)
        data = []
        for user in users:
            user.pop("_id")
            data.append(user)
        return JSONEncoder().encode(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
