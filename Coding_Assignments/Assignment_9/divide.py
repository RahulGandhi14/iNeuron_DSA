# https://leetcode.com/problems/divide-two-integers/

"""
Bit manipulation:
8 (decimal) -> 1000 (binary)

Left Shift:
1000 << 1 -> 10000 (binary) -> 16 (decimal)
i.e left shift = multiplication * 2

Right Shift:
1000 >> 1 -> 0100 (binary) -> 4 (decimal)
i.e right shift = division / 2
"""

"""
Intution:

Suppose dividend = 15 and divisor = 3, 15 - 3 > 0. 
We now try to subtract more by shifting 3 to the left by 1 bit (6). 
Since 15 - 6 > 0, shift 6 again to 12. Now 15 - 12 > 0, shift 12 again to 24, 
which is larger than 15. So we can at most subtract 12 from 15. 
Since 12 is obtained by shifting 3 to left twice, it is 1 << 2 = 4 times of 3. 
We add 4 to an answer variable (initialized to be 0). 
The above process is like 15 = 3 * 4 + 3. 
We now get part of the quotient (4), with a remaining dividend 3.

Then we repeat the above process by subtracting divisor = 3 from 
the remaining dividend = 3 and obtain 0. We are done. 
In this case, no shift happens. We simply add 1 << 0 = 1 to the answer variable.
"""


def divide(dividend, divisor):
    absDividend = abs(dividend)
    absDivisor = abs(divisor)

    result = 0

    while absDividend >= absDivisor:
        shifts = 0
        while absDividend >= absDivisor << shifts:
            shifts += 1

        result += 1 << (shifts - 1)
        absDividend -= absDivisor << (shifts - 1)

    if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
        result = -result

    """
    Note: Assume we are dealing with an environment that could only store 
    integers within the 32-bit signed integer range: [−231, 231 − 1]. 
    For this problem, if the quotient is strictly greater than 231 - 1, 
    then return 231 - 1, and if the quotient is strictly less than -231, 
    then return -231.
    """
    return min(2147483647, max(-2147483648, result))


print(divide(10, 3))
