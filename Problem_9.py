import math

def pythagoreanTriplet():
    a = 1
    b = 2
    c = 3
    result = 0

    while((a + b + c) <= 1000):

        if(((a*a) + (b*b)) == (c*c)):
          
            print(a,b,c)
      
        a = a + 1
        b = b + 1
        c = c + 1

    print(a*b*c)

pythagoreanTriplet()