"""Library midule for examenation of answer"""


def answer_exam(answer, user_answer, counter):
    """Function for examine the answer to be correct"""
    if answer == user_answer:
        print('Correct!')
        return counter + 1
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
        return 3


def main():
    """Main function of module"""
    print("This is library mudule. Should be imported")


if __name__ == '__main__':
    main()

