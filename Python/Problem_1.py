def sumNumbers(num):
    result = 0
    for x in range(num):
        if((x % 3 == 0) or (x % 5 == 0)):
            print(x)
            result = result + x

    print(result)

sumNumbers(1000)