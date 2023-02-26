import os

class Config:
    SECRET_KEY = 'e8c2a10d3f5a80f93195b970be4a6242'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = os.environ.get('DB_EMAIL'),
    MAIL_PASSWORD = os.environ.get('DB_PASS')
