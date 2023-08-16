# object oriented programing
# global
print("i am walking")
def walking():
  print("i am walking")
# call function
walking()


# create class

class MyClass():
  x = 5
  def y(self):
    b = 1
    print("ana y ")
  def __init__(self):
    print("ana myclass constructor method")
m = MyClass()
print(m.x)
m.y()

class Person:
  firstName = "" # property
  lastName = ""
  hieght = ""
  age = ""
  def __init__(self, firstName, lastName, hieght, age):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.hieght = hieght

  def walking(self): # method
    print(self.firstName + " "+ self.lastName + " is walking")
  def improveHeight(self):
    if(self.age< 10):
      print("your best hieght is 100 centemeter")
    elif(10<=self.age <=20):
      print("your best hieght 160 centemeter")


# create instance
reza = Person("reza", "gholamalitabar", 180, 25)
reza.firstName = "reza"
reza.lastName = "hasani"
reza.hieght = 180
reza.age = 25
reza.walking()
#create instance 2
fatemeh = Person("fatemeh", "rezai", 160, 19)
fatemeh.firstName = "fatemeh"
fatemeh.lastName = "rezai"
fatemeh.hieght = 160
fatemeh.age = 19
fatemeh.walking()
fatemeh.improveHeight()

class NoBody():
  pass

n = NoBody()

# inheritince
class Student(Person):
  pass

hasan = Student("hasan", "hasani", 90, 7)
hasan.improveHeight()
