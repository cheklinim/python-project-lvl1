import prompt


def welcome_user():
    name = prompt.string('May I have your name?\n')
    print(f"Hello, {name}!")


if __name__ == "__main__":
    print("This file have to be imported!")

