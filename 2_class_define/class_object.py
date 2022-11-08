print("_______________class and object______________________")
# create class
class MyClass:
  x = 5
# create object
p1 = MyClass()
print(p1.x)
print("----------------------init function----------------------")
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p2 = Person("john", 36)
print(p2.name)
print(p2.age)
# the __str__() Function
print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p2 = Person("reza", 28)
print(p2)
print("----------------------object methods----------------------")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("hello my name is " + self.name)
p2 = Person("reza", 28)
p2.myfunc()

print("----------------------self parameter----------------------")
class Person:
  def __init__(mySillyObject, name, age):
    mySillyObject.name = name
    mySillyObject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
p1.age = 40 # modify propertity on objects
del p1.age # delete the age property from the p1 object
del p1  # delete the p1 object

# pass statement
class Person:
  pass
