guests = ["winnie", "nijo", "roo", "biscotti"]
message = "would you come over to have dinner with me?"
print(f"{guests[0].title()}, {message}")
print(f"{guests[1].title()}, {message}")
print(f"{guests[2].title()}, {message}")
print(f"{guests[3].title()}, {message}")

# name of the guest who can't make it
print(guests[-1].title())
# replace with name of new guest
guests[-1] = "bromine"

print(f"{guests[0].title()}, {message}")
print(f"{guests[1].title()}, {message}")
print(f"{guests[2].title()}, {message}")
print(f"{guests[3].title()}, {message}")