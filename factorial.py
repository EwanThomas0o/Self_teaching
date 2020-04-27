def factorial(n):

    if n == 1 or n ==0:
        return 1
    elif n < 0:
        print('you cannot have a factorial of a negative number!')
    else:
        return n*factorial(n-1)

print(factorial(3))