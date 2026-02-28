n = int(input())
s = list(map(int, input().split()))
M = s[0]
for i in s:
    if (M < i):
        M = i
print(M)