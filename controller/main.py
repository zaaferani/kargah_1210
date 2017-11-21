#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, url_for, request, redirect, g
from flask_httpauth import HTTPBasicAuth
from model.model import Users
from flask_restful import Resource

__author__ = 'Zaaferani'

auth = HTTPBasicAuth()


# noinspection PyBroadException
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = Users.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        try:
            user = Users.get(Users.username == username_or_token)
        except:
            user = None
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


class Main(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token(6)
        return {'token': token.decode('ascii'), 'duration': 6}

    @auth.login_required
    def post(self):
        return dict(username=g.user.username)
