# variable

# scope 1.global 2.local

def diff(x, y):
    #local
    return x - y

# global vriable
number1 = 1
number2 = 2
#print(number1)

diff(number2, number1)

def sum(x, y):
    #local
    print("number1 = ")
    print(number1)
    z = x + y
    return z

result = sum(number1, number2)
#output
#print(result)
# print(z) is error becuase z is local variable

# variable

# 
x= 1
y = 1.2
y = 1.34343433343434
#boolean
y = False
#string text 
y = "hello"

#array
#list orderd changable duplecated values
#averages = ['ali',20,20,20]
averages = [20,20,20,20]
print(averages)
averages[0] = 19.5
print(averages)

print("averages is:",averages[0])

a = {20,20,20}

# dictionary KEY : VALUE

dic = {'name':'reza', 'age':29}

print(dic)

#range
r = range(3,20,2)
for n in r:
    print(n)
print(type(r))

msg = ""
name = "zahra"
if(name == "hasan"):
    msg = "hello hasan"
elif(name == "zahra"):
    msg = 'hello ' + name
else:
    msg = "hello others"
print(msg)
# دستورات شرطی: if , else if, if elif else, switch