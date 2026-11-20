import time

def ways_iterative(n):
    if n <= 1:
        return 1
    prev2 = 1
    prev1 = 1
    current = 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return current

n = 1000
start = time.perf_counter()
result = ways_iterative(n)
duration = time.perf_counter() - start

print(f"n = {n}")
print(f"Ways to climb (Iterative): {result}")
print(f"Time taken: {duration:.6f} seconds")
