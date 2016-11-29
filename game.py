
import random
import sys

import piece
import board

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
    scores = brd.score_children(comp)
    max_value = max(scores)
    indices = [i for i, v in enumerate(scores) if v == max_value]
    index = random.choice(indices)
    brd = brd.children[index]
    return brd

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
        if brd.scores["one"] == 4:
            print("Player one wins! ")
            sys.exit(1)
        if brd.scores["two"] == 4:
            print("Player two wins! ")
            sys.exit(1)

run_game()
