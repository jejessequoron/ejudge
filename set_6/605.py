s = input()
print("Yes" if any(c in "aeiou" for c in s.lower()) else "No")