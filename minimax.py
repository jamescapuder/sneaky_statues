"""
a tree where each node is a board
"""

class Tree:
    def __init__(self, root, next_piece):
        self.root = root
        self.next_piece = next_piece
        self.children = None

    def find_children(self):
        self.children = self.root.get_possible_moves(self.next_piece)

    def minimax(self):
        """ does nothing lol """
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

    def is_complete(self):
        pass
