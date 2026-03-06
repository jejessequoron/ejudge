n = int(input())
l = list(map(int, input().split()))
print(*sorted(set(l)))