people = [
    {"name": "Ravi", "age": 17},
    {"name": "Meena", "age": 22},
    {"name": "Arjun", "age": 15},
    {"name": "Sita", "age": 30}
]

# Filter people who are 18 or above
adults = filter(lambda p: p["age"] >= 18, people)

# Get only names of adults
adult_names = map(lambda p: p["name"], adults)

# Convert to list and print
print(list(adult_names))
