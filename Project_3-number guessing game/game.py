from config import (
    DIFFICULTY,
    WIN_MESSAGE,
    LOSE_MESSAGE,
    HIGH_MESSAGE,
    LOW_MESSAGE,
)

from utils import (
    generate_number,
    get_user_guess,
    is_valid_guess,
    display_range,
)


class NumberGuessingGame:

    def __init__(self):
        self.secret_number = generate_number()
        self.attempts = 0
        self.max_attempts = 0

    def choose_difficulty(self):
        print("\nChoose Difficulty")
        print("1. Easy (10 Attempts)")
        print("2. Medium (7 Attempts)")
        print("3. Hard (5 Attempts)")

        while True:
            choice = input("\nEnter your choice (1-3): ")

            if choice == "1":
                self.max_attempts = DIFFICULTY["easy"]
                break

            elif choice == "2":
                self.max_attempts = DIFFICULTY["medium"]
                break

            elif choice == "3":
                self.max_attempts = DIFFICULTY["hard"]
                break

            else:
                print("Invalid choice. Try again.")

    def play(self):

        self.choose_difficulty()
        display_range()

        while self.attempts < self.max_attempts:

            print(f"\nAttempts Left: {self.max_attempts - self.attempts}")

            guess = get_user_guess()

            if not is_valid_guess(guess):
                print("Guess must be between 1 and 100.")
                continue

            self.attempts += 1

            if guess == self.secret_number:
                print(WIN_MESSAGE)
                print(f"You guessed it in {self.attempts} attempts.")
                return

            elif guess > self.secret_number:
                print(HIGH_MESSAGE)

            else:
                print(LOW_MESSAGE)

        print(LOSE_MESSAGE)
        print(f"The correct number was {self.secret_number}.")