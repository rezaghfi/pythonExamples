print("----------------------import module----------------------")
import myModule
myModule.greeting("reza")
a = myModule.person1["name"]
b = str(myModule.person1["age"])
print(a + " age is " + b)

import myModule as mm

c = mm.person1["name"]
d = str(mm.person1["age"])
print(c + " age is " + d)
print("----------------------built-in modules----------------------")
import platform
x = platform.system()
print(x)
x = dir(platform)
print(x)
print(platform.python_version())
print(platform.release())

print("----------------------import apart of module----------------------")
from myModule import person1
print(person1["country"])
print("----------------------datetime module----------------------")
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
x = datetime.datetime(2020, 5, 17)
print(x)
print(x.strftime("%a"))
print("----------------------math module----------------------")
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
x = abs(-7.25)
print(x)
x = pow(4,3)
print(x)
import math
x = math.sqrt(64)
print(x)
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)
x = math.pi;
print(x)
print("----------------------json module----------------------")
import json
#convert form json to python
x = '{ "name":"john", "age":30, "city":"babol"}'
y = json.loads(x)
print(y["age"])

#convert from python to json
x = {
  "name":"John",
  "age": 30,
  "city": "babol"
}
y = json.dumps(x)
print(y)

#convert python objects into json strings
print(json.dumps({"name":"John", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.43))
print(json.dumps(True))
print(json.dumps(None))

x = {
  "name": "reza",
  "age": 29,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
print("----------------------regEx module----------------------")
import re

txt = "the rain in spain"
x = re.search("^the.*spain$", txt)
print(x)
# regex function findall, search, split, sub

""" Metacharacters
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
"""
x = re.findall("ai", txt)
print(x)
x = re.findall("portugal", txt)
print(x)
x = re.search("\s", txt)
print(x)
x = re.sub("\s", "9", txt, 2)
print(x)

# install camelcase with pip. pip is a package manager for python packages.
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

# unistall camelcase package with pip unistall.

