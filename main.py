import time
import unittest
import board
import minimax
import piece
from collections import deque

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
        print()
        start = time.time()
        x = deque([piece.Piece(1,(1,1)),piece.Piece(3,(2,2)),piece.Piece(5,(5,6)),piece.Piece(7,(1,2))],maxlen=4)
        y = deque([piece.Piece(2,(4,4)),piece.Piece(4,(0,0)),piece.Piece(6,(2,4)),piece.Piece(8,(1,3))],maxlen=4)
        players = {"one": x, "two": y}
        root = board.Board(players)
        root.find_children(1)
        for child in root.children:
            child.find_children(2)
        print(repr(root))
        end = time.time()
        print(end-start)

def main():
    unittest.main()

if __name__ == "__main__":
    main()



