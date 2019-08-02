"""
KMP算法学习
"""


class KMP(object):

    def kmp1(self, s, p):
        """
         暴力破解法
         :param s: 字符串
         :param p: 匹配模式串
         :return:
         """
        sLen = len(s)
        pLen = len(p)

        i = 0
        j = 0

        while i < sLen and j < pLen:
            if s[i] == p[i]:
                i += 1
                j += 1
            else:
                j = 0
                i = i - j + 1
        if j == pLen:
            return i - j
        else:
            return -1

    def kmp2(self, s, p):
        """
        根据next数组求解
        :param s:
        :param p:
        :return:
        """
        sLen = len(s)
        pLen = len(p)

        i = 0
        j = 0

        next_arr = self.get_next(p)
        while i < sLen and j < pLen:
            if s[i] == p[i]:
                i += 1
                j += 1
            else:
                j = next_arr[j]
        if j == pLen:
            return i - j
        else:
            return -1

    def get_next(self, p):
        next_arr = [-1]
        pLen = len(p)
        k = -1
        j = 0
        while j < pLen-1:
            if k == -1 or p[k] == p[j]:
                j += 1
                k += 1
                next_arr.append(k)
            else:
                k = next_arr[k]
        return next_arr


if __name__ == '__main__':
    p = 'abcdabd'
    kmp = KMP()
    arr = kmp.get_next(p)