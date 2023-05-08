"""Module for user greeting."""

import prompt


def greet_user():
    """Greet a user."""
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}!')
    return name


if __name__ == '__main__':
    print('This is library file. It should be imported')
