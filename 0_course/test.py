import jalase14_15

w = jalase14_15.Work()

#w.create_table()

print(w.read_all())
data = ['work0', 'it is work0 body']
w.insert(data)
data = [
  ('work 1','body1'),
  ('work 2', 'body2'),
  ('work 3', 'body3')
]
w.insert_many(data)
w.delete(1)
w.fatemeh()
print(w.read_all())
