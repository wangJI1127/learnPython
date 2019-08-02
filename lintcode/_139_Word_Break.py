"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """  暴力破解
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.word_break(s, set(wordDict), 0)

    def word_break(self, s, wordDict, start):
        if start == len(s):
            return True
        for end in range(start+1, len(s)+1):
            if s[start:end] in wordDict and self.word_break(s, wordDict, end):
                return True
        return False

    def wordBreak1(self, s, wordDict):
        """  动态规划
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]




if __name__ == '__main__':
    s = "applepenapple"
    word = ["apple", "pen"]
    so = Solution()
    re = so.wordBreak1(s, word)
