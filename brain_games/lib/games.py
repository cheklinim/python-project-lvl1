"""Module with main logic of games."""

import prompt
import random
from brain_games.lib.greeting import greet_user
from brain_games.lib.calculations import is_even


def game_even():
    name = greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(1, 99)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer:')
        answer = 'yes' if is_even(number) else 'no'
        if answer == user_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break


def game_calc():
    pass


def main():
    print('This is library file. It should be imported.')


if __name__ == '__main__':
    main()
