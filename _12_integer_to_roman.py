"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

Example 2:

Input: 4
Output: "IV"

Example 3:

Input: 9
Output: "IX"

Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        q = num // 1000
        b = (num - (q * 1000)) // 100
        s = (num - (q * 1000) - (b * 100)) // 10
        g = (num - (q * 1000) - (b * 100) - (s * 10))
        re = ''
        if q > 0:
            re = re + 'M' * q
        if b > 0:
            if b == 9:
                re = re + 'CM'
            elif b >= 5:
                re = re + 'D' + 'C' * (b % 5)
            elif b == 4:
                re = re + 'CD'
            else:
                re = re + 'C' * b
        if s > 0:
            if s == 9:
                re = re + 'XC'
            elif s >= 5:
                re = re + 'L' + 'X' * (s % 5)
            elif s == 4:
                re = re + 'XL'
            else:
                re = re + 'X' * s
        if g > 0:
            if g == 9:
                re = re + 'IX'
            elif g >= 5:
                re = re + 'V' + 'I' * (g % 5)
            elif g == 4:
                re = re + 'IV'
            else:
                re = re + 'I' * g
        return re


if __name__ == '__main__':
    so = Solution()
    re = so.intToRoman(num=3)

