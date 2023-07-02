"""Module with main logic of game-prime."""

import prompt
import random
from brain_games.lib.greeting import greet_user
from brain_games.lib.answer_examenation import answer_exam
from brain_games.lib.calculations import is_prime


def game_prime():
    name = greet_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(2, 100)
        answer = 'yes' if is_prime(number) else 'no'
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer:')
        counter = answer_exam(answer, user_answer, counter, name)


def main():
    print('This is library file. It should be imported.')


if __name__ == '__main__':
    main()
