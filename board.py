from collections import deque
from copy import deepcopy

import piece

class Board:

    def __init__(self, players=None):
        self.leaf = False
        self.scores = {}
        self.children = []
        if players is None:
            self.players = {"one": deque(maxlen=4), "two": deque(maxlen=4)}
            self.scores["one"] = 0
            self.scores["two"] = 0
        else:
            self.players = deepcopy(players)
            self.scores["one"] = score(self.players["one"])
            self.scores["two"] = score(self.players["two"])
            if self.scores["one"] == 4 or self.scores["two"] == 4:
                self.leaf = True

    def place_piece(self, statue):
        self.players[statue.player].append(statue)
        self.scores["one"] = score(self.players["one"])
        self.scores["two"] = score(self.players["two"])
        if self.scores["one"] == 4 or self.scores["two"] == 4:
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
                    if depth > 1:
                        temp.find_children(next_move(statue_num), depth - 1)
        self.children = possible_boards
        return self.children

    #gets score of all boards under this one, with respect to @player
    def score_children(self, player, depth=1):
        opponent = "one"
        if player == "one":
            opponent = "two"
        if not self.children:
            return self.scores[player] - self.scores[opponent]
        total = 0
        if depth == 1:
            lst = []
            for child in self.children:
                lst.append(child.score_children(player, depth + 1) + (self.scores[player] \
                                                                      - self.scores[opponent]))
            return lst
        for child in self.children:
            total += child.score_children(player, depth + 1)
        return total

    def __str__(self):
        board = [[(0,0)], [(0,1), (1,1)], [(0,2), (1,2), (2,2)], [(0,3), (1,3), (2,3), (3,3)], [(0,4), (1,4), (2,4), (3,4), (4,4)],
                 [(0,5), (1,5), (2,5), (3,5), (4,5), (5,5)], [(0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6)]]
        pieces_played = list(self.players["one"])+list(self.players["two"])
        for statue in pieces_played:
            board[statue.y][statue.x] = "(x, "+ str(statue.num) + ")"
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
        ret += str(self.scores["one"])
        ret += " player one: "
        for statue in self.players["one"]:
            ret += str(statue) + ", "
        ret += str(self.scores["two"])
        ret += " player two: "
        for statue in self.players["two"]:
            ret += str(statue) + ", "
        ret += "\n"
        if self.children:
            for child in self.children:
                ret += child.__repr__(level + 1)
        return ret

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



























































