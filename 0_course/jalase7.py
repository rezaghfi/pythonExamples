# structure programing

# paratice1

list = ["apple", "banana"]

def guess(list):
  print("your list is:", list)
  for x in list:
    in1 = input("is your word "+x+"?")
    if(in1 == "yes"):
      print("hoooooray! I found the word.")
      break
#guess(list)

def max():
  a = int(input("enter number one: "))
  b = int(input("enter number two: "))
  c = int(input("enter number three: "))
  if(a >=b and a>=c):
    return a
  elif(b>=a and b>=c):
    return b
  else:
    return c

#print(max())

# object oriented programing

class car:
  # properties
  pass


