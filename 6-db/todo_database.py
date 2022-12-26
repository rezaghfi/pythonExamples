import mysql.connector
from mysql.connector import Error


class Database():
  my_db = my_cursor = None

  def __init__(self):
    global my_db, my_cursor
    my_db = mysql.connector.connect(host="localhost", user="root", password="", database="todo")
    my_cursor = my_db.cursor()
    print('connect to database')

  def __del__(self):
    my_db.commit()
# create db todo and table work
# table work have id, title , body , created
# id = int , title = varchar , body = text , created = datetime()
class Todo(Database):
  def all_students(self, mode='DESC'):
    sql = "SELECT * FROM work ORDER BY id {}".format(mode)
    try:
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
    except Exception as e:
      return e
    return result

  def insert(self, data):
    sql = "INSERT INTO work (title, body) VALUES (%s , %s)"
    try:
      my_cursor.execute(sql, data)
    except Exception as e:
      return e
    return my_cursor.lastrowid

  def insert_many(self, data):
    sql = "INSERT INTO work (title, body) VALUES (%s , %s)"
    try:
      my_cursor.executemany(sql, data)
    except Exception as e:
      return e

  def delete(self, id):
    sql = "DELETE FROM work WHERE id = {}".format(id)
    try:
      my_cursor.execute(sql)
    except Exception as e:
      return e

  def update(self, id, data):
    sql = "UPDATE work SET title = %s ,body = %s WHERE id = {}".format(id)
    val = (data[0], data[1])
    try:
      my_cursor.execute(sql, val)
    except Exception as e:
      return e

  def truncate(self):
    sql = "TRUNCATE TABLE work"
    try:
      my_cursor.execute(sql)
    except Exception as e:
      return e
    return True
