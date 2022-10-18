# Count number of ways to reach nth staircase.
# He can take only 1 or 2 steps at once.

# Here, for each staircase n
# staircase     1   2   3   4   5
#  ways         1   2   3   5   8

# So it's forming fibonacci series
# index     0   1   2   3   4   5   6
#  term     0   1   1   2   3   5   8

# Here we can see that ways(n) = fib(n+1)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def numberOfWaysToClimb(n):
    return fib(n + 1)


print(numberOfWaysToClimb(4))
