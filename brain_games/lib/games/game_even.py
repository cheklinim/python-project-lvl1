"""Module with main logic of game-even."""

import prompt
import random
from brain_games.lib.greeting import greet_user
from brain_games.lib.calculations import is_even
from brain_games.lib.answer_examenation import answer_exam


def game_even():
    name = greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(1, 99)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer:')
        answer = 'yes' if is_even(number) else 'no'
        counter = answer_exam(answer, user_answer, counter, name)


def main():
    print('This is library file. It should be imported.')


if __name__ == '__main__':
    main()
