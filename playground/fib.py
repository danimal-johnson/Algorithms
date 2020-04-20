import time
import functools


@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


for i in range(0, 10000, 10):
    start_time = time.time()
    fib(i)
    print(i, " ", time.time() - start_time)
