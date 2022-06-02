



#explicit implementation of memoization

fibonacci_cache = {}
def fibonacci(n):
    #If we have cached value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    #compute nth term
    if n == 1:
        value = 1
    elif n == 2:
        value =  1
    elif n >2:
        value = fibonacci(n-1) + fibonacci(n-2)
    #cache the value and then return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 10):
     print(n, ":", fibonacci(n))

#memoization; store the values of recent function calls so future calls do not have to repeat the work
from functools import lru_cache
@lru_cache(maxsize = 10)
def fibonacci(n):
    #check that the input is a positive integer
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 1:
        raise ValueError('n must be a positive int')
#compute the Nth term
    if n == 1:
        return 1
    elif n== 2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,10):
    print(fibonacci(n))


for n in range(1, 10):
    print(fibonacci(n+1) / fibonacci(n))     #indicates how quickly the ratio grows

