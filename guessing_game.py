import random

top_of_range = input("Choose the top number for your guess: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("The number must be higher than 0, Please try again")
        quit()
else:
    print("Please type a number next time")
    quit()

random_num = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_num:
        print("\nWay to go, you got it correct!")
        break
    elif user_guess < random_num:
        print("You were below the number")
    else:
        print("You were above the number")

print("\nIt only took you", guesses, "tries to get it!")
