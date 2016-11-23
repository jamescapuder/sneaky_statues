import board
from collections import deque
import piece

def minimax(root, player, move, depth=2):
    opponent = "one"
    if player == "one":
        opponent = "two"
    print("\t"*depth, root.scores[player], root.scores[opponent], repr(root))
    if depth == 0:
        return root.scores[player] - root.scores[opponent]
    if root.leaf:
        return 4 if max(root.scores, key=root.scores.get) == player else -4
    else:
        best = 0
        for node in root.find_children(move):
            score = root.scores[player]-root.scores[opponent]
            score += minimax(node, player, move+1, depth-1)
            if score > best:
                best = score
        return best

def main():
    p1 = deque([piece.Piece(1,(0,2)),piece.Piece(3,(1,2)),piece.Piece(5,(2,2)),piece.Piece(7,(3,3))],maxlen=4)
    p2 = deque([piece.Piece(2,(3,4)),piece.Piece(4,(1,4)),piece.Piece(6,(2,5)),piece.Piece(8,(3,6))],maxlen=4)
    players = {"one":p1, "two":p2}
    b = board.Board(players)
    print(minimax(b,"one",1))

if __name__ == "__main__":
    main()
