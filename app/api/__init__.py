# -*- coding: utf-8 -*-
__author__ = 'op'

from flask import Blueprint

bp = Blueprint('api', __name__)

from . import routes