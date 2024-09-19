def doubledInt(x:int) -> int:
    return x*2

def largest(x:float,y:float) -> float:
    if x > y:
        return x
    else:
        return y
    
def isVertical(a:tuple[float,float], b:tuple[float,float]) -> bool:
    return a[0] == b[0]

def primes(n:int) ->list[int]:
    def is_prime (n:int) -> bool:
        if n < 2:
            return False
        for i in range(2,int(n**0.5)):
            if n%i == 0:
                return False
        return True
    return [n for n in range(2,n) if is_prime(n)]

def fibonacciSequence(n:int) -> list[int]:
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def sortedIntegers(l:[int]) -> [int]:
    
def sublists(l:list[int]) -> list[list[int]]: