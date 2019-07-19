"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

https://www.cnblogs.com/grandyang/p/4340948.html
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        minlen = len(s)
        res = ''
        count = 0
        m = dict()
        left = 0
        for i in t:
            m.setdefault(i, 0)
            m[i] += 1
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]] -= 1
                if m.get(s[i]) >= 0:
                    count += 1
            while count == len(t):
                if i - left + 1 <= minlen:
                    minlen = i - left + 1
                    res = s[left:left+minlen]
                if s[left] in m:
                    m[s[left]] += 1
                    if m[s[left]] > 0:
                        count -= 1
                left += 1
        return res

if __name__ == '__main__':
    s = "A"
    t = "A"
    so = Solution()
    r = so.minWindow(s, t)



