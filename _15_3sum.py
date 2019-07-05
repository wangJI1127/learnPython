"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

https://blog.csdn.net/turing365/article/details/80565988
"""


class Solution(object):
    def threeSum(self, nums):
        """ 时间复杂度较高， 会超时
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = list()
        nums = sorted(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    if [nums[i], nums[j], -(nums[i] + nums[j])] not in l:
                        l.append([nums[i], nums[j], -(nums[i] + nums[j])])
        return l

    def threeSum1(self, nums):
        """ 超时"""
        nums = sorted(nums)
        l = list()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    if [nums[i], nums[left], nums[right]] not in l:
                        l.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                elif nums[right] + nums[left] < -nums[i]:
                    while left < right:
                        left += 1
                        if nums[left-1] < nums[left]:
                            break
                else:
                    while left < right:
                        right -= 1
                        if nums[right+1] > nums[right]:
                            break
        return l

    def threeSum2(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
    


if __name__ == '__main__':
    ar = [3,0,-2,-1,1,2]
    so = Solution()
    r = so.threeSum1(ar)


