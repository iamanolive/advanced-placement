# getting the one's digit of a number
number = 49
tens_digit = number // 10
ones_digit = 49 % 10
print(tens_digit, ones_digit)
print(10 * tens_digit + ones_digit)

# 24 hour clock (clock arithmetic)
current_time = 20
shift_duration = 8
shift_end = (current_time + shift_duration) % 24
print(shift_end)

# screen wraparound (spaceship from week seven)
width = 800
position = 797
move = 5
position = (position + move) % width
print(position)