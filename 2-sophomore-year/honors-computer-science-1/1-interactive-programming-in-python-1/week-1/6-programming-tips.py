# NameError
def volume_cube (side) :
    return side ** 3 # misspelled variable name

s = 2; volume = volume_cube(s) # misspelled function name
print("volume of cube with side", s, "is", volume)

import random # missing import statement

def random_dice ():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1 + die2

print("sum of two random dice, rolled once:", random_dice())
print("sum of two random dice, rolled twice:", random_dice())
print("sum of two random dice, rolled thrice:", random_dice())


# AttributeError
import math

def volume_sphere (radius) :
    # calling nonexistant function from imported module
    # all names are case sensitive
    return 4/3 * math.pi * (radius ** 3)

r = 2; volume = volume_sphere(r)
print("volume of sphere of radius", r, "is", volume_sphere(r))


# TypeError
def area_triangle (base, height):
    # strings cannot be multiplied
    return 0.5 * float(base) * float(height)
b = "5"; h = 2 + 2
area = area_triangle(b, h)
print("area of triangle with base", b, "and height", h, "is", area)


# SyntaxErrors
# function cannot be defined without colon
def is_mary (x) :
    # use "==" for checking equality
    if x == "mary":
        print("found mary!")
    else:
        print("no mary")

# undefined variables cannot be used as strings without quote
is_mary("mary"); is_mary("fred")


# code readability
import math

def area (a, b, c) :
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def area_triangle (side1, side2, side3) :
    """
    documentation string
    returns area of a triangle, given the lenghts of
    its three sides.
    """
    # heron's formula
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(semi_perimeter * 
                     (semi_perimeter - side1) * 
                     (semi_perimeter - side2) * 
                     (semi_perimeter - side3))


def favorites (instructor) :
    """
    returns the favorite thing of the given instructor
    """
    if instructor == "Joe":
        return "games"
    elif instructor == "Scott":
        return "ties"
    elif instructor == "John":
        return "outdoors"
    # returns None for all other cases
    else:
        print("favorites saw invalid instructor:", instructor)

print(favorites("John"))
# None signifies the lack of a value
print(favorites("Jeanie"))