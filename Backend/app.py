import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["devops_db"]
collection = db["users"]


@app.route("/api/add-user", methods=["POST"])
def add_user():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({"message": "Inserted"}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)