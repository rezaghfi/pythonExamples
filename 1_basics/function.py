
print("______________________________python functions______________________________")
# print("Hello it is simple calculator\n Enter your input1:")
# input1 = int(input())
# print("Enter your input2:")
# input2 = int(input())
# def add(in1, in2): return in1 + in2
# def sub(in1, in2): return in1 - in2
# def mul(in1, in2): return in1 * in2
# def div(in1, in2): return in1 / in2
# print(" add input1 and input2 is:",add(input1, input2))
# print(" sub input1 and input2 is:",sub(input1, input2))
# print(" multiple input1 and input2 is:",mul(input1, input2))
# print(" division input1 and input2 is:",div(input1, input2))

def drawRectangle(row):
  i = 1
  while i <= row:
    j = 1
    while j <= i:
      print('*', end = ' ')
      j += 1
    i += 1
    print("")
drawRectangle(5)

print("create a fuction - calling function - parameters or arguments - number of argument - arbitary arguments by * - keyword argument - arbitory keyword arguments - defualt paarameter value - passing list as a argument - return values - the pass statement - recursion - ")

list = ["apple", "cherry","banana"]
def guess(list):
  print("choose name from list:", list)
  for x in list:
    in1 = input("is your word "+ str(x) + "?")
    if (in1 == "yes"):
      print("hoooooray! I found the word.")
      break
#guess(list)

def max():
  a = int(input("enter input1:"))
  b = int(input("enter input2:"))
  c = int(input("enter input3:"))
  if(a > b):
    if (a > c):
      return a
    else:
      return c
  else:
    if(b>c):
      return b
    else:
      return c

print(max())