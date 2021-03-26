# ONLY PRINT
#    res = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#    for n in res:
#       print(n, end=" ")

# CLASS CORRECTION
#    series = [0, 1]
#    a, b = 0, 1
#    for n in range(1, 10):
#        c = b + a
#        series.append(c)
#        a, b = b, c
#    print(series)

# MY CODE
fib = [0, 1]
for c in range(1, 10):
    fn = fib[c] + fib[c-1]
    fib.append(fn)
print(fib)
