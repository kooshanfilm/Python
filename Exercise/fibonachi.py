


def fib(number):

    if number >= 3:
        result = fib(number-1) + fib(number-2)
        return result
    else:
        return 1




print fib(2)


