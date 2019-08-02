"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"


"""


class Solution(object):
    def longestValidParentheses(self, s):
        """ 利用栈实现
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        l = list()
        l.append(-1)
        m = 0
        for i in range(len(s)):
            if s[i] == '(':
                l.append(i)
            else:
                l.pop()
                if len(l) == 0:
                    l.append(i)
                else:
                    m = max(m, i-l[len(l)-1])
        return m

    def longestValidParentheses1(self, s):
        """
        动态规划
        :param s:
        :return:
        """
        if len(s) < 2:
            return 0
        m = 0
        l = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i > 2:
                        l[i] = l[i-2] + 2
                    else:
                        l[i] = 2
                elif i - l[i-1] > 0 and s[i - l[i-1] - 1] == '(':
                    if i - l[i - 1] >= 2:
                        l[i] = l[i-1] + 2 + l[i - l[i-1] - 2]
                    else:
                        l[i] = l[i-1] + 2
                m = max(m, l[i])
        return m

