n = int(input())
flag = True
while n > 0:
    if (n % 10) % 2 != 0:
        flag = False
        break
    n //= 10
print("Valid" if flag else "Not valid")