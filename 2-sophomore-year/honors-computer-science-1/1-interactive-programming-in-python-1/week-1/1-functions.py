# computes the area of a triangle
def triangle_area (base, height) : # function header
    # function body
    area = (1 / 2) * base * height
    return area # function output

a1 = triangle_area(3, 8); print(a1)
a2 = triangle_area(14, 2); print(a2)


# converts fahrenheit to celsius
def fahrenheit_to_celsius (fahrenheit) :
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

c1 = fahrenheit_to_celsius(32); print(c1)
c2 = fahrenheit_to_celsius(212); print(c2)


# converts fahrenheit to kelvin
def fahrenheit_to_kelvin (fahrenheit) :
    # calling another function inside of a function
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

k1 = fahrenheit_to_kelvin(32); print(k1)
k2 = fahrenheit_to_kelvin(212); print(k2)


# prints "hello, world!"
def hello () :
    # no inputs and no outputs
    print("hello world!")
    # return None

hello()
h = hello(); print(h)