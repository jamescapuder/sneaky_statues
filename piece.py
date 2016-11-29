
def get_players(num):
    if num % 2 == 1:
        return "one", "two"
    else:
        return "two", "one"

class Piece:
    def __init__(self, num, xycord=None):
        self.num = num
        self.player, self.opp = get_players(self.num)
        if xycord:
            self.xy = xycord
            self.x = xycord[0]
            self.y = xycord[1]

    def set(self, xycord):
        self.xy = xycord
        self.x = xycord[0]
        self.y = xycord[1]

    def __str__(self):
        return "[" + str(self.num) + ", " + str(self.xy) + "]"
