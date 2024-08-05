# Given a template that pre-defines a variable "miles", write an assignment statement that defines a variable
# "feet" whose value is the number of feet in "miles" miles.

miles = 13
feet_in_miles = 5280
feet = miles * feet_in_miles

result = str(miles) + " miles equals " + str(feet) + " feet." 
print(result)