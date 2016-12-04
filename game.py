
import sys

import piece
import board
import network

PLAYER_ONE = 0
PLAYER_TWO = 0

def player_turn(turn, brd):
    print("Turn: ", turn, "\n")
    print(brd)
    inpt = input("Your move x,y: ")
    inpt = tuple(int(x) for x in inpt.split(","))
    next_piece = piece.Piece(turn, inpt)
    brd.place_piece(next_piece)
    return brd

def minimax_turn(turn, brd):
    brd.find_children(turn, 3)
    best_score = float("-inf")
    best_board = None
    for child in brd.children:
        if child.score_one == 4:
            return child
        if child.score_one - child.score_two > best_score:
            for next_gen in child.children:
                if next_gen.score_two == 4:
                    break
            else:
                best_score = child.score_two - child.score_one
                best_board = child
    if best_board is None:
        return -1
    return best_board

def focus_tree_turn(turn, brd):
    brd.focused_find_children(turn, 3)
    best_score = float("-inf")
    best_board = None
    for child in brd.children:
        if child.score_two == 4:
            return child
        if child.score_two - child.score_one > best_score:
            for next_gen in child.children:
                if next_gen.score_one == 4:
                    break
            else:
                best_score = child.score_two - child.score_one
                best_board = child
    if best_board is None:
        return -1
    return best_board

def comp_stomp():
    global PLAYER_ONE
    global PLAYER_TWO
    print(PLAYER_ONE, PLAYER_TWO)
    if PLAYER_TWO == 10 or PLAYER_ONE == 10:
        print(PLAYER_ONE, PLAYER_TWO)
    brd = board.Board()
    first = piece.Piece(1, (1, 2))
    brd.place_piece(first)
    turn = 1
    while True:
        turn = board.next_move(turn)
        print(turn)
        print(brd)
        if turn % 2 == 1:
            brd = minimax_turn(turn, brd)
            if brd == -1:
                PLAYER_TWO += 1
                comp_stomp()
        else:
            brd = focus_tree_turn(turn, brd)
            if brd == -1:
                PLAYER_ += 1
                comp_stomp()

def run_game():
    player = "one"
    comp = "two"
    turn = 0
    brd = board.Board()
    while True:
        turn = board.next_move(turn)
        if turn % 2 == 1:
            brd = player_turn(turn, brd)
        else:
            brd = minimax_turn(turn, brd)
        if brd.score_one == 4:
            print("Player one wins! ")
            sys.exit(1)
        if brd.score_two == 4:
            print("Player two wins! ")
            sys.exit(1)

comp_stomp()

































