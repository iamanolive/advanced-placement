# Given the pre-defined variables "first_name" and "last_name", write an assignment statement that defines
# the variable "name_tag" whose value is the string "My name is % %." where the percents should be replaced
# by "first_name" and "last_name". Note that, in Python, you can use the + operator on strings to
# concatenate (i.e. join) them together into a single string.

first_name = "Joe"
last_name = "Warren"

name_tag = "My name is " + first_name + " " + last_name + "."
print(name_tag)