n = int(input())
l = list(map(int, input().split()))
print("Yes" if all(x >= 0 for x in l) else "No")