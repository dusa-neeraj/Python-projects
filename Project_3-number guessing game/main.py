from config import WELCOME_MESSAGE
from game import NumberGuessingGame


def play_again():
    while True:
        choice = input("\nDo you want to play again? (y/n): ").strip().lower()

        if choice in ["y", "yes"]:
            return True

        elif choice in ["n", "no"]:
            return False

        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


def main():
    print(WELCOME_MESSAGE)

    while True:
        game = NumberGuessingGame()
        game.play()

        if not play_again():
            print("\nThank you for playing! 👋")
            break


if __name__ == "__main__":
    main()