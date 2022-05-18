def sumSquaresDif(num):
    total1 = sumSquares(num)
    total2 = squareSum(num)
    
    print(total2 - total1)

def sumSquares(numMax):
    total = 0

    for x in range(1,numMax+1):
        
        total = total + (x * x)

    return total

def squareSum(numMax):
    total = 0
    for x in range(1,numMax+1):
        total = total + x

    total = total * total    
    return total

sumSquaresDif(100)