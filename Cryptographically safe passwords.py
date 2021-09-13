import string
from secrets import choice
# We need to import the secrets instead of the random module to generate cryptographically secure random numbers

characters = string.ascii_letters + string.punctuation + string.digits
print(characters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789

password = "".join(choice(characters)for x in range(10))
# range for no. of characters
print(password)
