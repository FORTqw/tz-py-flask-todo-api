from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate

# Устанавливаем pymysql как драйвер для mysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
# Подключение к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cocb@localhost/todo'
# Создаем экземпляр SQLAlchemy для работы с базой данных
db = SQLAlchemy(app)
# Создаем экземпляр migrate для работы с миграциями
migrate = Migrate(app, db)


from app.models import task
from app.views import task_view