def g(l, k):
    for _ in range(k):
        for e in l:
            yield e
l = list(map(str, input().split()))
k = int(input())
for v in g(l, k):
    print(v, end=" ")