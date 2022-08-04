from os import environ

if environ.get('ENVIRNMENT') == "PROD":
    SQLALCHEMY_DATABASE_URL = 'oracle:///'


if environ.get('GAE_ENV'):
    SQLALCHEMY_DATABASE_URL = 'sqlite:///'
else:
    SQLALCHEMY_DATABASE_URL = 'sqlite:///db.sqlite3'