
# Double the value of x 
def doubledInt(x:int) -> int:
    return x*2

# Return the larger value between x and y
def largest(x:float,y:float) -> float:
    if x > y:
        return x
    else:
        return y
    
# Determine if the two x coordinates are the same, which would imply that they are on top of each other
def isVertical(a:tuple[float,float], b:tuple[float,float]) -> bool:
    return a[0] == b[0] and a[1] != b[1]

# Determine the first n primes
def primes(n:int) ->list[int]:

    # Create a helper function that checks if a number is prime
    def is_prime(x:int) ->bool:
        if x <= 1: 
            return False
        for i in range (2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    prime_list = []
    i = 2
    while len(prime_list) < n:
        if (is_prime(i)):
            prime_list.append(i)
        i+= 1
    # In range of 2 to n, append i to the list if i is a prime
    return prime_list

    # You can skip checking if i is a prime by instead using 
    # the formulas based on wilsons theorem
    """
     def prac_primes(n):
        primes_list = []
        for i in range(2, n):
            if floor(factorial(i - 1) % i) == i - 1:
                primes_list.append(i)
        return primes_list
    """

def fibonacciSequence(n:int) -> list[int]:
    #accepts an integer n and returns a list containing the first n elements of fibonacci sequence (starting with 0 and 1)

    # Base cases
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_list = [0, 1]

    # Append n - 2 times to as 0 1 are the starting numbers
    for i in range(2,n):
        # Append the sum of the last two terms in the sequence or list
        # Negative indexes indicate reading right to left, so -2 index would be 2nd to the last index
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list

def bubbleSort(arr: list[int]) -> list[int]:
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def sortedIntegers(l: list[int]) -> list[int]:
    # Accepts a list of integers and returns a list with the same integers sorted from smallest to highest
    return bubbleSort(l)

def sublists(l:list[int]) -> list[list[int]]:
    # accepts a list of integers and returns all the sublists of the list. Sublists are contiguous chunks of a list 
    # (including an empty list and the list itself). [1,2], [2], [], [2,3,4], and [1,2,3,4,5] are sublists of [1,2,3,4,5] 
    # but [3,5] and [1,2,3,4,6] are not

    # Start by first appending the list itself
    # "Remove" the last element, append the new list, keep doing that until you are left with the front most element
    # "Remove" the front most element then start from the last element

    if not l:
        return []
    
    sub_lists = []
    # Go through the list
    for i in range(len(l)):
        # If the difference of the index and length is 1, skip the operation as it repeats append([l[i]])
        if i + 1 != len(l):
            sub = l[i:len(l)]
            sub_lists.append(sub)
        if (len(l) - i - 1) != 0:
            sub = l[0:len(l) - i]
            sub_lists.append(sub)
        # Append each element on the list
        sub_lists.append([l[i]])
    sub_lists.append([])
    return sub_lists

print(sublists([1,2,3]))