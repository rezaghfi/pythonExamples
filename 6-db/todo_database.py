import mysql.connector
from mysql.connector import Error


class TodoDatabase():
  def __init__(self):
    try:
      self.connection = mysql.connector.connect(host='localhost',
                                                database='todo',
                                                user='root',
                                                password='')
      if self.connection.is_connected():
        db_Info = self.connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        self.cursor = self.connection.cursor()
        self.cursor.execute("select database();")
        record = self.cursor.fetchone()
        print("You're connected to database: ", record)

    except Error as e:
      print("Error while connecting to MySQL", e)

  def create(self):
    self.cursor.execute("create table if not exists work(id n")

  def read(self):
    pass

  def update(self):
    pass

  def delete(self):
    pass

  def close(self):
    self.connection.close()
