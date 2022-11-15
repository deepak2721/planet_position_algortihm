from matplotlib import pyplot as plt
import random
import sys
 
x = []
y = []
 
plt.xlabel("X-axis")
plt.ylabel("Y-plot")
plt.title("Simple x-y plot")

for i in range(0, 50):
    plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5])
    plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5])
    x.append(random.randint(0, 100))
    y.append(random.randint(0, 100))
    plt.scatter(x, y, color = "green")
    plt.pause(0.01)
     
sys.exit(plt.show())