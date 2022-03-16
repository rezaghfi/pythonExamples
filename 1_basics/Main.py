
str1 = "Hello"
str1 = str1*3
print(str1 + " Python")
g = 1
def pythonVariable(g):
  # data type 
  a = 'a'
  b = 'b'
  c = 1
  d = 1.343434
  f = 23434343434.34343434
  g += 1
  arr = [0,2,4,6]
  list = [1, 'reza', 23.44]
  print('array index 3: ', arr[2])
  print('list indec 2:', list[1])
  return a, b, c, d, f

def pythonIterative():
  arr = [2, 1,3,4,5,6,7,8,9,0,7]
  print("-------------------iterative for---------------------")
  for x in arr:
    print(x)
  i = 0
  print("-------------------iterative while---------------------")
  while i < arr[0]:
    print(i)
    i += 1
  n = 10
  result = 1
  print("-------------------iterative for range---------------------")
  for i in range(1, n+1):
    result *= i
    print(result)

a, b, c, d, f = pythonVariable(g)
pythonIterative()
print('f = ', f)

# function call in python: call by value
print(g)

