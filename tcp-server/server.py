import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import time

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.tododb

def todo():

    _items = db.tododb.find()
    items = [item for item in _items]

    print(items)


if __name__ == "__main__":
    while True:
        todo()
        time.sleep(10)

