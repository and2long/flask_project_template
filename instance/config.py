"""instance/config.py
"""

# from instance.postgresql import SQLALCHEMY_DATABASE_URI as DATABASE_URI
from instance.sqlite3 import SQLALCHEMY_DATABASE_URI as DATABASE_URI

SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
