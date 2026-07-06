# Input a character
ch = input("Enter a character: ")

# Check if the character is an alphabet
if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")