#!/usr/bin/python3.8
from flask import Flask
from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import uuid
import jwt
import datetime
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from routes.endpoint import bp

app = Flask(__name__)

app.register_blueprint(bp)
app.run(host='0.0.0.0', port=5500 )
