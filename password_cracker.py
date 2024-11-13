import random
import string

character_list = string.ascii_letters + string.digits + string.punctuation
password = input("Enter your password: ")
guess = ""

while (guess != password):
    guess = random.choices(character_list,k=len(password))
    guess = "".join(guess)

print("your password is " + guess)
