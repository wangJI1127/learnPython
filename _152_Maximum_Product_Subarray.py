"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

求最大子数组乘积  https://www.cnblogs.com/grandyang/p/4028713.html
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return None
        if len(nums) == 1:
            return nums[0]
        ma = nums[0]
        mi = nums[0]
        re = nums[0]
        for i in range(1, len(nums)):
            mx = ma
            mn = mi
            ma = max(max(nums[i], mx * nums[i]), mn * nums[i])
            mi = min(min(nums[i], mx * nums[i]), mn * nums[i])
            re = max(re, ma)
        return re
