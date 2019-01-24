# -*- coding: utf-8 -*-
__author__ = 'op'

from . import bp
from app.models import Author, Content
from flask import jsonify, render_template

@bp.route('/search_author/<string:author>/<int:limit>/<int:page>')
def search_author(author, limit, page):
    authors = Author.query.filter(Author.name.contains(author)).limit(limit).offset(page*limit).all()
    return jsonify([author.to_dict() for author in authors])

@bp.route('/')
@bp.route('/hello')
def hellp():
    return "Hello"