
def get_players(num):
    if num % 2 == 1:
        return "one", "two"
    else:
        return "two", "one"

class Piece:
    def __init__(self, num, xycord):
        self.num = num
        self.xy = xycord
        self.x = xycord[0]
        self.y = xycord[1]
        self.player, self.opp = get_players(self.num)

    def __str__(self):
        return "[" + str(self.num) + ", " + str(self.xy) + "]"
