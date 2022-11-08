# open file function
f = open("demofile.txt")
f = open("demofile.txt", "rt")
print(f.read())
# open file in different location.
#f = open("D:\\code\\python_tutorial\\5_file\\demofile.txt")
#print(f.read(5))
#print(f.readline())
#print(f.readline())
f = open("demofile.txt", "r")
for x in f:
    print(x)

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# append and write
f = open("demofile2.txt", "a")
f.write("now the file has more content!")
f.close()
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
import os
if os.path.exists("demofile4.txt"):
    os.remove("demofile4.txt")
else:
    print("demofile4.txt does not exist")
os.rmdir("myfolder")
f2 = open("demofile4.txt", "x")
f2.close()
#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

