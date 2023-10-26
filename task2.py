class Square:
    def init(self,x):
        self.x = x
    def S(self):
        print(f"S = {self.x*self.x}")
    def P(self):
        print(f"P = {self.x*4}")

Sq = Square(5)
Sq.S()
Sq.P()