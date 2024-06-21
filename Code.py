import random

def guess_number_game():
    # Step 1: User inputs the range
    X = int(input("Enter the starting range (X): "))
    Y = int(input("Enter the ending range (Y): "))
    
    if X > Y:
        print("Invalid range. Starting range (X) should be less than or equal to ending range (Y).")
        return

    # Step 2: System selects a random number in the range [X, Y]
    N = random.randint(X, Y)
    
    low = X
    high = Y
    attempts = 0
    
    print(f"Guess the number between {X} and {Y}.")
    
    while True:
        # Step 3: User makes a guess (using binary search technique)
        guess = int(input("guess:"))
        attempts += 1
        print(f"Your guess: {guess}")
        
        # Step 4: System provides feedback
        if guess < N:
            print(f"Too low, guess next number between {guess+1} and {high}")
            low = guess + 1
        elif guess > N:
            print(f"Too high, guess next number between {low} and {guess-1}")
            high = guess - 1
        else:
            print(f"Correct! The number was {N}. You guessed it in {attempts} attempts.")
            break

# Run the game
guess_number_game()

