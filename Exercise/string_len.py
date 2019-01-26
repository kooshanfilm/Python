# find the lenght of the string




def find_len(num):

    count = 0
    for i in num:
        count+=1

    return count


def test_find_len():

    assert find_len("a") == 1
    assert find_len("koushan") == 7


test_find_len()