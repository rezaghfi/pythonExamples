# if
# print("*")
# print("**")
# print("***")
#
second = 0
minute = 0
hour = 0
i = 0
print("-----------------loop ---------------")
print("-----------------while ---------------")
# true and false  = false
# clock
while hour != 0 or minute != 0:
    second += 1
    if(second == 60):
        minute += 1
        second = 0
        if(minute == 60):
            hour += 1
            minute = 0
            if(hour == 24):
                second = 0
                minute = 0
                hour = 0
    print(hour,":",minute,":",second)

i = 6
while i > 3:
    i -= 1
    print(i)

print("--------------------------------")
# break
i = 8
while i > 0:
    if i ==3:
        break
    print(i)
    i -= 1
print("--------------------------------")

# continue

i = 8
while i > 0:
    i -= 1
    if i ==3:
        continue
    print(i)

print("-----------------for ---------------")

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
print("-----------------while ---------------")

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

for x in 'banana':
    print(x)

print("-----------------function ---------------")
# function == تابع

# 1. keyword def
# 2. function name
# 3.  parameters
# 4. function body
# 5. calling function
def my_function(firstName, lastName):

    print("my name is:", firstName)
    print("my lastname is: ", lastName)


my_function("reza", "gholamalitabar")

def add(in1 , in2):
    return in1 + in2 + 2

def sub(in1, in2):
    return in1 - in2 + 3

print("enter:")
x = input()
print("your function is ",x)


# تمرین در مورد ایجاد یک ماشین حساب که از ورودی عدد می گیره و چهار تابع داره و عملیات اصلی رو روش آن ها انجام می دهد.
# تمرین دو: درست کردن یک مثلث قائم متساوی ساقین که اندازه ساق را از ورودی می گیره