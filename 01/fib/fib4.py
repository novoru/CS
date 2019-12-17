import time

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n-1) + fib4(n-2)

if __name__ == "__main__":
    start_time =  time.time()
    n = 40
    print("fib4(%d)=%d"%(n, fib4(n)))
    print("execution time: %s [s]"%(time.time()-start_time))

    