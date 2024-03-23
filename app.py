from flask import Flask, render_template
from pymongo import MongoClient
import datetime
from flask import request

app = Flask(__name__)

client = MongoClient("SAMPLE")
db = client['log_db']
collection = db['logs']

def log_to_db(message):
    log = {"message": message, "timestamp": datetime.datetime.utcnow()}
    collection.insert_one(log)

@app.route('/')
def home():
    log_to_db("Home page visited")
    return render_template('home.html')

@app.route('/file_list')
def file_list():
    log_to_db("File list page visited")
    uploaded_files = [] 
    return render_template('file_list.html', uploaded_files=uploaded_files)

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    log_to_db(data['message'])

    return '', 204


if __name__ == '__main__':
    app.run(debug=True)