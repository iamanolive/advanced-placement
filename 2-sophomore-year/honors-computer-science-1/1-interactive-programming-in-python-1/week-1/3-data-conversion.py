# convert an hour into 24-hour format
hour = 3
ones_digit = hour % 10
tens_digit = hour // 10
print(str(tens_digit), str(ones_digit), ":00")
# string concatenation
time = str(tens_digit) + str(ones_digit) + ":00"
print(time) # string formatting


# python modules
import math
import random