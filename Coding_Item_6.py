# Ask user for a sentence
sentence = input("Enter a sentence: ")

# Convert the to uppercase and lowercase
upper = sentence.upper()
lower = sentence.lower()
print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")

# Count how many times the letter "a" appears (case-insensitive)
count_a = sentence.lower().count('a')
print(f"The letter 'a' appears {count_a} times.")

# Check if the starts with "Hello"
starts_with_hello = sentence.startswith("Hello")
print(f"Starts with 'Hello': {starts_with_hello}")

# Split the sentence into words and print one per line
words = sentence.split()
print("Words:")
for word in words:
    print(word)