# Create an initial list of friends
friends = ["Gel", "Jim", "Kiel", "Vhony"]

# Print the list in the specified format
for i, friend in enumerate(friends):
    if i == 0:
        print(friend, end="")
    elif i == len(friends) - 1:
        print(f", and {friend}")
    else:
        print(f", {friend}", end="")

# Add items
friends.append("Juan")  # Add to end
friends.insert(1, "Jose")  # Insert at index 1

# Remove an item
friends.remove("Gel")

# Arrange list alphabetically
friends.sort()

# Print again
print("\nSorted list:")
for i, friend in enumerate(friends):
    if i == 0:
        print(friend, end="")
    elif i == len(friends) - 1:
        print(f", and {friend}")
    else:
        print(f", {friend}", end="")