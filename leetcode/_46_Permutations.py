"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = list()
        res = list()
        self.find(nums, temp, res)
        return res



    def find(self, nums, temp, res):
        if len(temp) == len(nums):
            res.append(list(temp))  # 如果不新建对象，最后都会变为空列表
        else:
            for i in nums:
                if i not in temp:
                    temp.append(i)
                else:
                    continue
                self.find(nums, temp, res)
                temp.pop()
        return res