# 让mysql以mysqldb的方式来对接ORM数据库
from pymysql import install_as_MySQLdb

install_as_MySQLdb()
