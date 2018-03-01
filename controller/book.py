#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, url_for, request, redirect, g
from model.model import Books
from controller.main import auth2
from flask_restful import Resource

__author__ = 'Zaaferani'


class Insert(Resource):
	@auth2.login_required
	def post(self):
		json_input = request.get_json()
		b = Books()
		b.title = json_input['title']
		b.author = json_input['author']
		b.save()
		return dict(id=b.id, title=b.title, author=b.author)


class List(Resource):
	@auth2.login_required
	def get(self):
		res = Books.select()
		ls = [
			dict(id=b.id, title=b.title, author=b.author) for b in res
		]
		return dict(books=ls)


class Remove(Resource):
	@auth2.login_required
	def delete(self, b_id):
		try:
			b = Books.get(id=b_id)
		except Books.DoesNotExist:
			return None, 404
		b.delete_instance()
		return dict(status=True, id=b_id), 200
