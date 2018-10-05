



def fib(n,my_dict = {}):

    if n == 0 or n == 1:
        return 1
    try:
        return my_dict[n]
    except KeyError:
        result = fib(n-1) + fib(n-2)
        my_dict[n] = result
        return result


print(fib(99))
