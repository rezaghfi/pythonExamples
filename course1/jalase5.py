list = [1,3,4,5,7,7]
# print(list[-2])

# list2 = ['ali', 'reza']

# list2.pop(1)
# list2.remove('ali')
# print(list2)

# max = 0
# for i in list:
#     if i > max:
#         max = i

# for i in list:
#     if i == max:     
#     #list.remove(i)

# max = 0

# for i in list:
#     if i > max:
#         max = i
# print(list)
# list = []

# for i in range(0,10):
#     temp = float(input("enter your number"))
#     list.append(temp)

# failed = []


# for i in list:
#     if i < 12:
#         failed.append(i)     

# print(max(failed))

def convertDay(input):
    year = 0
    month = 0
    day = 0
    year = 2023 + input // 365
    input = input % 365
    month = 1 + input // 30
    day = 1 + input % 30
    print(year,'/', month, '/', day)
    
# convertDay(366)

def primary2(number):
    for i in range(1, number+1):
        if number % i == 0:
            if primary(i) == True:
                print(i)

def primary(number):
    if number == 1: return False
    for j in range(2,number):
        if number % j == 0:
            return False
    return True



def employ(hour):
    salay = 0
    if  hour > 0 and hour <= 160:
        return hour * 100000
    elif hour <= 200 and hour > 160:
        return 160 * 100000 + (hour - 160) * 50000
    elif hour > 200:
        return 160 * 100000 + 40 * 50000

print(employ(201))