def power_of_number(x,n):
    if n == 0:
        return 1
    else:
        return x * power_of_number(x, n - 1) # 4  * (4 raise to 4 -1 = 3) -> 4 * 4^3 ...

print(power_of_number(4,3))


# easy but lets do something else to reduce the time complexity to O(Log n)

# def power_logn(x,n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         y = power_logn(x, n / 2)
#         return y * y
#     else:
#         return x * power_logn(x , n - 1)


# print(power_logn(2,5))

