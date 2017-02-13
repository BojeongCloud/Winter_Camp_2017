def factorial(k):
    if(k == 1):
        return 1
    else:
        return k * factorial(k - 1)
# print(factorial(7))

def fibonacci(n):
    if(n == 1):
        return 1
    elif(n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))
