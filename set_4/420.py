m = int(input())
g = 0
def outer():
    n = 0
    def inner():
        nonlocal n
        global g
        x = 0
        for _ in range(m):
            s, v = input().split()
            v = int(v)
            if s == "global":
                g += v
            elif s == "nonlocal":
                n += v
            else:
                x += v
    inner()
    return n
t = outer()
print(g, t)