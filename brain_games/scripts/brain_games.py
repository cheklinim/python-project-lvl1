#!/usr/bin/env python3

"""Main brain-games module."""

from brain_games.cli import welcome_user


def main():
    """Start the game."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
