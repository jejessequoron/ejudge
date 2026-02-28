class Employee():
    def __init__(self, n, bs):
        self.n = n
        self.bs = bs
    def total_salary(self):
        return self.bs
class Manager(Employee):
    def __init__(self, n, bs, bon):
        super().__init__(n, bs)
        self.bon = bon
    def total_salary(self):
        return self.bs * (1 + self.bon / 100)
class Developer(Employee):
    def __init__(self, n, bs, cp):
        super().__init__(n, bs)
        self.cp = cp
    def total_salary(self):
        return self.bs + self.cp * 500
class Intern(Employee):
    pass
p = input().split()
e = p[0]
_, n, bs = p[0], p[1], p[2]
if e == "Manager":
    bon = p[3]
    o = Manager(n, int(bs), int(bon))
elif e == "Developer":
    cp = p[3]
    o = Developer(n, int(bs), int(cp))
else:
    o = Intern(n, int(bs))
print(f"Name: {o.n}, Total: {o.total_salary():.2f}")