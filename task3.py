class Tri:
    def init(self,a,b):
        self.a = a
        self.b = b
    def Stri(self):
        print(f'S = {self.a*self.b/2}')
    def Ptri(self):
        c = (self.a2 + self.b2)**0.5
        print(f'P = {self.a + self.b + c}')

Tri = Tri(3,5)
Tri.Ptri()
Tri.Stri()