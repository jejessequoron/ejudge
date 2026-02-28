class Account:
    def __init__(self, o, b):
        self.o = o
        self.b = b
    def deposit(self, a):
        self.b += a
    def withdraw(self, a):
        if a > self.b:
            return False
        self.b -= a
        return True
b, a = map(int, input().split())
o = Account("jdan", b)
if o.withdraw(a):
    print(o.b)
else:
    print("Insufficient Funds")