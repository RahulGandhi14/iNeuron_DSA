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


"""
Let n be the absolute value of dividend.
Time Complexity: 0(log^2 n)
We started by performing an exponential search to find the biggest number that fits into
the current dividend. So, for this time complexity is o(log n) operations
After doing this search, we updated the dividend by subtracting the number we found.
In the worst case, we were left with a dividend slightly less than half of the previous
dividend (if it was more than half, then we couldn't have found the maximum number that fit in by doubling! ).
So how many of these searches did we need to do?
Well, with the dividend at least halving after each one, there couldn't have been more
than o(1log n) of them.
So combined together, in the worst case, we have 0(1og n) searches with each search
takingo (log n) time.
This gives us O( (log n) (log n)) O(log2 n)
Space Complexity : O(1)

e.g
Here do the left shift starting from
2^0, 2^1, 2^2, ..., 2^k where 2^k <= n (dividend)

2^k = n ==> k = log(n) (outer while loop)
then we'll update the dividend, and loop will run again for the updated dividend
in the worst case, that can also take around O(log(n)) time

Overall time complexity = O(log(n) * log(n)) => O(log^2(n)) 
in words big o of log square n.
"""

print(divide(10, 3))
