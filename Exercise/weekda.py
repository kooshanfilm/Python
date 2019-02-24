import unittest


def sleep_in(weekday, vacation):

    if weekday == False or vacation == True:
        return True
    else:
        return False

class Weekday(unittest.TestCase):

    def test_sleep_in(self):
        self.assertEqual(sleep_in(False,True),True)


if __name__ == '__main__':
    unittest.main()