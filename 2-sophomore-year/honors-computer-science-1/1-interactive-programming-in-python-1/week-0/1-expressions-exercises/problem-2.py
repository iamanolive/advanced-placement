# Write a Python statement that calculates and prints the number of 
# seconds in 7 hours, 21 minutes and 37 seconds

minutes_in_hour = 60
seconds_in_minutes = 60
seconds_in_hour = minutes_in_hour * seconds_in_minutes

hours = 7
minutes = 21
seconds = 37

hours_to_seconds = hours * seconds_in_hour
minutes_to_seconds = minutes * seconds_in_minutes

total_time = hours_to_seconds + minutes_to_seconds + seconds
print(total_time)