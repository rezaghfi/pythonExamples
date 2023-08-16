# jalase10-module

# dictionary
person = {
  'name':"reza",
  'age': 27
}

#class
class Human():
  # feature = attribute
  name = ""
  age = 0

  # method
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def walking(self):
    print(self.name + " is walking")


