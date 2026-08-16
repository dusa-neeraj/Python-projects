🎯 Number Guessing Game

A command-line Number Guessing Game built with Python. The player selects a difficulty level and tries to guess a randomly generated number within a limited number of attempts.


🚀 Features


Random number generation within a defined range
Three difficulty levels:

Easy — 10 attempts
Medium — 7 attempts
Hard — 5 attempts



Input validation (handles invalid/non-numeric input gracefully)
High/Low hints after every guess
Attempts counter and remaining tries display
Play Again option after each round
Clean, modular project structure (separate config, logic, and utility files)



📂 Project Structure

textNUMBER-GUESSING-GAME/
│
├── config.py         # Game constants (ranges, attempts per difficulty)
├── game.py            # Core game logic (guessing loop, win/lose conditions)
├── main.py             # Entry point — runs the game
├── utils.py            # Helper functions (input validation, display formatting)
├── README.md
└── requirements.txt


🛠️ Requirements


Python 3.8 or higher
No external dependencies (uses only Python standard library)



▶️ How to Run


Clone the repository


bash   git clone <repository-url>
   cd NUMBER-GUESSING-GAME


Run the game


bash   python main.py


Follow the on-screen prompts

Choose a difficulty level (Easy / Medium / Hard)
Enter your guesses
Get Higher/Lower hints until you guess correctly or run out of attempts






🎮 Sample Gameplay

textWelcome to the Number Guessing Game!

Select difficulty:
1. Easy   (10 attempts)
2. Medium (7 attempts)
3. Hard   (5 attempts)

Enter your choice: 2

I'm thinking of a number between 1 and 100.
You have 7 attempts remaining.

Enter your guess: 50
Too High! Try again.

Enter your guess: 25
Too Low! Try again.

Enter your guess: 37
🎉 Correct! You guessed it in 3 attempts.

Do you want to play again? (y/n):


🧩 Design Notes


config.py keeps all tunable values (number range, attempts per difficulty) in one place, so difficulty settings can be changed without touching game logic.
utils.py isolates reusable helpers like input validation, so game.py stays focused purely on game flow.
game.py contains the core loop: generating the number, checking guesses, tracking attempts, and determining win/loss.
main.py is a thin entry point that wires everything together and handles the "Play Again" loop.


This separation keeps the codebase easy to extend — for example, adding a new difficulty level or a scoring system later only touches one or two files.


🔮 Future Improvements


Add a scoring/leaderboard system
Add a hint system with limited "extra hint" tokens
Support custom number ranges
Add unit tests for game logic



📄 License

This project is open-source and available for personal or educational use.