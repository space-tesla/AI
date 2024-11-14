#Q.1) Write a Python program to print lowercase and uppercase alphabets of a string

text = "HelloWorld"

lowercase = [char for char in text if char.islower()]
print("Lowercase letters:", lowercase)

uppercase = [char for char in text if char.isupper()]
print("Uppercase letters:", uppercase)


# Output:
Lowercase letters: ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
Uppercase letters: ['H', 'W']