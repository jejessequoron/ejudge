n = int(input())
l = list(map(int, input().split()))
q = int(input())
o = []
for _ in range(q):
    p = input().split()
    op = p[0]
    if op == "add":
        x = int(p[1])
        o.append(lambda a, x=x: a + x)
    elif op == "multiply":
        x = int(p[1])
        o.append(lambda a, x=x: a * x)
    elif op == "power":
        x = int(p[1])
        o.append(lambda a, x=x: a ** x)
    elif op == "abs":
        o.append(lambda a: abs(a))
for i in range(n):
    for f in o:
        l[i] = f(l[i])
print(*l)