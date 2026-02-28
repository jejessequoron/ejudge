class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r * self.r
r = int(input())
o = Circle(r)
a = o.area()
print(f"{a:.2f}")