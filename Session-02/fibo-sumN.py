def fibosum(n):
    fib = [0, 1]
    for c in range(1, n):
        fn = fib[c] + fib[c-1]
        fib.append(fn)
    return sum(fib)


print("Sum of the First 5 terms of the Fibonacci series: ", fibosum(5), "\nSum of the First 10 terms of the Fibonacci series: ", fibosum(10))