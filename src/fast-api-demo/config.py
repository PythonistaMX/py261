from os import environ

if environ.get('GAE_ENV'):
    SQLALCHEMY_DATABASE_URL = 'sqlite:///'
else:
    SQLALCHEMY_DATABASE_URL = 'sqlite:///db.sqlite3'