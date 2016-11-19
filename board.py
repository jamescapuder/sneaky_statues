
from collections import deque
from copy import deepcopy

import piece

class Board:
    board = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, players=None):
        self.leaf = False
        self.scores = {}
        if players is None:
            self.players = {"one": deque(maxlen=4), "two": deque(maxlen=4)}
            self.scores["one"] = None
            self.scores["two"] = None
        else:
            self.players = deepcopy(players)
            self.scores["one"] = score(self.players["one"])
            self.scores["two"] = score(self.players["two"])
            if self.scores["one"] == 4 or self.scores["two"] == 4:
                self.leaf = True
        self.children = []

    def place_piece(self, statue):
        self.players[statue.player].append(statue)

    def find_children(self, statue_num):
        possible_boards = []
        for y in range(7):
            for x in range(y+1):
                if is_valid_move((x, y), self.players):
                    statue = piece.Piece(statue_num, (x, y))
                    temp = Board(self.players)
                    temp.place_piece(statue)
                    possible_boards.append(temp)
        self.children = possible_boards

    def __str__(self):
        pieces_played = list(self.players["one"])+list(self.players["two"])
        for statue in pieces_played:
            Board.board[statue.y][statue.x] = statue.num
        printstr = ""
        for i in range(0, len(Board.board)):
            row = ''
            for j in Board.board[i]:
                row += str(j)+" "
            printstr += '{:^16}'.format(row)
            printstr += '\n'
        return printstr

    def __repr__(self, level=0):
        ret = "\t" * (level)
        ret += "player one: "
        for statue in self.players["one"]:
            ret += str(statue) + ", "
        ret += "player two: "
        for statue in self.players["two"]:
            ret += str(statue) + ", "
        ret += "\n"
        if self.children:
            for child in self.children:
                ret += child.__repr__(level + 1)
        return ret

def is_valid_move(xycord, players):
    if xycord > (6, 6):
        return False
    if xycord[0] > xycord[1]:
        return False
    for statue in list(players["one"]) + list(players["two"]):
        if xycord == statue.xy:
            return False
    return True

def max_run(pieces):
    count, max_r = 1, 1
    for i in range(len(pieces)-1):
        if pieces[i] + 1 == pieces[i+1]:
            count += 1
            if count > max_r:
                max_r = count
        else:
            count = 1
    return max_r

def score(player):
    player_x = sorted(player, key=lambda statue: statue.x)
    player_y = sorted(player, key=lambda statue: statue.y)
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

# def tree(root, start, max_depth):
#     if start == max_depth:
#         return root
#     else:
#         node = board.Board()
#         node.find_children(start)
#         for child in node.children:
#             tree(child, start+1, max_depth)
