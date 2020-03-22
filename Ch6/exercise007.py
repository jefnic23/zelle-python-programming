n = eval(input('Enter a number: '))

def fib(n):
    fib = [1,1]
    for i in range(n-2):
        x = fib[i]
        y = fib[i+1]
        fib.append(x+y)
    return fib

print(fib(n))
