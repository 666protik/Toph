import math

f = math.factorial(int(input().strip()))

if f >= 1000:
    print(f"{f % 10000:04d}")
else:
    print(f)
