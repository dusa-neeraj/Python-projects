import random
from config import (
    MIN_NUMBER,
    MAX_NUMBER,
    INVALID_INPUT
)


def generate_number():
    """
    Generate a random number within the configured range.
    """
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_user_guess():
    """
    Continuously ask the user for a valid integer.
    """
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print(INVALID_INPUT)


def is_valid_guess(guess):
    """
    Check whether the guess is within the allowed range.
    """
    return MIN_NUMBER <= guess <= MAX_NUMBER


def display_range():
    """
    Display the guessing range.
    """
    print(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}.")