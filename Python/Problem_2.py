def fibonacci(times):
    prev1 = 1
    prev2 = 0
    cur = 1
    sum = 0
    while(cur <= times):
        next = prev1 + prev2
        prev2 = prev1
        prev1 = next
        print(next)
        if(next%2==0):
            sum = sum + next
        cur = cur + 1
        if(next>=4000000):
            break

    print(sum)

fibonacci(40000) #Rand number to reach four millions