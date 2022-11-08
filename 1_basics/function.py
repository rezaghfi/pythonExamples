
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

# number of argument
def my_function(fName, lName):
  print(fName + " "+ lName)

# my_fuction("email") it have error
my_function("reza","gholamalitabar")

#arbitrary arguments, *args
# it is overloaded function
def my_function(*kids):
  print("the youngest child is " + kids[2])
my_function("Email", "Tobias", "Linus")

#keyword arguments
def my_function(child3, child2, child1):
  print("The oldest child is "+ child3)
my_function(child1="Email", child2 = "Tobias", child3= "Linus")
my_function("Email", "Tobias", "Linus")

#arbitrary keyword arguments, **kwargs
def my_function(**kids):
  print("His last name is " + kids["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# default parameter
def func(country = "iran"):
  print("i am from " + country)
func()
func("india")
# passing a list as an argument
def func1(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
func1(fruits)

#return values
def func2(x):
  return 4 * x
print(func2(2))

#pass statement
def func3():
  pass

#Recursion
def tri_recursion(k):
  if (k > 0):
    result = k + tri_recursion(k - 1)
  else:
    result = 0
  return result
print(tri_recursion(6))

# python lambda
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression
x = lambda a : a + 20
print(x(5))
x = lambda a, b : a * b
print(x(3 ,5))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
