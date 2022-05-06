from turtle import color
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def midpoint(x, y, midX, midY):
    """First make a midpoint variable to hold the midpoint value after it calulates it,
    then send that calculated value to the varible. This is for exclusively for Quadrilaterials."""

    #! Use this for midpoints
    # for i in range(len(x)):
    #     mid.append((x[i] + x[i + 1])/2)
    #     mid.append((y[i] + y[i + 1])/2)

    for i in range(len(x)):
        midX.append((x[i] + x[i + 1])/2)
        midY.append((y[i] + y[i + 1])/2)

        if i >= 1:
            if midX[0] == midX[i]:
                break

x = [-2, 1, 5, 2, -2]
y = [3, 1, 7, 9, 3]

MidlineX = [-2, 5, 1, 2]
MidlineY = [3, 7, 1, 9]

midx = []
midy = []

midpoint(MidlineX, MidlineY, midx, midy)

plt.title('Shapes: Properties of Quadrilaterals')
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.plot(MidlineX, MidlineY, color='orange')
plt.plot(x, y, color='blue')
plt.scatter(midx[0], midy[0], color='red')

ax.set_xticks(np.arange(-4, 10, step = 1))
ax.set_yticks(np.arange(-1, 10, step = 1))

names = ['A', 'B', 'C', 'D', 'A']
mid_name = ['E']

for i, xy in enumerate(zip(x, y)):
    ax.annotate(text=f'{names[i]} {xy}', xy=xy)

for i, xy in enumerate(zip(midx, midy)):
    if i > 0:
        break
    else:
        ax.annotate(text=f'{mid_name[i]} {xy}', xy=xy)

plt.grid(linestyle = '--')
plt.gca().set_aspect('equal')


plt.show()