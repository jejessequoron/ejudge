def g(n):
    for x in range(0, n + 1, 2):
        yield x
n = int(input())
gen = g(1000000)
for _ in range(n // 2):
    print(next(gen), end=",")
print(next(gen))