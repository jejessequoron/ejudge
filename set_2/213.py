
n = int(input())
f = True
if (n == 1):
    print('No')
else:
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            f = False
    if (f):
        print('Yes')
    else:
        print('No')