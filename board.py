import copy

class Board:
    def __init__(self, moves=None):
        self.board = []
        self.pieces = [1,2,3,4,5,6,7,8]
        for i in range(1,7):
            self.board.append([0]*i)
        if moves!=None:
            try:
                self.moves = moves
                for k,v in moves:
                    self.board[v[0]][v[1]] = k
            except IndexError:
                print("Invalid board positions, edit input and try again")
        else:
            self.moves = {}
            for j in self.pieces:
                self.moves[j] = (-1,-1)


    def get_board(self):
        return self.board

    def set_position(self,piece, x, y):
        try:
            templocat = self.moves[piece]
            self.board[templocat[0]][templocat[1]] = 0
            self.moves[piece] = (x,y)
            self.board[x][y] = piece
        except IndexError:
            print("Attempt to set position out of board bounds.")

    def get_possible_moves(self, next_piece):
        if next_piece in self.pieces:
            templocat = self.moves[next_piece]
            possible_boards = []
            # zero_coords = self.get_empty()
            # tempB = Board(self.moves)
            # tempB.board[templocat[0]][templocat[1]] = 0
            for i in range(0,6):
                for j in range(len(self.board[i])-1):
                    if (i, j)!=templocat and self.board[i][j]==0:
                        temp = Board(self.moves)
                        temp.set_position(next_piece, i, j)
                        possible_boards.append(temp)
            return possible_boards
        else:
            print("Invalid piece number")


if __name__=='__main__':
    b1 = Board()
