from functools import lru_cache
import sys
import time


@lru_cache
def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


end = int(sys.argv[1])
start = 1
print(f"Calculating Fibonacci from {start} to {end}")

for _ in range(start, end - 1):
    now = time.perf_counter()
    n = fibonacci(_)
    delta = time.perf_counter() - now
    print(f"{_:3}:{n} ({delta:0.3}s)")
