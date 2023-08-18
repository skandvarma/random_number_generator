from random import randint
from GUESS_ART import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose level Easy or Hard: ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, turns):
    if turns is None:
        turns = 0

    if guess > answer:
        print("Too high")
        turns -= 1
    elif guess < answer:
        print("Too low")
        turns -= 1
    elif guess == answer:
        print(f"You got it! The answer was {answer}")

    return turns


def game():
    print(logo)

    answer = randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print(f"Pssst, the answer is {answer}!")

    turns = set_difficulty()

    guess = 0
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

    if turns == 0:
        print(f"You've run out of guesses. The answer was {answer}")


game()
