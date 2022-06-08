from flask import Flask, request
import os
from datetime import datetime
import requests

config = {
    "DEBUG": True  # run app in debug mode
}

public_ip = os.getenv('PUBLICID')
app = Flask(__name__)

@app.route('/enqueue', methods=['PUT'])
def enqueue():
    iterations = int(request.args.get('iterations'))
    work = request.get_data()
    requests.put(f"http://{public_ip}:5000/send_work?iterations={iterations}", data=work)
    return 'work pushed to queue'

@app.route('/pullCompleted', methods=['POST'])
def pullCompleted():
    top = int(request.args.get('top'))
    response = requests.post(f"http://{public_ip}:5000/pullCompleted?top={top}")
    return response.json

@app.route('/', methods=['GET'])
def status():
    date = datetime.now()
    return date.strftime("%d/%m/%y")
