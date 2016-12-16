import sys
import random
import numpy

import piece
import board
import network


# player prompt
def player_turn(turn, brd):
    print("Turn: ", turn, "\n")
    print(brd)
    inpt = input("Your move x,y: ")
    inpt = tuple(int(x) for x in inpt.split(","))
    next_piece = piece.Piece(turn, inpt)
    brd.place_piece(next_piece)
    return brd


# minimax sans focus net
def minimax_turn_one(player, turn, brd):
    brd.find_children(turn, 3)
    best_score = brd.children[0].score_one - brd.children[0].score_two
    best_board = brd.children[0]
    same = 0
    for child in brd.children:
        if child.longest_run_1 == 4:
            return child
        score = child.score_one - child.score_two
        if score == best_score:
            same += 1
        if score > best_score:
            for gchild in child.children:
                if gchild.longest_run_2 == 4:
                    break
            else:
                best_score = score
                best_board = child
    if same == len(brd.children) - 1:
        return random.choice(brd.children) 
    return best_board

def minimax_turn_two(player, turn, brd):
    brd.find_children(turn, 3)
    best_score = brd.children[0].score_two - brd.children[0].score_one
    best_board = brd.children[0]
    same = 0
    for child in brd.children:
        if child.longest_run_2 == 4:
            return child
        score = child.score_two - child.score_one
        if score == best_score:
            same += 1
        if score > best_score:
            for gchild in child.children:
                if gchild.longest_run_1 == 4:
                    break
            else:
                best_score = score
                best_board = child
    if same == len(brd.children) - 1:
        return random.choice(brd.children) 
    return best_board


# focus net, for player one
def player_one(turn, brd, net):
    brd.focused_find_children(turn , 3, net)
    best_score = brd.children[0].score_one - brd.children[0].score_two
    best_board = brd.children[0]
    same = 0
    for child in brd.children:
        if child.longest_run_1 == 4:
            return child
        score = child.score_one - child.score_two
        if score == best_score:
            same += 1
        if score > best_score:
            for gchild in child.children:
                if gchild.longest_run_2 == 4:
                    break
            else:
                best_score = score
                best_board = child
    if same == len(brd.children) - 1:
        return random.choice(brd.children) 
    return best_board


# focus net, for player two
def player_two(turn, brd, net):
    brd.focused_find_children(turn , 3, net)
    best_score = brd.children[0].score_two - brd.children[0].score_one
    best_board = brd.children[0]
    same = 0
    for child in brd.children:
        if child.longest_run_2 == 4:
            return child
        score = child.score_two - child.score_one
        if score == best_score:
            same += 1 
        if score > best_score:
            for gchild in child.children:
                if gchild.longest_run_1 == 4:
                    break
            else:
                best_score = score
                best_board = child
    if same == len(brd.children) - 1:
        return random.choice(brd.children)
    return best_board


# if the game is over return score
def game_over(brd=None):
    score = {"one": 0, "two": 0}
    if brd is None:
        return score
    elif brd.longest_run_1 == 4:
        score["one"] = 1
        score["two"] = -1
    elif brd.longest_run_2 == 4:
        score["two"] = 1
        score["one"] = -1
    return score


# two nets enter, one leaves as the champion 
def comp_stomp(net_1, net_2):
    brd = board.Board()
    turn = 0 #1-8
    turn_count = 0
    while turn_count < 40:
        turn = board.next_move(turn)
        turn_count += 1
        if turn % 2 == 1:
            brd = player_one(turn, brd, net_1)
        else:
            brd = player_two(turn, brd, net_2)
        if brd.longest_run_1 == 4 or brd.longest_run_2 == 4:
            print(game_over(brd))
            return game_over(brd)
    print(game_over())
    return game_over()


# net vs minimax, net first
def net_v_max(net):
    brd = board.Board()
    turn = 0 #1-8
    turn_count = 0
    while turn_count < 40:
        turn = board.next_move(turn)
        turn_count += 1
        if turn % 2 == 1:
            brd = player_one(turn, brd, net)
        else:
            brd = minimax_turn_two(2, turn, brd)
        if brd.longest_run_1 == 4 or brd.longest_run_2 == 4:
            print("net", game_over(brd))
            return game_over(brd)
    print("net", game_over())
    return game_over()


# net vs minimax, minimax first
def max_v_net(net):
    brd = board.Board()
    turn = 0 #1-8
    turn_count = 0
    while turn_count < 40:
        turn = board.next_move(turn)
        turn_count += 1
        if turn % 2 == 1:
            brd = minimax_turn_one(1, turn, brd)
        else:
            brd = player_two(turn, brd, net)            
        if brd.longest_run_1 == 4 or brd.longest_run_2 == 4:
            print("max", game_over(brd))
            return game_over(brd)
    print("max", game_over(brd))
    return game_over()


# for playing against the bot 
def run_game():
    net = network.load_network("pop4_gen10.npz")
    turn = 0
    turn_count = 0
    brd = board.Board()
    while turn_count < 40:
        turn = board.next_move(turn)
        turn_count += 1 
        if turn % 2 == 1:
            brd = player_turn(turn, brd)
        else:
#            brd = minimax_turn(2, turn, brd)
            brd = player_two(turn, brd, net)
        if brd.longest_run_1 == 4 or brd.longest_run_2 == 4:
            print(game_over(brd))
            return game_over(brd)
    return game_over()


if __name__ == "__main__":
    run_game()
