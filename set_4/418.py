a, b = map(float, input().split())
c, d = map(float, input().split())
x = (a * d + b * c) / (b + d)
print(f"{x:.10f} {0.0:.10f}")