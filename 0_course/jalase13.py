import mysql.connector
from mysql.connector import Error


try:
  connection = mysql.connector.connect(host='localhost',
                                       database='todo',
                                       user='root',
                                       password='')
  if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version: ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
    sql = """
    CREATE TABLE IF NOT EXISTS work(
      id int(11) NOT NULL AUTO_INCREMENT,
      title varchar(100) NOT NULL,
      body text NOT NULL,
      created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (id)
    ) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;"""
    try:
      cursor.execute(sql)
    except Exception as e:
      print(e)
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
except Error as e:
  print("Error while connecting to MySQL", e)

