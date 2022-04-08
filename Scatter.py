import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

#? Scale canvas
ax.set_xticks(np.arange(0, 8, step = 0.5))
ax.set_yticks(np.arange(0, 8, step = 0.5))

plt.title("Scatter", fontsize= 15)
plt.xlabel('x-values', fontsize = 13)
plt.ylabel('y-values', fontsize = 13)

#? Set the lines and grid
plt.gca().set_aspect('equal')
plt.grid(linestyle = '--')

names = ['A', 'B', 'C', 'D', 'E']

for i, xy in enumerate(zip(x, y)):
    ax.annotate(text=f'{names[i]} {xy}', xy=xy)



plt.scatter(x, y)
plt.show()