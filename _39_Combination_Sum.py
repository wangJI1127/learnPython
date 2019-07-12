"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
 combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

非常典型的DFS并且返回路径的题目，我们采用DFS的方法  https://www.jianshu.com/p/79b05c2bfdbc
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        re = list()
        temp = list()
        candidates.sort()
        self.combine(candidates, target, 0, temp, re)
        return re


    def combine(self, arrays, target, index, temp, re):
        # 如果目标和的差值小于0，表示该路径出现错误
        if target < 0:
            return
        # 等于表示，这是一条正确的路径，将其add到result上
        elif target == 0:
            # 这里每次重新创建temp列表，避免与之前的列表重复
            re.append(list(temp))
            # 否则的话，目标和的差值大于0，继续进行深度优先搜索
        else:
             # 选取之后的每个数字都是一种可能性，其中index的作用是避免搜索之前搜索过的数组元素
            for i in range(index, len(arrays)):
                temp.append(arrays[i])
                # 先加入元素，然后进行搜索，这里进行DFS搜索，如果不满足，就把temp列表里的元素去除掉
                self.combine(arrays, target-arrays[i], i, temp, re)
                # 目标和不符合，所以将临时列表的最新值去除，然后尝试下一个元素
                temp.pop()

if __name__ == '__main__':
    nums = [2,3,6,7]
    so = Solution()
    so.combinationSum(nums, 7)



