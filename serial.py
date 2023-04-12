import re
import csv
import matplotlib.pyplot as plt
with open('./acquisition.csv') as f:
    data = f.read()
data = data.split(",")
y = [float(x) for x in data]
with open('./acquisition2.csv') as f:
    data = f.read()
data = data.split(",")
y_2 = [float(x) for x in data]
x = [i for i in range(len(data))]

plt.plot(x,y,color = "orange")
plt.plot(x,y_2,color = "cyan")
plt.show()