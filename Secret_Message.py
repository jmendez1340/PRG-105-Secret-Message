# We will create a secret message using anagrams (Mixed up letters)

# import the Random library
import random

# Randomly jumble the order of items in a list
# This code is encoded from the jumble program
def jumble_list(jumble):
    for current_index in range(len(jumble)):    # Loop through all the letters
        random_index = random.randrange(0, len(jumble)) # Randomly chooses a letter
         # Swap the letters at that position
        temp = jumble[current_index]    # Remember the value at the current index
        jumble[current_index] = jumble[random_index]
        jumble[random_index] = temp

# Creates a list of the letters of the alphabet
alpha_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Create a copy of the list with the letters mixed up
# alpha_jumble = alpha_list

# alpha_jumble.append('end')
# print alpha_list
# print alpha_jumble

# Cannot just set a list equal to a new variable name because it just creates a new name
# for the same list and we want a new list
alpha_jumble = list() #Creates an empty list
# Copy the alpha_list to the alpha_jumble
for letter in alpha_list:
    alpha_jumble.append(letter)
#Call my function to jumble this list - it does not return a value
jumble_list(alpha_jumble)

# print alpha_list
# print alpha_jumble

# Create a dictionary that pairs a letter with a random letter
anagram = dict()     # Create an empty Dictionary
index = 0            # Use this to index the ordered lists

# Loops through the ordered lists and make a dictionary entry
for letter in alpha_list:
    anagram[letter] = alpha_jumble[index]
    index += 1

# print "\n"
# print anagram

print ("\nThis program will encode your message")
message = raw_input("Enter your message: ")
print("\n Your secret message is: ")

Secret_Message = ""             # Start with an empty string
# Loop through theh characters entered by the user
# If the character needs to be encoded, find the match in the dictionary
# Otherwise, just copy over the character

for character in message:
    if character.upper() in alpha_list:
        # If the user typed a lowercase I want to add a lowercase letter
        # Otherwise if it's already uppercased just keep it that way
        if character == character.upper():
            Secret_Message += anagram[character.upper()]
        else:
            Secret_Message += anagram[character.upper()]
    else:
        Secret_Message += character

print Secret_Message
