# from tkinter import CENTER
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def Spiral():
    center = ()
    radius = []
    circle = []

    number = 20

    for i in range(number):
        center = list(center)
        center.append((i - number, i - number))
        center = tuple(center)

        radius.append(i + 1)
        circle.append(plt.Circle(center[i], radius[i], linewidth=2, fill=False))
        ax.add_patch(circle[i])


    x = [[number + 1, -number - 1], [0, 0]]
    y = [[0, 0], [number, -number - 1]]

    plt.title('Circle: Spiral')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.plot(x[0], y[0], color='blue')
    plt.grid(linestyle = '--')
    plt.gca().set_aspect('equal')
    plt.plot(x[1], y[1], color='red')

    # ax.set_xticks(np.arange(-10, 10, step = 1))
    # ax.set_yticks(np.arange(-10, 10, step = 1))

    plt.show()

def Nested():
    origin = (0, 0)
    radius = []
    circle = []
    coordinate = 0

    for i in range(50):
        radius.append(i + 1)
        circle.append(plt.Circle(origin, radius[i], linewidth=2, fill=False))
        ax.add_patch(circle[i])

        if i + 1 == 50:
            coordinate = i + 2


    x = [[coordinate, -coordinate], [0, 0]]
    y = [[0, 0], [coordinate - 1, -coordinate]]

    plt.title('Circle: Nested Circles', fontsize = 17)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.plot(x[0], y[0], color='blue')
    plt.grid(linestyle = '--')
    plt.gca().set_aspect('equal')
    plt.plot(x[1], y[1], color='red')

    # ax.set_xticks(np.arange(-10, 10, step = 1))
    # ax.set_yticks(np.arange(-10, 10, step = 1))

    plt.show()

Spiral()