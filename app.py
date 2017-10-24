#!/usr/bin/env python
import hashlib, os, logging, sys
from flask import Flask, jsonify, make_response, request, url_for, abort, g
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

from flask_apps import *

if __name__ == '__main__':
    app.run(host=app.config['LISTENIP'], port=app.config['LISTENPORT'], debug=app.config['DEBUG'])
