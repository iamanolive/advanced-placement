# global variables
num1 = 1; print(num1)

def function():
    # local variables
    num1 = 2
    num2 = num1 + 1
    print(num2)

function()

# num2 cannot be called outside function()

print(num1)