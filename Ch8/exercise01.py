# The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, .... Each number in the
# sequence (after the first two) is the sum of the previous two. Write a
# program that computes and outputs the nth Fibonacci number, where n is a
# value entered by the user.


nth = eval(input('Enter a number n, where n is the nth Fibonacci number: '))
fib = [1, 1]
for i in range(nth-2):
    fib.append(fib[-1] + fib[-2])
print(fib[-1])
