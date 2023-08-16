import mysql.connector

class Database():
  my_cursor = my_db = None

  def __init__(self):
    global my_cursor, my_db
    try:
      my_db = mysql.connector.connect(host="localhost", user="root", password="",database="todo")
      my_cursor = my_db.cursor()
      print("connected to database")
    except:
      print("not connected database")

  def __del__(self):
    my_db.commit()

class Work(Database):

  def create_table(self):
    sql = "create table work(id int not null auto_increment primary key, title varchar(100) not null, body text not null, created datetime not null default current_timestamp)"
    my_cursor.execute(sql)

  def read_all(self):
    sql = "select * from work"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    return result

  def insert(self, data):
    sql = "insert into work(title, body) values(%s , %s)"
    my_cursor.execute(sql, data)

  def insert_many(self, data):
    sql = "insert into work(title, body) values (%s, %s)"
    my_cursor.executemany(sql, data)

  def delete(self, id):
    sql = "delete from work where id = {}".format(id)
    my_cursor.execute(sql)

  def fatemeh(self):
    d="truncate table work"
    my_cursor.execute(d)