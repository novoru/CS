import time

def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

if __name__ == "__main__":
    start_time =  time.time()
    n = 40
    print("fib2(%d)=%d"%(n, fib2(n)))
    print("execution time: %s [s]"%(time.time()-start_time))