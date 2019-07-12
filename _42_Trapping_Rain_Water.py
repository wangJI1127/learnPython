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
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        l = 0
        r = len(height) - 1
        while l < r and height[l] < height[l+1]:
            l += 1
        while r > l and height[r] < height[r-1]:
            r -= 1

        m = 0
        li = []
        while l < r:
            li.append(height[l])
            if li[0] > height[l+1]:
                l += 1
            else:
                he = min(li[0], height[l+1])
                wi = len(li) - 1
                z = 0
                for i in range(1, len(li)-1):
                    z = z + li[i]
                m = m + he * wi - z
                l += 1
                li = []
        return m

if __name__ == '__main__':
    nums = [2,0,2]

    so = Solution()
    r = so.trap(nums)

