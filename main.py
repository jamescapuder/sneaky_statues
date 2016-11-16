import unittest
import board
import minimax

class BoardTest(unittest.TestCase):
    def testBoard(self):
        root = board.Board()
        # children = root.get_possible_moves("1")
        # print(children)
        # self.assertTrue(len(children) != 27)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()


