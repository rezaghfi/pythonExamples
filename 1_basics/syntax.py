print("-----------------indentation----------------")
# Python uses indentation to indicate a block of code.
# Python will give you an error if you skip the indentation:
"""
if 5 < 2:
print("5 is bigger than 2")
"""
#The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 4 > 2:
  print("4 is bigger than 2")
if 5 > 2:
      print("5 is bigger than 2")
#You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
"""
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""
print("-----------------python variable----------------")
x = 5
y = "Hello, World!"
print("x=",x,"and y=", y)
print("-----------------comments----------------")
print("comment in single line use # and in multiple line use double \"\"\" ")   #this is a comment
print("-----------------creating variable----------------")
#A variable is created the moment you first assign a value to it.
x = 4
y = "john"
print(x)
print(y)
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4 # x is of type int
x = "Sally" # x is now of type str
print("-----------------casting variable----------------")
print(x)
x = str(3)  # x is '3'
y = int(3) #y is 3
z = float(3) #z will be 3.0
print("-----------------get the type----------------")

x = 5
y = "john"
print(type(x))
print(type(y))
print("-----------------single or double quotes----------------")
x = "John"
# is the same as
x = 'John'
print("-----------------case-sensitive----------------")
a = 4
A = "Sally"
# A will not overwrite a
print("-----------------variable Names----------------")
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""
ILLIGAL VARIABLE NAMES:
2myvar = "John"
my-var = "John"
my var = "John"
"""
print("-----------------Multi Words Variable Names----------------")
print("CamelCase")
print("PascalCase")
print("snake_case")
print("-----------------Many Values to Multiple Variables----------------")
x , y , z = 1, 3, 4
print(x, y, z)
print("-----------------One Value to Multiple Variables----------------")
x = y = z = "orange "
print(x, y, z)
print("-----------------unpack collection----------------")
fruits = ["apple", "banana", "cherry"]
print(x, y, z)
print("-----------------print function----------------")
# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)
#In the print() function, you output multiple variables, separated by a comma:
x , y , z = "Python" , " is " , "awesome"
print(x, y, z)
#You can also use the + operator to output multiple variables:
print(x + y + z)
#For numbers, the + character works as a mathematical operator:
x , y = 2 , 5
print(x + y)
#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
"""
x = 3
y = "John"
print(x + y)
"""
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 3
y = "John"
print(x, y)
print("-----------------Global Variable----------------")
x = "awesome"
def myfunc():
  print("Python is "+ x)
myfunc()
print("-----------------local Variable----------------")
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is "+ x)
print("-----------------the global keyword----------------")
#If you use the global keyword, the variable belongs to the global scope:
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
print(x)
myfunc()
print("Python is "+ x)

print("-----------------python Operators----------------")
print("1.Arithmetic +-*/ ** //", " 2.Assignment = += -= ", " 3.Comparison < > <= >= == !=", " 4.Logical AND OR NOT", " 5.Identity IS , NOT IS", " 6.Membership in , not in", " 7.Bitwise Operators | &")


print("-----------------python if elif else----------------")
a = 33
b = 200
if a > b:
  print("a is bigger than b")
elif a == b:
  print("a is equal to b")
else:
  print("a is smaller than b")

# short hand if
if a > b: print("a is bigger than b")
print("a is bigger") if a > b else print("b is bigger")
a = 220
b = 220
print("a") if a > b else print("=") if a == b else print ("b")
# and
a , b , c = 200 , 33 , 500
if a > b and c > a:
  print("both conditions are true")
# or
if a > b or a > c:
  print("at least one conditions is true")
# nested if
x = 41
if x > 10:
  print("above ten,")
  if x > 20:
    print(" and also above 20!")
  else:
    print("but not above 20.")
# pass
if a > b:
  pass

