def new_dectorator(func):
    def wrap_func():
        print("Start")

        func()

        print("END after func")

    return wrap_func()

@new_dectorator
def func_need_dec():
    print("this func needs dec")

func_need_dec()