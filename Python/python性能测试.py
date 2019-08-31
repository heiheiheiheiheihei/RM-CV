import time



def fib(n):
    if n < 2:
        return 1
    elif n >= 2:
        return fib(n - 2) + fib(n - 1)

timetemp = time.time()
print(fib(40))
print(time.time() - timetemp)