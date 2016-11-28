
def minimax(root, move, player="one"):
    root.find_children(move, 2)
    scores = root.score_children(player)
    max_index = scores.index(max(scores))
    return root.children[max_index]


