""""
Sqrt(x) (Easy)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
"""
#avoiding use of sqrt 
#using binary search to find the square root of x
class Solution: #O(log n)
    def mySqrt(self, x: int) -> int:
        if x== 0 or x == 1:
            return x #return x if 0 or 1 since sqrt is itself
        start = 1
        end = x // 2 #end is x//2 since sqrt can't be greater than x//2 for x > 1; optimization instead of just end = x
        while start <= end:
            mid = (start + end) // 2 #find midpoint
            if mid * mid == x:
                return mid #if the midpoint squared is equal to x, return midpoint
            elif mid * mid < x: #start searching in upper half
                start = mid + 1 #move start to mid + 1
            else: #mid * mid > x , search in lower half
                end = mid - 1 #move end to mid - 1
        return end 