"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # self.length = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, word, 0, i, j):  # 从word[0]开始
                    return True
        return False

    def backtrack(self, board, word, count, row, col):
        if count == len(word):
            return True
            # 下标越界，或者当前位置字符不匹配
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[count]:
            return False
            # 防止重复访问
        board[row][col] = '.'
        # 对四个方向递归搜索，注意是or
        res = self.backtrack(board, word, count + 1, row - 1, col) \
              or self.backtrack(board, word, count + 1, row + 1, col) \
              or self.backtrack(board, word, count + 1, row, col-1) \
              or self.backtrack(board, word, count + 1, row, col+1)
        # 还原现场
        board[row][col] = word[count]
        return res





if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCCED'
    so = Solution()
    res = so.exist1(board, word)
