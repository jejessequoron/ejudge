def g(n):
    for i in range(n + 1):
        yield pow(2, i)
n = int(input())
for v in g(n):
    print(v, end=" ")