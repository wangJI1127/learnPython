"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

https://blog.csdn.net/waterkong/article/details/77851539

"""


class Solution(object):
    def maxSubArray(self, nums):
        """ 动态规划
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        sum = nums[0]
        x = 0
        for i in range(1, len(nums)):
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
                x = i
            if sum > result:
                result = sum
                y = i
        # print("最大子数组的起始-结束下标", x, y)
        return result
