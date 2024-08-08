def print_digits (number):
    if number < 0 or number >= 100:
        error_message = "Error: Input is not a two-digit number."
        print(error_message)
    else:
        tens_digit = number // 10
        ones_digit = number % 10
        number_string = "The tens digit is " + str(tens_digit) + ", and the ones digit is " + str(ones_digit) + "."
        print(number_string)

print_digits(29)