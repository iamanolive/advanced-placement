# initializing variables
my_name = "Joe Warren"
print(my_name)
my_age = 121
print(my_age)

# reassigning values
my_age = my_age + 1
my_age += 1

# the magic pill scenario
magic_pill = 30
print(my_age - magic_pill)
my_granddad = 74
print(my_granddad - 2 * magic_pill)

# fahrenheit to celsius
temp_fahrenheit = 32
temp_celsius = (temp_fahrenheit - 32) * 5 / 9
print(temp_celsius) # 0 degrees celsius
temp_fahrenheit = 212
temp_celsius = (temp_fahrenheit - 32) * 5 / 9
print(temp_celsius) # 100 degrees celsius

# celsius to fahrenheit
temp_celsius = 0
temp_fahrenheit = (temp_celsius + 32) * 9 / 5
print(temp_fahrenheit) # 32 degrees fahrenheit
temp_celsius = 100
temp_fahrenheit = (temp_celsius + 32) * 9 / 5
print(temp_fahrenheit) # 212 degrees fahrenheit