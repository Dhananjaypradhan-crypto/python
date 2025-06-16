import random
EASY_LEVELS_ATTEMPTS = 10
HARD_LEVELS_ATTEMPTS = 5
def choose_difficulty(level_chosen):
    if level_chosen == "easy":
        return EASY_LEVELS_ATTEMPTS
    else:
        return HARD_LEVELS_ATTEMPTS
def check_guess(guess, answer, attempts):
    if guess < answer:
        print("your guess is too low")
        return attempts - 1
    elif guess > answer:
        print("your guess is too high")
        return attempts - 1
    else:
        print(f"you got it! the answer was {answer}")
        return 0
def play_game():  
    print("let me think of a number between 1 and 100")
    answer = random.randint(1, 100)
    print("Let me think of a number between 1 and 100")
    answer = random.randint(1, 100)
    level= input("choose a difficulty. type 'easy' or 'hard': ")
    attempts = choose_difficulty(level)
    if attempts!= EASY_LEVELS_ATTEMPTS and attempts != HARD_LEVELS_ATTEMPTS:
        print("you have entered an invalid level")
        return
    guessed_number= 0
    while guessed_number != answer:
        print(f"you have {attempts} attempts remaining to guess the number")
        guessed_number = int(input("make a guess: "))
        attempts = check_guess(guessed_number, answer, attempts)
        if attempts == 0:
            print("you have run out of guesses, you lose")
            return
        elif guessed_number != answer:
            print("guess again")
    print("you have guessed the number")