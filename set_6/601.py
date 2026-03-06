n = int(input())
l = list(map(int, input().split()))
print(sum(map(lambda x: x * x, l)))