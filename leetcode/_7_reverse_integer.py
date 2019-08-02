"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,
  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            re = int(str(x)[::-1])
        else:
            re = int(str(x)[:0:-1]) * -1
        if re <= 2**31-1 and re >= -2**31:
            return re
        else:
            return 0

