"""Module with main logic of game-progression."""

import prompt
import random
from brain_games.lib.greeting import greet_user
from brain_games.lib.answer_examenation import answer_exam
from brain_games.lib.calculations import progression


def game_progression():
    name = greet_user()
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        start = random.randint(1, 20)
        difference = random.randint(1, 10)
        length = random.randint(5, 10)
        question = random.randint(1, length - 2)
        progr = progression(start, difference, length)
        answer = progr[question]
        progr[question] = '...'
        print('Question:', *progr)
        user_answer = int(prompt.string('Your answer:'))
        counter = answer_exam(answer, user_answer, counter, name)


def main():
    print('This is library file. It should be imported.')


if __name__ == '__main__':
    main()
