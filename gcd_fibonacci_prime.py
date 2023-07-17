from random import random
import math

def gcd(a,b):
    """
    Function to find common divisor

    input a,b : two integers 
    return: greatest common divisor of the two integers a and b
    
    >>> gcd(7, 21)
    7
    """

    while b!= 0:
        result = b
        a, b = b, a % b
    return result

def fibonacci(n):
    """ 
    Function to find the number in the 'n'th sequence of the fibonacci

    param n: sequence number
    return: integer value of the 'n'th sequence of the fibonacci number
    >>> fibonacci(6)
    8
    """

    if n < 2: 
        return n
    else:
        a,b = 0 , 1
        for i in range(n):
            a,b = b, a+b
        return a

def fibonacci_2(n):
    if n <2:
        return 1
    else:
        return fibonacci_2(n-1) + fibonacci_2(n-2)
    

def is_prime_brute_force(number):
    """ Function that checks if the number is prime or not, using brute force"""
    num = abs(number)
    if num < 4:
        return True
    else:
        for x in range(2, num):
            if num % x == 0:
                return False
        return True
    
def is_prime_sqrt(number):
    """ Function that checks if the number is prime or not, (half the time complexity of brute force"""
    num = abs(number)
    if num < 4:
        return True
    else:
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                return False
        return True

def find_all_primes(number):
    """The following function finds all primes within the range from 1 to the number. is_prime_sqrt is used for this instance"""
    answer = [1,2,3]
    for i in range(4, number):
        if is_prime_sqrt(i)==True:
            answer.append(i)
    return answer

def find_all_primes_2(number):
    """The following function finds all primes within the range from 1 to the number. is_prime_brute_force is used for this instance"""

    answer = [1,2,3]
    for i in range(4, number):
        if is_prime_brute_force(i)==True:
            answer.append(i)
    return answer


# Best way to find all primes in a certain number set is to use the Seieve of Erathostenes
def sieve_of_eratosthenes(n):
    sieve = [1]*n
    sieve[0], sieve[1] = 0,0
    for i in range(2, int(n**0.5)+1):
        for j in range(i+i, n, i):
            sieve[j]=0
    return [i for i in range(n) if sieve[i]==1]


if __name__ == "__main__":
    import timeit
    # timing using find prime using sqrt (0.19s)
    # print(timeit.timeit('find_all_primes(100000)', setup='from __main__ import find_all_primes', number =1))    
    #timing using find prime using brute force (27.8s)
    # print(timeit.timeit('find_all_primes_2(100000)', setup='from __main__ import find_all_primes_2', number =1))    

    # print(sieve_of_eratosthenes(100))
    
    print(timeit.timeit('fibonacci(100)', setup='from __main__ import fibonacci', number = 10))
    print(timeit.timeit('fibonacci_2(100)', setup='from __main__ import fibonacci_2', number = 10))