import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    UPLOAD_FOLDER = 'static/post_pics'
    UPLOAD_PROFILE_FOLDER = 'static/profile_pics'
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
