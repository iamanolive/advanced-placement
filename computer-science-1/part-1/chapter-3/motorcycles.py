motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# modifying elements in a list
motorcycles[1] = "ducati"
print(motorcycles)

# appending elements to end of list
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append("ducati")
print(motorcycles)

# appending elements to empty list
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

# inserting elements into a list
motorcycles.insert(0, "ducati")
print(motorcycles)

# removing item using del statement
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# removing item using pop() method
motorcycles = ["honda", "yamaha", "suzuki"]
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
message = f"The last motorcycle I owned was a {last_owned.title()}."
print(message)

# removing an element by value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
message = f"\nA {too_expensive.title()} is too expensive for me."
print(message)