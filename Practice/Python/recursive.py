def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)
        
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def factorial2(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
        
print(factorial(4))