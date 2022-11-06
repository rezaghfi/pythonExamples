# ------------------------- jalase 4 --------------------------------------
#operator
# boolaean
x=bool(10 > 5)

x = bool(10>5)
print(x)
x = 3
print(bool(x > 0))

# string

a1 = "hasan"
a1 = 'hasan'
a2 = """fgfgfgfgfgf
fgfgfgfgf
fgfgf
"""
print("a2: ", a2)

a = "Hassan"
a = a.upper()
print("a: ", a)
a = a.replace("HA",'RR')
print("a: ", a)
print(a.find("A"))

# operators
#arithmetic
#assignment
#comparison
#logical
#identity
#membership
# + - * / // % **
# = += *=
x = 10
x += 6
# > < >= <= == !=
# x is y
# x in y
# logical opertor : and or not
x = 3
print("is x == 3 and x > 2?", bool(x==3 and x>2))
# identity opertor
x = 3.0
y = 3
print("is x equal to y? ", x is y)

# membership operator
x = "reza"
z = ["reza", "hasan", "ali"]
y = "my name is reza"
print("is x in z?",x in z)
print("is x in y?", x in y)


# if else elif
x = 2
if(x > 2):
    print("x is bigger than 5")
elif(x == 2):
    print("x is equal 2")
else:
    print("x is smaller than 2")

x = "hasan"
y = "my name is reza"
if(x in y):
    print("x is exist in y")
else:
    print("x is not exist in y")
