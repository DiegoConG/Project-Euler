def findMirror():
    num = 999

    while(num > 100):
        print(num)
        print("reverse")
        if(checkMirror(num*num)):
            
            print(str(num) + "Is Mirror:" )
            break
        else:
            num = num - 1

    
    

def checkMirror(num):
    reverse = 0
    isMirror = False

    while(num > 0):
        lastDigit = num % 10
        reverse = (reverse * 10 ) + lastDigit
        print(reverse)
        num = num // 10

    if(num == reverse):
        print("@@@@")
        isMirror = True
    
    return isMirror


findMirror()