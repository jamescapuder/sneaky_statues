
from collections import deque
from copy import deepcopy

import piece

def is_valid_move(xycord, players):
    if xycord > (6, 6):
        return False
    if xycord[0] > xycord[1]:
        return False
    for statue in list(players["one"]) + list(players["two"]):
        if xycord == statue.xy:
            return False
    return True

def is_winner(player):
    # player_x = [x[1] for x in list(player)]
    # player_y = [x[0] for x in list(player)]
    # if sorted(player_x)==range(min(player_x), max(player_x)+1):
    # check horizontal win
    # check forward diagonal
    # check backward diagonal
    return False

class Board:
    board = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, players=None):
        if players is None:
            self.players = {"one": deque(maxlen=4), "two": deque(maxlen=4)}
        else:
            self.players = deepcopy(players)
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

