import random
print("Number Guessing Game")

Number = random.randint(1,9)
chances = 0
print("Guess a number between 1-9")
while chances < 5:
    guess = int(input("Enter your guess"))

    if guess == Number:
        print("Congratulations you won!")
        break
    elif guess < Number:
        print("You loose, try to choose a higher number.",guess)
    else:
        print("Your guess was too high, guess a low number than that.",guess)
    chances += 1
if not chances < 5:
    print("You loose! The actual number is: ",Number)