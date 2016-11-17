
class Tree:

    def __init__(self, root):
        self.root = root
        self.height = 1
        self.children = []

    def get_next_piece(self):
        next_piece = self.height % 8
        if next_piece == 0:
            next_piece = 8
        return next_piece

    def find_children(self, next_piece):
#        next_piece = self.get_next_piece()
        boards = self.root.get_possible_moves(next_piece)
        for board in boards:
            temp = Tree(board)
            self.children.append(temp)
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

    def __repr__(self,level=0):
        ret = "\t" * level*2 + repr(self.root) + "\n"
        if self.children:
            for child in self.children:
                ret += child.__repr__(level+1)
        return ret

    
