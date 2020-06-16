from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.models import Registration
from flask_bcrypt import Bcrypt
from flaskblog import config
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
bcrypt = Bcrypt()
bcrypt.init_app(app)
hashed_password = bcrypt.generate_password_hash('latzonakospower').decode('utf-8')
print(hashed_password)
reg_key = Registration(registration=hashed_password)
db.session.add(reg_key)
db.session.commit()


