from collections import deque
from copy import deepcopy
import numpy as np

import piece
import network

class Board:

    def __init__(self, players=None):
        self.rating = -1
        self.leaf = False
        self.children = []
        if players is None:
            self.players = {"one": deque(maxlen=4), "two": deque(maxlen=4)}
            self.score_one = 0
            self.score_two = 0
            self.longest_run_1 = 0
            self.longest_run_2 = 0
        else:
            self.players = deepcopy(players)
            self.score_one = score(self.players["one"])
            self.score_two = score(self.players["two"])
            self.longest_run_1 = self.score_one
            self.longest_run_2 = self.score_two
            if self.score_one == 4 or self.score_two == 4:
                self.leaf = True

    def place_piece(self, statue):
        self.players[statue.player].append(statue)
        self.score_one = score(self.players["one"])
        self.score_two = score(self.players["two"])
        self.longest_run_1 = self.score_one
        self.longest_run_2 = self.score_two
        if self.score_one == 4 or self.score_two == 4:
            self.leaf = True

    def find_children(self, statue_num, depth):
        possible_boards = []
        for y in range(7):
            for x in range(y+1):
                if is_valid_move((x, y), self.players):
                    statue = piece.Piece(statue_num, (x, y))
                    temp = Board(self.players)
                    temp.place_piece(statue)
                    possible_boards.append(temp)
                    if depth > 1 and not temp.leaf:
                        temp.find_children(next_move(statue_num), depth - 1)
                        for child in temp.children:
                            temp.score_one += child.score_one
                            temp.score_two += child.score_two
        self.children = possible_boards
        return self.children

    def focused_find_children(self, statue_num, depth, net):
        self.find_children(statue_num, 0)
        pruned = test_children(self.children, statue_num, net)
        for child in pruned:
            if depth > 1 and not child.leaf:
                child.focused_find_children(next_move(statue_num), depth - 1, net)
                for gchild in child.children:
                    child.score_one += gchild.score_one
                    child.score_two += gchild.score_two
        self.children = pruned
        return self.children

    def __str__(self):
        board = [["(0,0)"], ["(0,1)", "(1,1)"], ["(0,2)", "(1,2)", "(2,2)"],
                 ["(0,3)", "(1,3)", "(2,3)", "(3,3)"],
                 ["(0,4)", "(1,4)", "(2,4)", "(3,4)", "(4,4)"],
                 ["(0,5)", "(1,5)", "(2,5)", "(3,5)", "(4,5)", "(5,5)"],
                 ["(0,6)", "(1,6)", "(2,6)", "(3,6)", "(4,6)", "(5,6)", "(6,6)"]]
        for statue in list(self.players["one"]):
            board[statue.y][statue.x] = "(X," + \
                                        str(statue.num) + ")"
        for statue in list(self.players["two"]):
            board[statue.y][statue.x] = "(Y," + \
                                        str(statue.num) + ")"
        printstr = ""
        for i in range(0, len(board)):
            row = ''
            for j in board[i]:
                row += str(j)+""
            printstr += '{:^80}'.format(row)
            printstr += '\n'
        return printstr

    def __repr__(self, level=0):
        ret = "\t" * (level)
        ret += str(self.score_one)
        ret += " player one: "
        for statue in self.players["one"]:
            ret += str(statue) + ", "
        ret += str(self.score_two)
        ret += " player two: "
        for statue in self.players["two"]:
            ret += str(statue) + ", "
        ret += "\n"
        if self.children:
            for child in self.children:
                ret += child.__repr__(level + 1)
        return ret


def test_children(boards, cur_piece, net):
    for brd in boards:
        brd.rating = test_child(brd, cur_piece, net)
    boards.sort(key=lambda x: x.rating)
    return boards[int(len(boards)*.30):]


# run the board thru the net
def test_child(child, cur_piece, net):
    LAYER_1, LAYER_2, LAYER_3 = net[0], net[1], net[2]
    pieces = list(child.players['one']) + list(child.players['two'])
    pieces.sort(key=lambda x: x.num)
    index = 0
    inputs = np.zeros((17, 1))
    for piece in pieces:
        inputs[index] = piece.x
        inputs[index+1] = piece.y
        index += 2
    inputs[16] = cur_piece
    inputs = network.normalize(inputs)
    inputs[16] = (inputs[16] * 6) / 8 # the current piece is the only input not from 0-6 so we re-normalize it for 1-8
    out = LAYER_3.feed(LAYER_2.feed(LAYER_1.feed(inputs)))
    return out[0]


def next_move(current):
    n_move = (current + 1) % 8
    if n_move == 0:
        n_move = 8
    return n_move


def is_valid_move(xycord, players):
    if xycord > (6, 6):
        return False
    if xycord[0] > xycord[1]:
        return False
    for statue in list(players["one"]) + list(players["two"]):
        if xycord == statue.xy:
            return False
    return True


# checks how many pieces player has in a row
def score(player):
    player_x = sorted(player, key=lambda statue: statue.xy)
    player_y = sorted(player, key=lambda statue: statue.xy[::-1])
    max_score = [0]
    count = 1
    for cur_s, next_s in zip(player_x, player_x[1:]):
        if cur_s.x + 1 == next_s.x and cur_s.y == next_s.y:
            count += 1
        else:
            max_score.append(count)
            count = 1
    max_score.append(count)
    count = 1
    for cur_s, next_s in zip(player_y, player_y[1:]):
        if cur_s.y + 1 == next_s.y and cur_s.x == next_s.x:
            count += 1
        else:
            max_score.append(count)
            count = 1
    max_score.append(count)
    count = 1
    for cur_s, next_s in zip(player_y, player_y[1:]):
        if cur_s.y + 1 == next_s.y and cur_s.x + 1 == next_s.x:
            count += 1
        else:
            max_score.append(count)
            count = 1
    max_score.append(count)

    return max(max_score)
