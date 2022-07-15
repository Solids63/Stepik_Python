import random


class Cell:
    def __init__(self, mine, around_mines=0, fl_open=False):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = fl_open


class GamePole:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pole = self.init()

    def init(self):
        count = 0
        self.pole = [[Cell(0) for _ in range(self.n)] for _ in range(self.n)]
        while count <= (self.m + 1):
            x = random.choice(random.choice(self.pole))
            if x.mine == 1:
                continue
            else:
                x.mine = 1
                count += 1
            if count == self.m:
                break
        return self.pole

    #        self.pole = [[Cell(random.randint(0, 1)) for _ in range(self.n)] for _ in range(self.n)]
    def show(self):
        pass


#  c1 = Cell(3)

pole_game = GamePole(5, 12)
#  pole = ([[Cell(random.randint(0, 1)) for _ in range(10)] for _ in range(10)])
#  pole_game.init()

b = 0
for el in pole_game.pole:
    for i in el:
        if i.__dict__.get('mine') == 1:
            b += 1
        print(i.__dict__)
print(b)

