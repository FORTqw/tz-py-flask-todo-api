import pymysql
from app import app, db

# Устанавливаем pymysql как драйвер для MySQL
pymysql.install_as_MySQLdb()

if __name__ == '__main__':
    app.run(debug=True)