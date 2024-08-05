# Heron's formula states that the area of a triangle is sqrt(s(s - a)(s - b)(s - c)) where a, b and c
# are the lengths of the sides of the triangle and s = 1/2(a + b + c) is the semi-perimeter of the triangle.
# Given the variables x0, y0, x1, y1, x2 and y2, write a Python program that computes a variable "area" whose
# value is the area of the triangle with vertices (x0, y0), (x1, y1) and (x2, y2).

x0, y0 = 0, 0
x1, y1 = 3, 4
x2, y2 = 1, 1

a = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
b = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
c = ((x2 - x0) ** 2 + (y2 - y0) ** 2) ** 0.5 
s = 0.5 * (a + b + c)
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5