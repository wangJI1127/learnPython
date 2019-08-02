"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        temp = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                temp = i
                break
        if temp == -1:
            return nums[::-1]
        for i in range(len(nums)-1, temp, -1):
            if nums[i] > nums[temp]:
                nums[i], nums[temp] = nums[temp], nums[i]
                break
        nums[temp+1:len(nums)] = nums[temp+1:len(nums)][::-1]
        return nums

    def nextPermutation1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return nums
        partition = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                partition = i
                break
        if partition == -1:
            nums.reverse()
            return nums
        else:
            for i in range(len(nums) - 1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
        nums[partition + 1:len(nums)] = nums[partition + 1:len(nums)][::-1]
        return nums
