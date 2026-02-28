n = int(input())
c = 0
s = list(map(int, input().split()))
for i in s:
    if (i > 0):
        c += 1
print(c)