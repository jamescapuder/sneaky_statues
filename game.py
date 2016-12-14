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
                for next_gen in child.children:
                    if next_gen.score_one == 4:
                        break
                else:
                    best_score = child.score_two - child.score_one
                    best_board = child
    if best_board is None:
        return -1
    return best_board

def focus_tree_turn(player, turn, brd, net):
    brd.focused_find_children(turn, 4, net)
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
                for next_gen in child.children:
                    if next_gen.score_one == 4:
                        break
                else:
                    best_score = child.score_two - child.score_one
                    best_board = child
    if best_board is None:
        return -1
    return best_board

def comp_stomp(net_1, net_2=None):
    brd = board.Board()
    first = piece.Piece(1, (1, 2))
    brd.place_piece(first)
    turn = 1
    turn_count = 1
    while True:
        turn = board.next_move(turn)
        turn_count += 1
        if turn % 2 == 1:
            brd = focus_tree_turn(1, turn, brd, net_1)
            if brd == -1:
                return -1, turn_count
        else:
            if net_2 is not None:
                brd = focus_tree_turn(2, turn, brd, net_2)
                if brd == -1:
                    return 1, turn_count
            else:
                brd = minimax_turn(2, turn, brd)
                if brd == -1:
                    return 1, turn_count

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
























