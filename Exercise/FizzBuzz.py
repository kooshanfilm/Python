


def fizzbuzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuuz"
    elif num % 3 == 0 or num % 5 == 0:
         return "Fizz"
    else:
        return num


print (fizzbuzz(7))