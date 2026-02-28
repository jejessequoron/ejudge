class Pair():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, c, d):
        return [self.a + c, self.b + d]
a, b, c, d = map(int, input().split())
p = Pair(a, b)
print(f"Result: {p.add(c, d)[0]} {p.add(c, d)[1]}")