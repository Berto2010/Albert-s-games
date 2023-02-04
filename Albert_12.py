def factorial_r(n):
    print("Factorial of ", n)
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        print("I am a recursion, calling n - 1: ", n - 1)
        return n * factorial_r(n - 1)
        
def factorial(n):
    f = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            f = f * (i)
        return f
    
    
    

res = factorial(10000)
print (res)