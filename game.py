
import random
import sys

import piece
import board

def run_game():
    player = "one"
    comp = "two"
    turn = 0
    root = board.Board()
    while True:
        turn = board.next_move(turn)
        next_piece = piece.Piece(turn)

        if next_piece.player == player:
            print("Turn: ", turn)
            print()
            print(root)
            inpt = input("Your move x,y: ")
            inpt = tuple(int(x) for x in inpt.split(","))
            next_piece.set(inpt)
            root.place_piece(next_piece)
        else:
            root.find_children(turn, 3)
            scores = root.score_children(comp)
            max_value = max(scores)
            indices = [i for i, v in enumerate(scores) if v == max_value]
            index = random.choice(indices)
            root = root.children[index]

        if root.scores["one"] == 4:
            print("Player one wins! ")
            sys.exit(1)
        if root.scores["two"] == 4:
            print("Player two wins! ")
            sys.exit(1)

run_game()
