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


api.add_resource(main.Login, '/login', endpoint='login')
api.add_resource(main.Main, '/', endpoint='index')

if __name__ == '__main__':
    database.connect()

    database.create_tables([Users], True)

    app.run('0.0.0.0', 5000, True)

# curl -X POST 127.0.0.1:5000/login -i -u ali:123
# curl -X POST 127.0.0.1:5000/login -i -H "Authorization: Basic YWxpOjEyMw=="
# YWxpOjEyMw== is Base64 of ali:123
# curl -X POST 127.0.0.1:5000/ -i -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsImV4cCI6MTUxMTQxNjc4MSwiaWF0IjoxNTExNDE2MTgxfQ.eyJpZCI6MX0.0Of_YE-UyIeOXW0JcP1-gaamK3x9dZYrBt4c2Q2D6uE"
