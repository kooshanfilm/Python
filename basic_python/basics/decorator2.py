def new_dectorator(func):
    def wrap_func():
        print("start")
        func()
        print("end after func")
    return wrap_func


@new_dectorator
def func_need_dec():
    print("this func needs decorator")

func_need_dec()

#another example:
"""
def my_decorator(func):
    def function_that_runs_func():
        print("start")
        func()
        print("end")

    return function_that_runs_func


@my_decorator
def my_function():
    print("inside")

my_function()

"""
