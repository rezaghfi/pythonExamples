print("-----------------python while loop----------------")
i = 1
while i < 6:
  print(i)
  i += 1
print("-----------------break----------------")

i = 0
while i < 6:
  if i == 3:
    break
  print(i)
  i += 1
print("-----------------continue----------------")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("-----------------else statement----------------")
i = 0
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print("______________________________python while loop______________________________")
friuts = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print("-----------------python while loop----------------")
for x in "banana":
  print(x)
print("-----------------break statement----------------")
for x in fruits:
  print(x)
  if x == "banana":
    break
print("-----------------continue statement----------------")
for x in fruits:
  if x == "banana":
    continue
  print(x)
for x in range(6):
  print(x)
for x in range(2, 6):
  print(x)
# else statement in for
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#nested loops
adj = ["red", "orange", "blue"]
for x in adj:
  for y in fruits:
    print(x, y)
#pass
for x in [0, 1 ,2]:
  pass