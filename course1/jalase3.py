# if else elif

# for stetemetn

list = [1,2,3,4,5,6]

for i in list:
    print(i)

for i in range(1,6):
    print(i)

day = 'sunny'
feel = 'bad'


if day == 'sunny' and feel == 'good':
    print("go out")
else:
    print("stay home")

if day == 'sunny' or feel == 'good':
    print('today is good')
else:
    print('today is bored')

#assignment
x = 1

#compresion
if(x == 1):
    print("x is 1")

# while

while (False):
    print("goodbye")



while x > 100:
    print(x)
    x +=2

# while True:
#     print("hello")

for i in range(1,100,2):
    print(i)

list = ['one', 'two', 'three']

list.append('four')

list.pop(3)
list.remove('three')

for i in list:
    print(i)

i = 0

while i < len(list):
    print(list[i])
    i+=1

array2d = [[1,2,3], [4,5,6],[7,8,9]]

print(array2d[0][0])

array3d = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]

print(array3d[1][0][2])



list2 = list.copy()

print(list2)

list.count('one')

list3 = [3,5,1,3,2]

list3.sort()

print(list3)


#function

def myfunction(*kids):
    print(kids[0])


myfunction('reza')

myfunction('reza', 'hasan', 'ali')

def max(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(max(z = 10, y = 5, x =1))


def empty():
    pass

sum100 = 0

for i in range(1,101):
    sum100 += i
print(sum100)

def sum100(n):
    if n > 0:
        return n + sum100(n-1)
    return 0

print(sum100(100))