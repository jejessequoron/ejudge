def isUsual(num):
    while num != 1:
        if num % 2 == 0:
            num //= 2
        elif num % 3 == 0:
            num //= 3
        elif num % 5 == 0:
            num //= 5
        else:
            return False
    return True
n = int(input())
print("Yes" if isUsual(n) else "No")