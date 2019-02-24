# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).
#


# combo_string('Hello', 'hi')  'hiHellohi'
# combo_string('hi', 'Hello') 'hiHellohi'
# combo_string('aaa', 'b') 'baaab'


def combo_string(a, b):
    a_l = len(a)
    b_l = len(b)
    if a_l > b_l:
        return b+a+b
    elif b_l > a_l:
        return a+b+a

print combo_string("hello","hi")