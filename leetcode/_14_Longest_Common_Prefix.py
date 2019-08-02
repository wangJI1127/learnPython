"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        re = strs[0]
        for i in range(1, len(strs)):
            re = self.longestCommonPrefix_1(re, strs[i])
            if re == '':
                return re
        return re

    def longestCommonPrefix_1(self, str1, str2):
        re = ''
        for i in range(min(len(str1), len(str2))):
            if str2[i] == str1[i]:
                re = str2[0:i+1]
            else:
                break
        return re



