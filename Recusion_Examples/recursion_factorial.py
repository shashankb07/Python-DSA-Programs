def factorial_rec(n):
    if n == 0 or n == 1:                    # statement no 1
        return 1                            # statement no 2
    elif n <0 :
        print('do not enter negative number!!')        
        return 0
    elif isinstance(n, float):
        print('do not enter floating point number!!')
        return 0
    else:
        return (n * factorial_rec(n - 1))   # statement no 3

print(factorial_rec(5))


