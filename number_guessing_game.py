"""
Task 2: Number Guessing game
Saiket Systems - Python Development Internship
Description: Its a game where the computer opts a number and the user has to guess it using hints as higher or lower with limitations accoring to the difficulty level
"""


import numpy as np

while True:

    # Welcome Message
    print("\n" + "_"*60)
    print("\nWelcome to Number guessing game!")
    print("_"*60)

    # Difficulty Section
    print("\nChoose diffculty level.")
    print("e - Easy")
    print("m - Medium")
    print("h - Hard")

    choice = input().lower()

    # set difficulty
    if choice == "e":
        upper_limit = 50
        max_attempts = 7
    elif choice == 'm':
        upper_limit = 100
        max_attempts = 8
    elif choice == 'h':
        upper_limit = 500
        max_attempts = 10
    else:
        print("Invalid Input!")
        exit()
        
    # Generating Secret Number
    secret_number = np.random.randint(1, upper_limit + 1)    
        
    attempts = 0
    won = False
        
    print(f"I have selected a number between 1 - {upper_limit}")
    print("Try to guess it.")
    print(f"You only have {max_attempts} attempts.")

    while attempts < max_attempts:
                
        try:
            guess = int(input("\nEnter your guess: "))
            if guess < 1 or guess > upper_limit:
                print(f"Please enter a number between 1 and {upper_limit}")
                continue
            
            attempts += 1
                
            if guess > secret_number:
                print("Lower")
            elif guess < secret_number:
                print("Higher")
            else:
                print("\nCongratulations!")
                print("You Guessed the number.")
                won = True
                break

            print(f"Attempts left: {max_attempts - attempts}")
        
        except ValueError:
            print("Please enter a valid number!")

    if won:
        
        if attempts > 1:
            print(f"\nYou made {attempts} attempts to guess the number.")
        else:
            print(f"\nYou made {attempts} attempt to guess the number.")

    else:
        print("\nGame Over!")
        print(f"The number was {secret_number}")

    continue_game = input("\nDo you want to play again? Type 'y' for YES or 'n' for NO:     ")

    if continue_game != 'y':
        print("Thank you for playing")
        break