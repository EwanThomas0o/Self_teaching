import numpy as np

t = int(input())

for i in range(1,t+1):
    n,b = [int(s) for s in input().split()]
    a = np.sort([int(k) for k in input().split()])
    #print("For Case#{} we have {} House at prices {} with budget {}\n".format(i,n,a,b))


    #We've got all of our data!! now we need to remain inside this for loop so that we can do calculations per value of t
    #case = i = 1, n = 4, b = 100, a = [20,40,90,90]

    h = 0

    for l in range(0,n-1):
        if b >= a[l]: 
            h += 1
            b -= a[l]
        
    print("Case #{}: {}".format(i,h))


