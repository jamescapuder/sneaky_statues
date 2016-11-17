import time
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
    #@unittest.skip("skipping")
    def testTree(self):
        start = time.time()
        root = board.Board()
        tree = minimax.Tree(root)
        tree.find_children()
        for child in tree.children:
            child.find_children()
            for x in child.children:
                x.find_children()
        end = time.time()
        print(end-start)
       
def main():
    unittest.main()

if __name__ == "__main__":
    main()


