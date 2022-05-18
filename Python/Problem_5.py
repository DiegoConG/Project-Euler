def isDivisible(num):
    divisible = True
    for x in range(11,20):
        if(num % x != 0):
            divisible = False
            break
        
    return divisible

def checkDivisibility():
    divisible = False
    testNumber = 1
    while(divisible != True):
       

        if(isDivisible(testNumber)):
            divisible = True
        else:
            testNumber = testNumber + 1
    
    print(testNumber)


checkDivisibility() #Can be optmized with prime numbers factorization, idk how to do it