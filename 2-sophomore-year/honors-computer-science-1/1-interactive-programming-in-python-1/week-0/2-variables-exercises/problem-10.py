# Given the variables x0, y0, x1 and y1, write an assignment statement that defines a variable "distance"
# whose value is the distance between the points (x0, y0) and (x1, y1).

import math

x0 = 2
y0 = 2
x1 = 5
y1 = 6

distance = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
print(distance)