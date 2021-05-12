import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['^', "@", '!', '#', '$', '%', '&', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

plst = [] # Defining an Empty Password List

for char in range(nr_letters):
    plst.append(random.choice(letters))

for char in range(nr_numbers):
    plst += (random.choice(numbers))  # '+=' works as List extend() Method

for char in range(nr_symbols):
    plst += (random.choice(symbols))

# shuffling the list
random.shuffle(plst)

# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
password = ''.join(plst)

print(f"The Password is =>   {password}")
