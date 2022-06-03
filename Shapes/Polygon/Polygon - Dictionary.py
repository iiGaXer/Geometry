from logging import root
from textwrap import fill
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

A = {'x': -2, 'y': 2}
B = {'x': 4, 'y': 1}
C = {'x': -1, 'y': 3}

A_2 = {'x': -2, 'y': 2}
B_2 = {'x': 4, 'y': 2}
C_2 = [4, -3]
D_2 = [-2, -3]

Side = []

# Tri_parts = [3, 2.5, 10] 
Tri_parts = []
Rect = []

MidlineX = [-2, 4, -1]
MidlineY = [2, 1, -3]
midx = []
midy = []

def Length(x, y):
    """First input lists x and y, and then it does the magic for you!"""

    Stop = len(x) 
    for i in range(len(x)):
        if i + 1 == Stop:
            break
        else:
            Side.append(np.sqrt(np.square(x[i] - x[i + 1]) + np.square(y[i] - y[i + 1])))
 
def Area_rect(x_len, y_len):
    Rect.append(x_len * y_len)
    return x_len * y_len

def Area_Poly(parts, whole):
    Whole = 0
    Parts = 0
    for i in range(len(whole)):
        Whole += whole[i]

    for i in range(len(parts)):
        Parts += parts[i]

    area = Whole - Parts
    return print('Area of Polygon:', area)

#! Main
def Polygon():
    x = [A[0], B[0], C[0]]
    y = [A[1], B[1], C[1]]

    x_2 = [A_2[0], B_2[0], C_2[0], D_2[0], A[0]]
    y_2 = [A_2[1], B_2[1], C_2[1], D_2[1], A[1]]

    print("\nTriangle Side Lengths:", Side)
    Side.clear()

    Length(x_2, y_2)

    print("\nRectangle Side Lengths:")
    for i in range(len(Side)):
        print(" ", Side[i])

    plt.title('Polygon: Area and line distances of Polygon')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')

    plt.plot(x_2, y_2, color='black')
    plt.fill(x_2, y_2, 'lavender')
    ax.add_patch(plt.Polygon(list(zip(x, y)), closed=True, fill=True, color='cornflowerblue'))

    ax.set_xticks(np.arange(-6, 10, step = 1))
    ax.set_yticks(np.arange(-6, 10, step = 1))

    plt.grid(linestyle = '--')
    plt.gca().set_aspect('equal')

    names = ['A', 'B']
    names_2 = ['A', 'E', 'F', 'C']

    for i, xy in enumerate(zip(x, y)):
        if i + 1 > len(names):
            break
        else:
            ax.annotate(text=f'{names[i]} {xy}', xy=xy)

    for i, xy in enumerate(zip(x_2, y_2)):
        if i + 1 > len(names_2):
            break
        else:
            ax.annotate(text=f'{names_2[i]} {xy}', xy=xy)

    # Parts(x, y)
    # Area_rect(Side[0], Side[1])
    # Area_Poly(Tri_parts, Rect)
    plt.show()

Polygon()