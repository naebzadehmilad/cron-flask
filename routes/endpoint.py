import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from flask import Blueprint
from flask import jsonify
from flask_expects_json import expects_json
from model import modeljson
from controller import controller
from werkzeug.security import generate_password_hash, check_password_hash
import json
import uuid
import shortuuid
from flask.globals import request
from ratelimit import limits


bp = Blueprint('/', __name__)
global keys
validuser = 'validuser'
validtoken = 'validpass'


@bp.route('/cron', methods=['POST'])
@expects_json(modeljson.registerjson)
@limits(calls=1, period=20) #max 1 call per second
def index():
    content = request.json
    try:
        print('is token', content['token'], 'AND', 'is username', content['username'])
        if content['token'] == validtoken and content['username'] == validuser:
            controller.call()
            return 'was implemented', 200
        else:
            return 'not authorized', 401

    except:

        return "An exception occurred", 500

