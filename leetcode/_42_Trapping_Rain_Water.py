"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
 is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


"""
class Solution(object):

    def trap(self, height):
        """
        解题思路：基于动态规划Dynamic Programming的，我们维护一个一维的dp数组，这个DP算法需要遍历两遍数组，第一遍遍历dp[i]中存入i位置
        左边的最大值，然后开始第二遍遍历数组，第二次遍历时找右边最大值，然后和左边最大值比较取其中的较小值，然后跟当前值A[i]相比，如果大于
        当前值，则将差值存入结果
        :type height: List[int]
        :rtype: int
        """
        m = 0
        r = len(height) - 1
        res = 0
        arr = [0 for i in range(r)]
        for i in range(r):
            arr[i] = m
            m = max(m, height[i])
        m = 0
        for i in range(r, -1, -1):
            arr[i] = min(m, arr[i])
            m = max(m, height[i])
            if arr[i] - height[i] > 0:
                res = res + arr[i] - height[i]
        return res

    def trap1(self, height):
        """
        解题思路：需要left和right两个指针分别指向数组的首尾位置，从两边向中间扫描，在当前两指针确定的范围内，先比较两头找出较小值，如果
        较小值是left指向的值，则从左向右扫描，如果较小值是right指向的值，则从右向左扫描，若遇到的值比当较小值小，则将差值存入结果，如遇
        到的值大，则重新确定新的窗口范围，以此类推直至left和right指针重合
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            mn = min(height[l], height[r])
            if mn == height[l]:
                l += 1
                while l < r and height[l] < mn:
                    res = res + mn - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and height[r] < mn:
                    res = res + mn -height[r]
                    r -= 1
        return res

if __name__ == '__main__':
    nums = [2,0,2]

    so = Solution()
    r = so.trap(nums)

