import random

print("### Program is starting ###")

min_range_number = 1
max_range_number = 100

number = random.randrange(min_range_number, max_range_number)

max_guesses = 7
chance = 1

print(f"Guess number between {min_range_number} and {max_range_number}")
while chance < max_guesses:

    guess_number = int(input("Insert number "))

    if guess_number < number:
        print("Your number is lesser")
        
    elif guess_number > number:
        print("Your number is higher")
    else:
        break

    chance += 1

if chance == max_guesses:
    print(f"You reach the maximum chances. The number was {number}")
else:
    print(f"Congratulations!! You guess the right number in {chance} guesses")

print("### Program is ending ###")

