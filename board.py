
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
    #len(set(iterator)) <= 1
    player_x = [statue.x for statue in player]
    player_y = [statue.y for statue in player]
    player_x.sort()
    player_y.sort()
    max_score = []
    max_x = max_run(player_x)
    max_y = max_run(player_y)
    print("x: ", player_x)
    print("y: ", player_y)
    if len(set(player_x)) <= 1:
        max_score.append(max_y)
    if len(set(player_y)) <= 1:
        max_score.append(max_x)
    if (max_x and max_y) >=3:
        max_score.append(min([max_x, max_y]))
    return max(max_score)
    #if len(set(player_y)) <= 1 and player_x == list(range(min(player_x),max(player_x)+1)):
    # if sorted(player_x)==range(min(player_x), max(player_x)+1):
    # check horizontal win
    # check forward diagonal
    # check backward diagonal
    # return False

# def tree(root, start, max_depth):
#     if start == max_depth:
#         return root
#     else:
#         node = board.Board()
#         node.find_children(start)
#         for child in node.children:
#             tree(child, start+1, max_depth)
