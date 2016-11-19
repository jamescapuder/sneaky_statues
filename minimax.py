
def minimax(root, player, piece, depth=2):
    opponent = "one"
    if player == "one":
        opponent = "two"

    if depth==0:
        return root.scores[player] - root.scores[opponent]
    if root.leaf:
        return 4 if max(root.scores, key=root.scores.get) == player else -4
    else:
        best = None
        root.find_children(piece)
        for move in root.children:
            score = root.scores[player]-root.scores[opponent]
            score += minimax(move, player, piece+1, depth-1)
            if score > best:
                best = score
        return best