import todo_database

db = todo_database.Database()
wk = todo_database.Work()
#sql = "insert into work(id, title, body, created) values (null, 'title 1', 'it is body of work 1', current_timestamp())"
# print(db.insert(sql))
# print(st.all_students())
# print(st.insert(('Omi', 1032, 'Dhaka')))
# print(st.truncate())

wk.create_table()
data = ['work0', 'it is body of work 0']
wk.insert(data)
data = [
      ('work 1', 'it is body of work 1'),
      ('work 2', 'it is body of work 2'),
      ('work 3', 'it is body of work 3'),
      ('work 4', 'it is body of work 4')
  ]
wk.insert_many(data)
print(wk.all_works())
wk.delete(4)
wk.update(3, ('work 3','it is updated body for work 3'))
print(wk.all_works())
