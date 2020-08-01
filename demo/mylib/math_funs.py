def iseven(n):
    """
    Returns true if given number is even number
    :param n: number to test
    :return: True for even numbers and False for odd numbers
    """
    return n % 2 == 0


def isprime(n):
    pass


def ispositive(n):
    return n > 0


print("Name = ", __name__)
if __name__ == '__main__':
    print("Math funs is executed!")
else:
    print("Math funs is imported!")
