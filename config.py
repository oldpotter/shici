# -*- coding: utf-8 -*-
__author__ = 'op'

import os
from dotenv import load_dotenv

env_file_path = os.path.join(os.getcwd(), '.env')
load_dotenv(env_file_path)

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////Users/oldpotter/python-projects/shici.sqlite'