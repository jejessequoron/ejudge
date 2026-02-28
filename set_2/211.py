n, l, r = map(int, input().split())
s = list(map(int, input().split()))
s[l - 1:r] = s[l - 1:r][::-1]
print(*s)