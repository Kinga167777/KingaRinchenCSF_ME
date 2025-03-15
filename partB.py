import random

def guess_number_game():
    """
    A game where the player guesses a number randomly selected by the computer
    within a defined range. The user is continuously prompted for guesses until
    the correct number is guessed.
    
    Input: User guesses (integer).
    Output: Feedback on whether the guess is too low, too high, or correct.
    """
    print("\n--- Guess the Number Game ---")
    
    # Set the range of numbers
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    attempts = 0
    while True:
        try:
            # Get user's guess with validation
            user_guess = input(f"Guess a number between {lower_bound} and {upper_bound}: ")

            # Check if user wants to exit the game
            if user_guess.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break

            # Ensure the input is a valid integer
            user_guess = int(user_guess)

            # Validate that the guess is within the defined range
            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue

            # Increment attempt count
            attempts += 1

            # Check if the guess is correct
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.")

def rock_paper_scissors():
    """
    A text-based Rock, Paper, Scissors game where the user plays against the computer.
    The user selects one of the three options, and the computer randomly chooses one.
    The result of each round (win, lose, tie) is displayed.
    
    Input: User's choice ('rock', 'paper', 'scissors').
    Output: The result of the round (win, loss, or tie).
    """
    print("\n--- Rock Paper Scissors Game ---")
    
    # List of possible choices
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

        # Handle exit condition
        if user_choice == 'exit':
            print("Thanks for participating! Exiting the game.")
            break

        # Validate input
        if user_choice not in choices:
            print("Invalid choice, please select 'rock', 'paper', or 'scissors'.")
            continue

        # Get the computer's random choice
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print(f"winner{user_choice} beats {computer_choice}.")
        else:
            print(f"loser {computer_choice} beats {user_choice}.")

def show_menu():
    """
    Display the main menu and prompt the user to select a game or exit.
    """
    while True:
        print("\n--- Main Menu ---")
        print("1. Guess the Number Game")
        print("2. Rock Paper Scissors")
        print("3. Exit")
        
        # Get user input for menu choice
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("leaving the game")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")

# Start the program by calling the show_menu function
show_menu()
