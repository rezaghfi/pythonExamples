
#global scope

x = 1
y = 1

# define function
def function1():
    #local scope
    return 100
    for i in range(1,4):
        #scope
        pass
    pass
    # return statement or end of function

def function2():
    pass
# call function
function1()


# x = int(input("how old are you?"))
# y = input("is you have permision?")
if y == "yes":
    y = True
elif(y == "no"):
    y = False
def acceptintomovie(age, is_supervise):
    if (age > 15) or (is_supervise == True):
        print ("MA+15 is accepted")
    else:
        print("not accepted")

# acceptintomovie(x, y)

def reverse(number):
    list = []
    while number > 0:
        list.append(number % 10)
        number = number // 10
    return list
print(reverse(123))

str = "100c"
if 'f' in str:
    print('c is in string')

str = str[:-1]
print(str)


list = [4,7,9,1,2]



max1 = list[-1]
max2 = list[-2]

number = max1 *10 +max2 

def compare(list1, list2):

    list1 = list1.sort()
    list2 = list2.sort()

    number1 = list1[-1] * 10 + list1[-2]
    number2 = list2[-1] * 10 + list2[-2]

    if number1 >= number2:
        return True
    else:
        return False
print(compare([1,3,4,6,2], [3,7,8,9,1]))
    