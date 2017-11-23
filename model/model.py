#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import SqliteDatabase, Model, IntegerField, DateTimeField, CharField, PrimaryKeyField
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import env

__author__ = 'Zaaferani'

db_path = os.path.join(os.path.dirname(__file__), "database.db")

database = SqliteDatabase(db_path)


class BaseModel(Model):
    class Meta:
        database = database


# noinspection PyBroadException
class Users(BaseModel):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    password = CharField()
    enabled = IntegerField(default=1)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(env.secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(env.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        try:
            user = Users.get(Users.id == data['id'])
            return user
        except:
            return None

    class Meta:
        db_table = "users"
        order_by = ('id', )


if __name__ == '__main__':
    u = Users()
    u.username = "ali"
    u.hash_password("123")
    u.enabled = 1
    u.save()

    u = Users()
    u.username = "hassan"
    u.hash_password("123456")
    u.enabled = 1
    u.save()
