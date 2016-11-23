
def minimax(root, player, move, depth=2):
    opponent = "one"
    if player == "one":
        opponent = "two"

    if depth==0:
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