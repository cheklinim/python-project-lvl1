"""Calculations library module."""


def is_even(x):
    return not (x % 2)


def gcd(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return (a + b)


def main():
    print('This is library module. It should be imported')


if __name__ == '__main__':
    main()
