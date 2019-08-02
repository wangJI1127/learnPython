"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


"""


class Solution(object):
    def minPathSum(self, grid):
        """ 不能使用贪心算法，必须使用动态规划
        :type grid: List[List[int]]
        :rtype: int
        """

        hang = len(grid)
        lie = len(grid[0])
        if hang == 0 or lie == 0:
            return 0
        temp = [[0 for i in range(lie)] for j in range(hang)]
        temp[0][0] = grid[0][0]
        for i in range(1, lie):
            temp[0][i] = grid[0][i] + temp[0][i-1]
        for j in range(1, hang):
            temp[j][0] = grid[j][0] + temp[j-1][0]
        for i in range(1, hang):
            for j in range(1, lie):
                temp[i][j] = grid[i][j] + min(temp[i-1][j], temp[i][j-1])

        return temp[hang-1][lie-1]





