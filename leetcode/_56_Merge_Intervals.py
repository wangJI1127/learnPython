"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals)
        res = []
        temp = intervals[0]
        i = 1
        while i < len(intervals):
            if self.ismerge1(temp, intervals[i]):
                t = [min(temp[0], intervals[i][0]), max(temp[1], intervals[i][1])]
                temp = t
                i += 1
                if i == len(intervals):
                    res.append(temp)
            else:
                res.append(temp)
                temp = intervals[i]
                i += 1
                if i == len(intervals):
                    res.append(temp)
        return res

    def ismerge1(self, nums1, nums2):
        if nums1[1] >= nums2[0]:
            return True
        else:
            return False

if __name__ == '__main__':
    nums = [[1,4],[4,5]]
    so = Solution()
    re = so.merge(nums)