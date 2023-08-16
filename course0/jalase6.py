#function
# culculator
# def add(in1, in2): return in1 + in2
# def sub(in1, in2): return in1 - in2
# def mul(in1, in2): return in1 * in2
# def div(in1, in2): return in1 // in2
#
# in1 = int(input("enter input one:"))
# in2 = int(input("enter input two:"))
# print("addition of in1 and in2 is: ", add(in1 , in2))
# print("subtract of in1 and in2 is: ", sub(in1 , in2))
# print("multiple of in1 and in2 is: ", mul(in1 , in2))
# print("divition of in1 and in2 is: ", div(in1 , in2))

#
width = int(input("enter regtancle's witdh: "))
i = 1
while i <= width:
  j = 1
  while j <= i:
    print("*", end=' ')
    j += 1
  print("\n")
  i += 1

print("your list is 1-orange 2-banana 3-apple 4-cherry and guess your fruit")
fruits = ["orange", "banana", "apple", "cherry"]
a = fruits[1]
x = input("is your choise is banana?")
if(x == 'no'):
  a = fruits[0]
  x = input("is your chiose is orange?")
elif(x == 'yes'):
  print("hooora")