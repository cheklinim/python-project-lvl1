"""Module with main logic of game-calc."""

import prompt
import random
from brain_games.lib.greeting import greet_user
from brain_games.lib.answer_examenation import answer_exam


def game_calc():
    name = greet_user()
    print('Calculate the expression:')
    counter = 0
    while counter < 3:
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        operations = '+-*'
        operation = operations[random.randint(0, 2)]
        expression = str(num1) + operation + str(num2)
        answer = eval(expression)
        print(expression)
        user_answer = int(prompt.string('Your answer:'))
        counter = answer_exam(answer, user_answer, counter, name)


def main():
    print('This is library file. It should be imported.')


if __name__ == '__main__':
    main()
