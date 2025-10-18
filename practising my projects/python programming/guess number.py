import random
print("Welcome to number guessing game: ")
user = input("Enter the number between 1-100 to start the game")
user = int(user)

x = random.randint(1,100)
if (user == x):
    print("You Guessed Right")
else:
    print("better luck next time")