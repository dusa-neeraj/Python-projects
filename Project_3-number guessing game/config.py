# Number Guessing Game Configuration

# Range of numbers
MIN_NUMBER = 1
MAX_NUMBER = 100

# Difficulty levels
DIFFICULTY = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}

# Messages
WELCOME_MESSAGE = """
====================================
     NUMBER GUESSING GAME
====================================
Guess the number between 1 and 100.
"""

WIN_MESSAGE = "🎉 Congratulations! You guessed the correct number."

LOSE_MESSAGE = "❌ You have used all your attempts."

INVALID_INPUT = "⚠ Please enter a valid integer."

HIGH_MESSAGE = "📈 Too High!"

LOW_MESSAGE = "📉 Too Low!"