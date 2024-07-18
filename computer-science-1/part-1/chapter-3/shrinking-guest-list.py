guests = ["winnie", "nijo", "roo", "biscotti"]
message = "would you come over to have dinner with me?"
print(f"{guests[0].title()}, {message}")
print(f"{guests[1].title()}, {message}")
print(f"{guests[2].title()}, {message}")
print(f"{guests[3].title()}, {message}")

# found a bigger table
print("guys, I found a bigger table, guess the party's getting bigger too.")
# inserting new guests
guests.insert(0, "queen")
guests.insert(2, "sheru")
guests.append("kitten")

print(f"{guests[0].title()}, {message}")
print(f"{guests[1].title()}, {message}")
print(f"{guests[2].title()}, {message}")
print(f"{guests[3].title()}, {message}")
print(f"{guests[4].title()}, {message}")
print(f"{guests[5].title()}, {message}")
print(f"{guests[6].title()}, {message}")

# invite only two people
print("oops sorry guys, turns out I can invite only two people over")

print(f"hey {guests.pop()} how about we catch up another time?")
print(f"hey {guests.pop()} how about we catch up another time?")
print(f"hey {guests.pop()} how about we catch up another time?")
print(f"hey {guests.pop()} how about we catch up another time?")
print(f"hey {guests.pop()} how about we catch up another time?")

print(f"hey {guests[0]} we're still on for tonight right?")
print(f"hey {guests[1]} we're still on for tonight right?")

del guests[0]
del guests[0]

print(guests)