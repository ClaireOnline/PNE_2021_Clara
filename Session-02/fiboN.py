def fibon(n):
    fib = [0, 1]
    for c in range(1, n):
        fn = fib[c] + fib[c-1]
        fib.append(fn)
    return fib[n]


# MAIN PROGRAM
print("5th Fibonacci term: ", fibon(5), "\n10th Fibonacci term: ", fibon(10), "\n15th Fibonacci term: ", fibon(15))
