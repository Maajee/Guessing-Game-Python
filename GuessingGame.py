import random

def we_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a Number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, Guess again. Too low.")
        elif guess > random_number:
            print("Sorry, Guess again, Too high")
    
    print(f"Yay! Congrats, You have found the random number {random_number} Correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (c): ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay! The Computer Guessed Your Number, {guess}, correctly")

we_guess(1000)
# computer_guess(100)

