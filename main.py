import unittest
import board
import minimax

class BoardTest(unittest.TestCase):
    @unittest.skip("skipping")
    def testBoard(self):
        root = board.Board()
        children = root.get_possible_moves("1")
        for child in children:
            print(child[0])
            print(child[1])

class TreeTest(unittest.TestCase):
    @unittest.skip("skipping")
    def testTree(self):
        root = board.Board()
        tree = minimax.Tree(root)
        tree.find_children()
        for child in tree.children:
            print(child[0])
            print(child[1])
            
def main():
    unittest.main()

if __name__ == "__main__":
    main()


