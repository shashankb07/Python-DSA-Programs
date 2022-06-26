def powerof2(n):
    if n == 0:
        return 1
    else :
        power = powerof2(n-1)
        return power * 2


print(powerof2(4))


# def powerof2(n):
#     power = 1
#     i = 0
#     while(i < n):
#         power  = power * 2
#         i = i + 1
#     return power

# ret_val = powerof2(5)
# print(ret_val)