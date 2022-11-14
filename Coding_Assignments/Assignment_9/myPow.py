# https://leetcode.com/problems/powx-n/

# Time Complexity
# O(log n)

# Space Complexity
# O(log n) -> call stack
def myPow(x, n):
    # Here returning inverse of power for negative power value
    if n < 0:
        return 1 / myPow(x, n * -1)

    # Terminating Condition for recursion
    # Returning 1 for power 0
    elif n == 0:
        return 1
    else:
        # To avoid unnecessary calls for same values, storing value in temp variable
        temp = myPow(x, n // 2)
        result = temp * temp
        if n % 2 == 0:
            return result
        else:
            return result * x


print(myPow(2, 10))
