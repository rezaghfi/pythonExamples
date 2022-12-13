
try:
  file = open("file1.txt")
except:
  print("not found")

print(file.read())

file.close()
