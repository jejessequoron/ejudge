n = int(input())
s = list(map(int, input().split()))
l = list()
for i in s:
    if i not in l:
        print('YES')
        l.append(i)
    else:
        print('NO')