
from collections import deque
from copy import deepcopy

import piece

def is_valid_move(xycord, players):
    if xycord > (6, 6):
        return False
    if xycord[0] > xycord[1]:
        return False
    for statue in players["one"] + players["two"]:
        if xycord == statue.xy:
            return False
    return True

def is_winner(players):
    # check horizontal win
    


    # check forward diagonal


    
    # check backward diagonal 



    return False

class Board:

    def __init__(self, players=None):
        if players is None:
            self.players = {"one": deque(maxlen=4), "two": deque(maxlen=4)}
        else:
            self.players = deepcopy(players)

    def place_piece(self, statue):
        self.players[statue.player].append(statue)

    def get_possible_moves(self, statue_num):
        possible_boards = []
        for y in range(7):
            for x in range(y+1):
                if is_valid_move((x, y), self.players):
                    statue = piece.Piece(statue_num, (x, y))
                    temp = Board(self.players)
                    temp.place_piece(statue)
                    possible_boards.append(temp)
        return possible_boards

    def __str__(self):
        board = [[0], [0, 0], [0,0,0], [0,0,0,0], [0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0,0]]
        pieces_played = self.players["one"] + self.players["two"]
        for piece in pieces_played:
            board[piece.y][piece.x] = piece.num
        printstr = ""
        for i in range(0, len(board)):
            row = ''
            for j in board[i]:
                row += str(j)+" "
            printstr += '{:^16}'.format(row)
            printstr += '\n'
        return printstr
