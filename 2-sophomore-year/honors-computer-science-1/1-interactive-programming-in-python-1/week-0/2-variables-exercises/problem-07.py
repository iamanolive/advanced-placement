# Given the pre-defined variables "present_value", "annual_rate" and "years", write an assignment
# statement that defines a variable "future_value" whose value is "present_value" dollars invested at
# "annual_rate" percent interest, compounded annually for "years" years.

present_value = 1000
annual_rate = 7
years = 10

future_value = present_value * (1 + 0.01 * annual_rate) ** years
print(future_value)