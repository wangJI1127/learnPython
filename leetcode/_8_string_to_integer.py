"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as
 possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
 because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.


"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str.split()) == 0:
            return 0
        s = str.strip().split()[0]
        if ord(s[0]) >= ord('0') and ord(s[0]) <= ord('9'):
            for i in range(1, len(s)):
                if s[i].isdigit() == False:
                    ss = s[:i]
                    if int(ss) < -2 ** 31:
                        return -2 ** 31
                    elif int(ss) > 2 ** 31 - 1:
                        return 2 ** 31 - 1
                    else:
                        return int(ss)
            if int(s) < -2 ** 31:
                return -2 ** 31
            elif int(s) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return int(s)
        elif ((s[0] == '-' or s[0] == '+') and len(s) > 1):
            if ord(s[1]) < ord('0') or ord(s[1]) > ord('9'):
                return 0
            else:
                for i in range(2, len(s)):
                    if s[i].isdigit() == False:
                        ss = s[:i]
                        if int(ss) < -2 ** 31:
                            return -2 ** 31
                        elif int(ss) > 2 ** 31 - 1:
                            return 2 ** 31 - 1
                        else:
                            return int(ss)
                if int(s) < -2 ** 31:
                    return -2 ** 31
                elif int(s) > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                else:
                    return int(s)
        else:
            return 0










