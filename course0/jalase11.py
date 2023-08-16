import matplotlib.pyplot as plt

a=[]
b=[]
# y=0
# x=-50

for x in range(-100,100,1):
    y=x**2
    a.append(x)
    b.append(y)
    #x= x+1


plt.plot(a,b)
plt.show()