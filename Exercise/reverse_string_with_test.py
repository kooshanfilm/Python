import unittest

def reverse_me(word):
    i = 0
    lenght = len(word)
    new_str = []
    while i < lenght:
        lenght -= 1
        new_str.append(word[lenght])
    return "".join(new_str)

class Mytest(unittest.TestCase):

    def test_reverse_me(self):
        self.assertEqual(reverse_me("abc"),"cba")


if __name__ == '__main__':
    unittest.main()

