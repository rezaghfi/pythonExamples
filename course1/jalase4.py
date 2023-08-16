# n = int(input("enter your numvber: "))

def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        fac = 1
        for i in range(1, n+1):
            fac *= i
        return fac

list = []

for i in range(1,101):
    list.append(i)
list[50] = 1000

def max(list):
    temp = 0
    for i in range(0, len(list)):
        if list[i] > temp:
            temp = list[i]
    return temp


print(max(list))