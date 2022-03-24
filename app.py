from flask import Flask,jsonify,request
from classify import get_prediction
app = Flask(__name__)



