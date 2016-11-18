
def minimax(self):
    node = self.root
    if node.complete():
        if node.X_won():
            return -1
        elif node.O_won():
            return 1
    best = None
    for move in self.children:
        node.set_position(move, player)
        val = self.minimax(node, get_enemy(player), alpha, beta)
        node.make_move(move, None)
        if player == 'O':
            if val > best:
                best = val
        else:
            if val < best:
                best = val
    return best
