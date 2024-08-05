# Given a template that pre-defines three variables "hours", "minutes" and "seconds", write an assignment
# statement that updates the variable "total_seconds" to have a value corresponding to the total number of
# seconds for "hours" hours, "minutes" minutes and "seconds" seconds.

hours = 7
minutes = 21
seconds = 37

time = hours * 3600 + minutes * 60 + seconds
print(time)