import sys
import random
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

def minimax_turn(player, turn, brd):
    brd.find_children(turn, 3)
    best_score = float("-inf")
    best_board = None
    if player == 1:
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
    else:
        for child in brd.children:
            if child.score_two == 4:
                return child
            if child.score_two - child.score_one > best_score:
                for next_gen in childb.children:
                    if next_gen.longest_run_1 == 4:
                        break
                else:
                    best_score = child.score_two - child.score_one
                    best_board = child
    if best_board is None:
        return -1
    return best_board


def player_one(turn, brd, net):
    brd.focused_find_children(turn , 3, net)
    best_score = float("-inf")
    best_board = None
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
                best_score = child.score_one - child.score_two
                best_board = child
    if same == len(brd.children) - 1:
        return random.choice(brd.children) 
    return best_board

def player_two(turn, brd, net):
    brd.focused_find_children(turn , 3, net)
    best_score = float("-inf")
    best_board = None
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
                best_score = child.score_two - child.score_one
                best_board = child
    if same == len(brd.children) - 1:
        return random.choice(brd.children) 
    return best_board

def game_over(brd=None):
    score = {"one": 0, "two": 0}
    if brd is None:
        return score
    if brd.longest_run_1 == 4:
        score["one"] = 1
        score["two"] = -1
    else:
        score["two"] = 1
        score["one"] = -1
    return score

def comp_stomp(net_1, net_2):
    brd = board.Board()
    turn = 0 #1-8
    turn_count = 0
    while turn_count < 40:
        print(brd)
        turn = board.next_move(turn)
        turn_count += 1
        if turn % 2 == 1:
            brd = player_one(turn, brd, net_1)
        else:
            brd = player_two(turn, brd, net_2)
        if brd.longest_run_1 == 4 or brd.longest_run_2 == 4:
            print(brd)
            print(game_over(brd))
            return game_over(brd)
    return game_over()

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
            brd = minimax_turn(2, turn, brd)
        if brd.score_one == 4:
            print("Player one wins! ")
            sys.exit(1)
        if brd.score_two == 4:
            print("Player two wins! ")
            sys.exit(1)


if __name__ == "__main__":
    run_game()
