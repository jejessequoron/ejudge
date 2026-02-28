class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, nx, ny):
        self.x = nx
        self.y = ny
    def dist(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
        return ((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2) ** 0.5
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
o = Point(x1, y1)
o.show()
o.move(x2, y2)
o.show()
d = o.dist(x3, y3)
print(f"{d:.2f}")