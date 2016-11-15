
class Tree:
    """
    tree where each node is a board
    """
    def __init__(self, root):
        self.root = root
        self.next_piece = self.get_next_piece()
        self.children = self.find_children()

    def get_next_piece(self):
        self.next_piece = self.root.turn % 8
        if self.next_piece == 0:
            self.next_piece = "8"
        else:
            self.next_piece = str(self.next_piece)
        return self.next_piece

    def find_children(self):
        self.get_next_piece()
        self.children = self.root.get_possible_moves(self.next_piece)
        return self.children

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
