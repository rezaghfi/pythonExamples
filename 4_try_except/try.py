# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
try:
    print(x)
except:
    print("An exception occurred")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("something else went wrong")

# The else block lets you execute code when there is no error.

try:
    print("Hello")
except:
    print("something went wrong")
else:
    print("Nothing went wrong")

# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("something went wrong.")
finally:
    print("the try except is finished")
try:
    f = open("demofile.txt")
    try:
        f.write("writing...")
    except:
        print("something wrong with write in file")
    finally:
        f.close()
except:
    print("something wrong with opening file")

print("-----------------------------raise(throw) exception----------------")

x = -1
if x < 0 :
    raise Exception("sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")