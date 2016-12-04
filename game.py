
import sys

import piece
import board
import network

def player_turn(turn, brd):
    print("Turn: ", turn, "\n")
    print(brd)
    inpt = input("Your move x,y: ")
    inpt = tuple(int(x) for x in inpt.split(","))
    next_piece = piece.Piece(turn, inpt)
    brd.place_piece(next_piece)
    return brd

def computer_turn(turn, brd, comp):
    brd.find_children(turn, 3)
    best_score = float("-inf")
    best_board = None
    for child in brd.children:
        if child.score_two - child.score_one > best_score:
            best_score = child.score_two - child.score_one
            best_board = child
    return best_board

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
            brd = computer_turn(turn, brd, comp)
        if brd.score_one == 4:
            print("Player one wins! ")
            sys.exit(1)
        if brd.score_two == 4:
            print("Player two wins! ")
            sys.exit(1)

run_game()
