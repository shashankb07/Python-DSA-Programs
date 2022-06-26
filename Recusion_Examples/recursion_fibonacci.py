def fibonnaci(n):
    assert n >= 0 and int (n) == n, 'enter positive integer number!' 
    if n  in [0,1]:
        return n 
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)      # fib(n) = fib(n-1) + fib(n-2) EX: fib(5) = fib(4) + fib(3) 
 
print(fibonnaci(7))
 