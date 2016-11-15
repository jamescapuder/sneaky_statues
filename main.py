import board
import minimax

def main():
    root = board.Board()
    test = root.get_possible_moves("1")

    tree = minimax.Tree(root)


if __name__ == "__main__":
    main()


