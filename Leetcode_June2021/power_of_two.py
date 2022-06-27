# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false

# def power_of_two(n):
#     if n == 0:
#         return False
#     while ( n % 2 == 0):
#         n = n / 2
#     if n == 1:
#         return True
#     else:
#         return False
# TEST CASE
# print(power_of_two(2))
# print(power_of_two(1))
# print(power_of_two(16))
# print(power_of_two(3))
# print(power_of_two(12))

# Conclusion: All the test case works :)

def power_of_two(n):
    if n == 0:
        return False
    if n & (-n) == n:
        return True
    else:
        return False

# TEST CASE
print(power_of_two(0)) # False
print(power_of_two(2)) # True
print(power_of_two(1)) # True
print(power_of_two(16))# True 
print(power_of_two(3)) # False
print(power_of_two(12)) # False