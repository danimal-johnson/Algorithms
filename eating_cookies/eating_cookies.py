#!/usr/bin/python

import sys
import functools

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
@functools.lru_cache(maxsize=128)
def eating_cookies(n, cache=None):

"""Returns an int of arbitrary length.

For n cookies, how many ways can you eat them if you can only eat 1, 2, or 3 at a time?
Uses recursion, so max depth = 1000.
This function makes use of the least-recently-used cache built into functools.
"""
   # "Tribonacci" sequence:
   if n < 2:
        return 1
    if n == 2:
        return 2
    return (eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))


def eating_brady_cookies(n, cache=None):

"""Returns an int of arbitrary length.

This is Brady's version of the function given in class.
It makes use of an explicit cache, stored as an array inside the function.
"""
   if cache is None:
        cache = [0] * (n+1)  # Create an empty array on the first call.
    if n <= 1:
        cache[n] = 1        # Only one way to eat zero or one cookie
    elif n == 2:
        cache[n] = 2        # Two ways to eat two cookies

    # If the current result for n isn't in the cache, calculate it.
    elif cache[n] == 0:
        cache[n] = eating_brady_cookies(n-1, cache)
        + eating_brady_cookies(n-2, cache)
        + eating_brady_cookies(n-3, cache)

    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
