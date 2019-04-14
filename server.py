import pymongo
from flask import Flask

key_file = open('/home/shanu/my_projects/car_rental/key.txt')
key = str(key_file.read())

client = pymongo.MongoClient(key)
db = client.test

print db

app = Flask(__name__)
@app.route("/")

def home():
    return "Hello, World!"

@app.route("/salvador")
def salvador():
	home()
	return ("Hello, Salvador")


if __name__ == "__main__":
    app.run(debug=True)