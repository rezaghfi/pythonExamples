print("_______________Python Inheritance______________________")
class Person:
  def __init__(self, fname, lname):
    self.firstName = fname
    self.lastName = lname
  def printname(self):
    print(self.firstName, self.lastName)
class Student(Person):
  pass
s = Student("reza", "gholamalitabar")
s.printname()