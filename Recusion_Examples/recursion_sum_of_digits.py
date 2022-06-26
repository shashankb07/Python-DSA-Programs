def sum_of_digits(n):
    assert n >= 0 and int (n) == n, 'enter positive integer number!' 
    if n == 0:
      return 0
    else:
        return  int(n % 10) + sum_of_digits(int(n / 10))
print(sum_of_digits(512))




# (quotent) = int(a/10) 
# mod = a % 10
# result = quotent + mod
# print(quotent)
# print(mod)
# print(result)