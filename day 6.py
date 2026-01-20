'''
import matplotlib.pyplot as plt
y1 =[]
y2 =[]
x = range(-100,100,10)
for i in x: y1.append(i**2)
for i in x: y2.append(-1**2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-2000,2000)
plt.axhline(0)
plt.axhline(0)
plt.savefig('quad.png')
plt.show()

import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1,y1,label = "line 1")
x2 = [1,2,3]
y2 = [4,1,3]
plt.plot(x2,y2,label = "line 2")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("two lines on ssame graph")
plt.legend()
plt.show()

import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles
x = [1,2,3,4,5,6]
y = [2,4,1,5,2,6]
plt.plot(x,y,
color = "green",linestyle = "dashed",linewidth = 3,marker = "o",markerfacecolor = "blue",markersize = 12)
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

import matplotlib.pyplot as plt
values = [5,6,3,7,2]
names = ['a','b','c','d','e']
plt.bar(names,values,color = "green")
plt.show()

import matplotlib.pyplot as plt
ages = [2,3,70,45,78,35,67,89,98,76,57,45,78,33,45,60,70,80,56,67,13,21,42,90]
range = (0,100)
bins = 10
plt.hist(ages,bins,range,color="green",histtype="bar",rwidth=0.8)
plt.xlabel("age")
plt.ylabel("no of people")
plt.title("my histogram")
plt.show()

import matplotlib.pyplot as plt

activities = ["eat",'sleep',"work",'play']
slices = [3,7,8,6]
colors = ['r','y','g','b']
plt.pie(slices,labels = activities,colors = colors,startangle=90,shadow=True,explode=(0,0,0.1,0),radius=1.2,autopct='%1.1f%%')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*(np.pi),0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
plt.figure(figsize=(15,8))
ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)
plt.show()
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(15, 8))

df = pd.DataFrame(data={
    'x':np.random.randint(0, 100, 30),
    'y':np.random.randint(0, 100, 30),
})

plt.figure(figsize=(15, 8))
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)

ax1.plot(df.index.values, df['x'], color='green', label='a')
ax1.plot(df.index.values, df['y'], color='brown', label='b')

plt.scatter(df['x'], df['y'], label = "stars", color = "green", marker = "*", s=30)


ax1.legend(loc='upper center')
plt.show()
#fhhofjj
























