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
        print(getsize(root))
        end = time.time()
        print(end-start)

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

def tree(root, depth):
    pass

def main():
    unittest.main()

if __name__ == "__main__":
    main()
