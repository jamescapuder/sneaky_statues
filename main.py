import sys
import time
import unittest

from numbers import Number
from collections import Set, Mapping, deque

import board
import minimax
import piece

try: # Python 2
    zero_depth_bases = (basestring, Number, xrange, bytearray)
    iteritems = 'iteritems'
except NameError: # Python 3
    zero_depth_bases = (str, bytes, Number, range, bytearray)
    iteritems = 'items'

def getsize(obj_0):
    """Recursively iterate to sum size of object & members."""
    def inner(obj, _seen_ids=set()):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, zero_depth_bases):
            pass # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, iteritems):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, iteritems)())
        # Check for custom object instances - may subclass above too
        if hasattr(obj, '__dict__'):
            size += inner(vars(obj))
        if hasattr(obj, '__slots__'): # can have __slots__ with __dict__
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        return size
    return inner(obj_0)

class BoardTest(unittest.TestCase):
    @unittest.skip("skipping")
    def testMaxRun(self):
        print("testMaxRun")
        test_1 = [1, 2, 3, 4]
        self.assertEqual(board.max_run(test_1), 4)
        test_2 = [8, 2, 3, 4]
        self.assertEqual(board.max_run(test_2), 3)
        test_3 = [9, 1, 2, 8]
        self.assertEqual(board.max_run(test_3), 2)
        test_4 = [1, 3, 5, 7]
        self.assertEqual(board.max_run(test_4), 1)

    @unittest.skip("skipping")
    def testScore(self):
        print("testScore")
        p1 = deque([piece.Piece(1,(0,2)),piece.Piece(3,(1,2)),piece.Piece(5,(2,2)),piece.Piece(7,(3,3))],maxlen=4)
        p2 = deque([piece.Piece(2,(0,3)),piece.Piece(4,(1,4)),piece.Piece(6,(2,5)),piece.Piece(8,(3,6))],maxlen=4)
        self.assertEqual(board.score(p1), 3)
        self.assertEqual(board.score(p2), 4)
        p1 = deque([piece.Piece(1,(3,5)),piece.Piece(3,(4,5)),piece.Piece(5,(2,4)),piece.Piece(7,(3,4))],maxlen=4)
        p2 = deque([piece.Piece(2,(1,3)),piece.Piece(4,(1,4)),piece.Piece(6,(1,5)),piece.Piece(8,(2,6))],maxlen=4)
        self.assertEqual(board.score(p1), 2)
        self.assertEqual(board.score(p2), 3)
        p1 = deque([piece.Piece(1,(0,1)),piece.Piece(3,(2,3)),piece.Piece(5,(4,5)),piece.Piece(7,(5,6))],maxlen=4)
        p2 = deque([piece.Piece(2,(0,6)),piece.Piece(4,(1,5)),piece.Piece(6,(2,4)),piece.Piece(8,(3,3))],maxlen=4)
        self.assertEqual(board.score(p1), 2)
        self.assertEqual(board.score(p2), 1)

class TreeTest(unittest.TestCase):
    #@unittest.skip("skipping")
    def testTree(self):
        print()

        
        x = deque([piece.Piece(1,(0,0)),piece.Piece(3,(2,2)),piece.Piece(5,(1,1)),piece.Piece(7,(4,4))],maxlen=4)
        y = deque([piece.Piece(2,(0,6)),piece.Piece(4,(0,4)),piece.Piece(6,(2,4)),piece.Piece(8,(3,4))],maxlen=4)
        players = {"one": x, "two": y}

        root = board.Board(players)
        root.find_children(1,2)
        print(repr(root))
        end = time.time()
#        print(end-start)
#        print(getsize(root))

        
def main():
    unittest.main()

if __name__ == "__main__":
    main()



















































