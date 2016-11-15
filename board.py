class Board:

    def __init__(self, moves=None):
        self.board = [[0], [0, 0], [0,0,0], [0,0,0,0], [0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0,0]]
        self.pieces = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.turn = 1
        if moves:
            try:
                self.moves = moves
                for key, val in moves.items():
                    if ((val[0],val[1]) != (-1,-1)):
                        self.board[val[0]][val[1]] = key
                    self.turn += 1
            except IndexError:
                print("Invalid board positions, edit input and try again")
        else:
            self.moves = {}
            for j in self.pieces:
                self.moves[j] = (-1, -1)

    def get_board(self):
        return self.board

    # Method to be used whenever we change anything's position, as we want to keep track of it in
    # the move dict and on the board itself. Just safer to have this i think.
    def set_position(self,piece, x, y):
        try:
            templocat = self.moves[piece]
            self.board[templocat[0]][templocat[1]] = 0
            self.moves[piece] = (x, y)
            self.board[x][y] = piece
            self.turn += 1
        except IndexError:
            print("Attempt to set position out of board bounds.")

    # Gets all possible board states that result from
    # next_piece being the next piece to be moved. Returns list of Boards.
    def get_possible_moves(self, next_piece):
        if next_piece in self.pieces:
            templocat = self.moves[next_piece]
            possible_boards = []
            for i in range(0, 7):
                for j in range(len(self.board[i])):
                    if (i, j) != templocat and self.board[i][j] == 0:
                        temp = Board(self.moves)
                        temp.set_position(next_piece, i, j)
                        print(temp)
                        possible_boards.append(((i, j), temp))
            return possible_boards
        else:
            print("Invalid piece number")

    def __str__(self):
        printstr = ""
        for i in range(0, len(self.board)):
            row = ''
            for j in self.board[i]:
                row += str(j)+" "
            printstr += '{:^16}'.format(row)
            printstr += '\n'
        return printstr
