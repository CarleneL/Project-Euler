'''
Find all the primes under 2mil and sum thim
'''
def isPrime(n):
    factors = []
    if n == 0 or n==1:
        return False
    elif n==2:
        return True
    elif n %2 ==0:
        return False
    for x in range(3, int(n**.5) + 1, 2):
        if n % x == 0:
            return False
    return True



solution = sum(filter(lambda x: isPrime(x), range(0,2000001)))
