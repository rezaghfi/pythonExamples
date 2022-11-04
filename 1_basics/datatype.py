print("-----------------Built-in Data Type----------------")
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
x = "Hello World"
x = 49
x = 39.5
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name" : "john", "age":36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
x = None

x = str("Hello World")
x = int(39)
x = float(39.3)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(4)
x = dict(name="john", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(3)
x = bytes(4)
x = bytearray(3)
x = memoryview(bytes(5))

print("-----------------python numbers----------------")
x = 1
y = 3.3
z = 1j
print(type(x))
print(type(y))
print(type(z))
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#Complex numbers are written with a "j" as the imaginary part:

print("-----------------python casting----------------")
# int() float() str()
x = int(3.44) # x will be 3
y = str(3.3434) # Y  will be '3.3434'
print("-----------------python string----------------")
print('Hello')
print("Hello")
print("""for multiple line""")
print('''for multiple line''')
a = "Hello, World"
print(a[1])
for x in "banana":
  print(x)
print(len(a))
txt = "The best things in life are free!"
# in
print("free" in txt)
if "free" in txt:
  print("Yes, 'free' is present.")
# not in
print("expensive" not in txt)
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
h = "Hello, World"
print(h[2:5])
print(h[:5])
print(h[-5:-2])
print("-----------------python Modify String----------------")
print("h in uppercase is: ",h.upper())
print("h in lowercase is: ",h.lower())
b = "    Hello, World      "
print("strip remove spave from begin and end")
print(b.strip())
print("replace character h with g")
print(a.replace('H','G'))
print(a.split(","))
# concatenate strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print("-----------------python Format String----------------")
age = 25
txt = "My name is John, I am {}"
print(txt.format(age))
q = 2
i = 368
m = 34.6
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(q, i, m))
#print Escape characters
txt = "\twe\n \'are the  \r \\ \"mens\" "
print(txt)
# there are many method is exist for strings in https://www.w3schools.com/python/python_strings_methods.asp site
print("-----------------python Booleans----------------")
print(10 > 5)
print(10 == 6)
print(39 < 34)
print(bool(12))
print(bool(0), bool(False), bool(None), bool(""), bool(0), bool(()), bool([]), bool({}))
# function can return boolean
def myFunc():
  return True;
if myFunc():
  print("YES!")
else:
  print("NO!")
print("-----------------python Collections----------------")
a = """Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
print(a)
print("-----------------List----------------")
print("List items are ordered, changeable, and allow duplicate values.")
thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)
print(len(thisList))

# a list can contain diffrent data types.
list1 = ["avd", 34, True, 40, "male"]
print(type(list1))
# create list with list constructor
thisList = list(("apple", 3, 34))
print(thisList[1]) # Access list items
print(thisList[:3])
print(thisList[-1])
if "apple" in thisList:
  print("Yes, 'apple' is in the fruits list")
thisList[1] = "orange" # change item
thisList[1:3] = ['melon']
print(thisList)
thisList.insert(2,"watermelon") # insert new item
thisList.append("orange") # add item to end of list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist.remove("banana") # remove specified Item
thisList.pop(1) # remove specofied index.
thislist.clear() # clear list
print(thislist)
thislist = ["apple", "cherry", "banana"]
for x in thislist:
  print(x)
[print(x) for x in thislist]
#sort list by alphanumerically
thislist.sort()
print(thislist)
# copy list
list2 = thislist.copy()
print(list2)
# join two list
list1 = list2.copy()
list3 = list1 + list2
print(list3)
# or extend
list1.extend(list2)
print(list1)
# list method in https://www.w3schools.com/python/python_lists_methods.asp
print("-----------------tuples----------------")
print("Tuple is a collection which is ordered and unchangeable. Allows duplicate members.")
mytuple = ("apple", "banana", "cherry")
# duplicate
tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print("tuple can have duplicate items: ", tuple1)
print(len(tuple1))
#tuple data type like list
# create tuple with tuple() function
tuple1[1] # access like list
# can not change tuple but can change to list and convert to tuple
x = (1 , 3 ,4)
x = list(x)
x[1] = 2
x = tuple(x)
print(x)
del x # The del keyword can delete the tuple completely:

# unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)
# * astrisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green, yellow, red)
# loop tuples
tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
for x in tuple1:
  print(x)
for i in range(len(tuple1)):
  print(tuple1[i])
i = 0
while i < len(tuple1):
  print(tuple1[i])
  i =  i + 1

# join tuple like list
# multiply tuples
fruits = ("apple", "banana", "cherry")
fruits2 = fruits * 2
print("-----------------set----------------")
print("Set items are unordered, unchangeable, and do not allow duplicate values.")
set1 = {"abc", 34, True, 40}
print(set1)
# data types like tuple and list .
# set() constructor for create new set
# access items
for x in set1:
  print(x)
