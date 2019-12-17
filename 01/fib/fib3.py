import time

from typing import Dict
memo: Dict[int, int] = { 0: 0, 1: 1 }

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]

if __name__ == "__main__":
    start_time =  time.time()
    n = 40
    print("fib3(%d)=%d"%(n, fib3(n)))
    print("execution time: %s [s]"%(time.time()-start_time))

    