from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_msearch import Search
from flask_mail import Mail
import os
from datetime import timedelta
from bankingsite.limiter import limiter
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= "logs.log", level=logging.INFO, format= log_format)
app = Flask(__name__)
limiter.init_app(app)
app.config['SECRET_KEY'] = 'this-is-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
search = Search()
search.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'CraftyWoodDev@hotmail.com'
app.config['MAIL_PASSWORD'] = 'outlook0appdev'
mail = Mail(app)

from bankingsite import routes