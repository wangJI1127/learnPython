"""


小易在学校中学习了关于字符串的理论, 于是他基于此完成了一个字典的项目。

小易的这个字典很奇特, 字典内的每个单词都包含n个'a'和m个'z', 并且所有单词按照字典序排列。

小易现在希望你能帮他找出第k个单词是什么。

输入描述:

输入包括一行三个整数n, m, k(1 <= n, m <= 100, 1 <= k <= 109), 以空格分割。


输出描述:

输出第k个字典中的字符串，如果无解，输出-1。


输入例子1:

2 2 6


输出例子1:

zzaa


例子说明1:

字典中的字符串依次为aazz azaz azza zaaz zaza zzaa


"""

# hang = list(map(int, input().split()))

"""
根据排列组合的知识可以知道，n个'a'和m个'z'只能组成 {\color{Green}C_{n+m}^n } 个字符串，我在这里暂且把{\color{Green}C_{n+m}^n } 
表示为C(n,n+m)吧。先假设第一个字符为'a'，那么剩下n-1个'a'和m个'z'组成的子序列能构成字典中的前C(n-1+m,n-1)个字符串。
然后比较k和C(n-1+m,n-1)，这里有俩种情况：①若k小于等于C(n-1+m,n-1)，就说明第k个字符串是字典里前C(n-1+m,n-1)个中的一个（显然该字符串的
第一个字符必为'a'），所以该问题又可以缩减为在子序列(n-1个'a'和m个'z')找到第k个字符串。②若k大于C(n-1+m,n-1)，就说明结果字符串ans是
以'z'开头的字符串中的第k-C(n-1+m,n-1)个字符串，所以该问题又可以缩减为在子序列(n个'a'和m-1个'z')找到第k-count(n+m-1,m-1)个字符串。
while(n&&m)循环结束后，剩余子序列中只存在"aaa...a"或"zzz...z"的情况，若k不为1则说明无解输出-1，否则在字符串ans后补'a'或'z'，
最后输出ans即可。
--------------------- 
作者：喜欢ctrl的cxk 
来源：CSDN 
原文：https://blog.csdn.net/weixin_42449444/article/details/94563972 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""


def xiaoyi1(hang):
    n = hang[0]
    m = hang[1]
    k = hang[2]
    res = ''
    while n > 0 and m > 0:
        cnt = 1
        # 求排列组合数
        for i in range(1, n):
            cnt *= (n + m - i)
            cnt /= i
            if cnt > k:
                break
        if k <= cnt:
            res += 'a'
            n -= 1
        else:
            res += 'z'
            m -= 1
            k -= cnt
    if k != 1:
        print(-1)
    else:
        while n > 0:
            res += 'a'
            n -= 1
        while m > 0:
            res += 'z'
            m -= 1
        print(res)


def xiaoyi(hang):
    n = hang[0]
    m = hang[1]
    k = hang[2]

    # 动态规划生成字符串，时间复杂度较大，完成度30%
    dp = [[set() for i in range(m + 1)] for j in range(n + 1)]
    dp[0][0] = {''}
    for i in range(1, n + 1):
        dp[i][0] = {'a' * i}
    for i in range(1, m + 1):
        dp[0][i] = {'z' * i}

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = set()
            for a in dp[i][j - 1]:
                s.add(a + 'z')
                s.add('z' + a)
            for z in dp[i - 1][j]:
                s.add(z + 'a')
                s.add('a' + z)
            dp[i][j] = s

    li = list(dp[n][m])
    li.sort()
    if k < 1 or k > len(li):
        print(-1)
    else:
        print(li[k - 1])


if __name__ == '__main__':
    hang = [3, 3, 6]
    xiaoyi1(hang)
    xiaoyi(hang)
