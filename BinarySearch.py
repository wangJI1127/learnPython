"""
二分查找
"""


def binarySearch(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


l = [1, 2, 4, 5, 6]
t = 4
