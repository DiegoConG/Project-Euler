import math
import sys
def checkPrime(nNum):
    testNum = 1
    primes = 0

    while(primes < nNum):
        if (isPrime(testNum)):
            primes = primes + 1
            print(testNum,primes)

        testNum = testNum + 2    
    
    print(primes,testNum-2)

def isPrime(num):

    prime = False

    fact = factorial(num-1) + 1
    if(fact % num == 0):
        prime = True
    
    return prime


def factorial(num):

    if num < 2:
        return 1
    else:
        return num * factorial(num-1)

print(sys.getrecursionlimit())

sys.setrecursionlimit(900000000)
print(sys.getrecursionlimit())

checkPrime(100001)