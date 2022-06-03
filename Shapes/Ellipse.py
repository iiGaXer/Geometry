from math import cos, sqrt
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as mp

def Arc_draw(ax):
    for i in range(1, 2):
        para = mp.Arc([0,0], 10, 8, angle=0, theta1=0, theta2=360/i)
        ax.add_patch(para) 

def Patterns(ax):
    for i in range(1, 3):
        for j in range(1, 10): # n# - 3
            if i == 1:
                para = mp.Arc([j,j], 10, 8, angle=0, theta1=0, theta2=360/i, color='blue')
                ax.add_patch(para) 
            else:
                para = mp.Arc([10 + j, 10 - j], 10, 8, angle=0, theta1=0, theta2=360, color='red')
                ax.add_patch(para) 

def Line():
    fig, ax = plt.subplots()

    x = np.arange(-10, 20, 2)
    y = []

    b = 6
    c = 8
    angle = np.cos(60)

    for i in x:
        y.append(sqrt(b**2 + c**2 + 2*b*c * angle))

    plt.plot(x, y)
    plt.title('Curve: Algebra 2 equation')
    plt.ylabel('y-axis')
    plt.xlabel('x-axis')

    plt.grid(linestyle = '--')
    plt.gca().set_aspect('equal')

    ax.set_yticks(np.arange(-12, 26, step = 2))
    ax.set_xticks(np.arange(-10, 20, step = 2))
    plt.show()

def Arc(): 
    fig, ax = plt.subplots()

    # Arc_draw(ax)
    Patterns(ax)    

    plt.grid(linestyle = '--')
    plt.title('Arc: Algebra 2 Parabola')
    plt.ylabel('y-axis')
    plt.xlabel('x-axis')


    plt.gca().set_aspect('equal')

    ax.set_yticks(np.arange(-5, 15, step = 2))
    ax.set_xticks(np.arange(-5, 25, step = 2))

    plt.show()

Line()