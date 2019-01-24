# -*- coding: utf-8 -*-
__author__ = 'op'

from . import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    desc = db.Column(db.Text)

    def __repr__(self):
        return 'Author:' + self.name

    def to_dict(self):
        author = {
            "id": self.id,
            "name": self.name,
            "desc": self.desc
        }
        return author

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    author = db.Column(db.String(100), index=True)
    body = db.Column(db.Text)

    def set_body(self, arr_body):
        self.body = ';'.join(arr_body)

    def get_body(self):
        return self.body.split(';')

    def __repr__(self):
        return 'Content: {} - {}'.format(self.title, self.author)