
import unittest
from python_qa_exercise import  *


class TestTicTacToe(unittest.TestCase):
    call = TicTacToe()
    def test_resolve_turn(self):
        self.assertEqual(call.resolve_turn(),"b")




if __name__ == '__main__':
    unittest.main()