"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
遍历由列表的两端向中间进行，每次较短的那条垂直线向中间移动一个单位，由对应的另一条垂直线代替；每次计算对应容器的容积，
保留这些容积中的最大值；当两条垂直线靠在一起时，遍历结束，此时已经得到了可能的最大容积。这种算法只需进行一层循环，时间复杂度为O(n)，因而更好。
"""
class Solution(object):

    def maxArea1(self, height):
        """ 暴力破解：超时
        :type height: List[int]
        :rtype: int
        """
        m = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                if min(height[i], height[j]) * (j-i) > m:
                    m = min(height[i], height[j]) * (j-i)
        return m


    def maxArea(self, height):
        result = 0
        i = 0
        j = len(height) - 1
        while i < j:
            result = max(result, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result
