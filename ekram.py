#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, g
from flask_restful import Api
from controller import main
import env
from model.model import database, Users

app = Flask(__name__)
app.secret_key = env.secret_key
app.config['SECRET_KEY'] = env.secret_key

api = Api(app)


api.add_resource(main.Main, '/h')
api.add_resource(main.Main, '/', endpoint='index')

if __name__ == '__main__':
    database.connect()

    database.create_tables([Users], True)

    app.run('0.0.0.0', 5000, True)

# curl -X POST 127.0.0.1:5000/h -i -u ali:123
# curl -X POST 127.0.0.1:5000/h -i -H "Authorization: Basic YWxpOjEyMw=="
# YWxpOjEyMw== is Base64 of ali:123