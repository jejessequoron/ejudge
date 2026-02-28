def g(n):
    for i in range(n):
        yield (i + 1) * (i + 1)
n = int(input())
for v in g(n):
    print(v)