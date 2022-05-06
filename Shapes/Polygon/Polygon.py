from logging import root
from textwrap import fill
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = [-2, 4, -1, -2]
y = [2, 1, -3, 2]

x_2 = [-2, 4, 4, -2, -2]
y_2 = [2, 2, -3, -3, 2]
Side = []

# Tri_parts = [3, 2.5, 10] 
Tri_parts = []
Rect = []

MidlineX = [-2, 4, -1]
MidlineY = [2, 1, -3]
midx = []
midy = []


def Parts(x, y):
    # for i in range(len(x)):
    #     if i + 1 >= len(x):
    #         break
    #     else:
    #         Tri_parts.append( (abs(x[i] - x[i + 1]) +  (abs(y[i] - y[i + 1])) )/2)

    Tri_parts.append( (abs(x[0] - x[0 + 1]) +  (abs(y[0] - y[0 + 1])) )/2)
    #! Tri_parts.append( (abs(x[1] - x[1 + 1]) +  (abs(y[1] - y[1 + 1])) )/2)
    #! Tri_parts.append( (abs(x[2] - x[2 - 1]) +  (abs(y[2] - y[2 - 1])) )/2)

def Length(x, y):
    """First input lists x and y, and then it does the magic for you!"""

    Stop = len(x) 
    for i in range(len(x)):
        if i + 1 >= Stop:
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
    Length(x, y)
    print("\nTriangle Side Lengths:", Side)
    Side.clear()

    Length(x_2, y_2)

    print("\nRectangle Side Lengths:")
    for i in range(len(Side)):
        print(" ", Side[i])

    plt.title('Polygon: Area and line distances of Polygon')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.plot(x, y, color='navy')
    plt.plot(x_2, y_2, color='black')

    plt.fill(x_2, y_2, "lavender")
    plt.fill(x, y, "cornflowerblue")

    ax.set_xticks(np.arange(-6, 10, step = 1))
    ax.set_yticks(np.arange(-6, 10, step = 1))

    plt.grid(linestyle = '--')
    plt.gca().set_aspect('equal')

    names = ['A', 'B', 'C']
    names_2 = ['A', 'E', 'F', 0,'A']
    #? mid_name = ['E']

    for i, xy in enumerate(zip(x, y)):
        if i + 1 > len(names):
            break
        else:
            ax.annotate(text=f'{names[i]} {xy}', xy=xy)

    for i, xy in enumerate(zip(x_2, y_2)):
        if names_2[i] == 0:
            pass
        else: ax.annotate(text=f'{names_2[i]} {xy}', xy=xy)

    # Parts(x, y)
    # Area_rect(Side[0], Side[1])
    # Area_Poly(Tri_parts, Rect)
    plt.show()

Polygon()





# #? Functions for the main one
# def midpoint(x, y, midX, midY):
#     """First make a midpoint variable to hold the midpoint value after it calulates it,
#     then send that calculated value to the varible. This is for exclusively for polygons."""

#     #! Use this for midpoints
#     for i in range(len(x)):
#         midX.append((x[i] + x[i + 1])/2)
#         midY.append((y[i] + y[i + 1])/2)

#         if i >= 0:
#             break