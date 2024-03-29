from math import sqrt

def getPrimes(limit):

    '''primes = []
    first = 2

    primes = getNumbers(n)

    while((first*first) < n):
        print(primes)
        for x in primes:
            if(first % x == 1):
                primes.remove(x)
    
    first = first + 1

        
        

    print(primes)'''

    
    


def getNumbers(num):
    temp = []
    for x in range(2,num):
        temp.append(x)

    return temp

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

print(sum(primes(2000000)))