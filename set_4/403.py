def g(n):
    for i in range(0, n + 1, 12):
        yield i
n = int(input())
for v in g(n):
    print(v, end=" ")