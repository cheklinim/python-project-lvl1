"""Module with main logic of game-gcd."""

import prompt
import random
from brain_games.lib.greeting import greet_user
from brain_games.lib.answer_examenation import answer_exam
from brain_games.lib.calculations import gcd


def game_gcd():
    name = greet_user()
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        answer = gcd(num1, num2)
        print(f'Question: {num1} {num2}')
        user_answer = int(prompt.string('Your answer:'))
        counter = answer_exam(answer, user_answer, counter, name)


def main():
    print('This is library file. It should be imported.')


if __name__ == '__main__':
    main()
