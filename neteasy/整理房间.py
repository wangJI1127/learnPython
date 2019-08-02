"""

又到了周末，小易的房间乱得一团糟。
他希望将地上的杂物稍微整理下，使每团杂物看起来都紧凑一些，没有那么乱。
地上一共有n团杂物，每团杂物都包含4个物品。第i物品的坐标用(ai,bi)表示，小易每次都可以将它绕着(xi,yi)逆时针旋转，这将消耗他的一次移动次数。
如果一团杂物的4个点构成了一个面积不为0的正方形，我们说它是紧凑的。
因为小易很懒，所以他希望你帮助他计算一下每团杂物最少需要多少步移动能使它变得紧凑。

输入描述:

第一行一个数n(1 <= n <= 100)，表示杂物的团数。
接下来4n行，每4行表示一团杂物，每行4个数ai, bi，xi, yi, (-104 <= xi, yi, ai, bi <= 104)，表示第i个物品旋转的它本身的坐标和中心点坐标。


输出描述:

n行，每行1个数，表示最少移动次数。


输入例子1:

4
1 1 0 0
-1 1 0 0
-1 1 0 0
1 -1 0 0
1 1 0 0
-2 1 0 0
-1 1 0 0
1 -1 0 0
1 1 0 0
-1 1 0 0
-1 1 0 0
-1 1 0 0
2 2 0 1
-1 0 0 -2
3 0 0 -2
-1 1 -2 0


输出例子1:

1
-1
3
3


例子说明1:

对于第一团杂物，我们可以旋转第二个或者第三个物品1次。


"""

"""
作者：incoging
链接：https://www.nowcoder.com/questionTerminal/c32f4c74446541a1ad2abbe54476681f?orderByHotValue=1&page=1&onlyReference=false
来源：牛客网

1. 顺时针
(x, y)绕(0, 0)顺时针转90度后坐标为(y, -x)
所以i[0], i[1] 绕x,y顺时针旋转90度，先把原点移动到x,y处，(i[0] - x, i[1] - y)
绕（0， 0）点顺时针旋转90度后是(i[1] - y, x - i[0])，
再将坐标换回到原来的位置，有(i[1] - y + x, x - i[0] + y)

2. 逆时针
(x, y)绕(0, 0)逆时针转90度后坐标为(-y, x)
所以i[0], i[1] 绕x,y顺时针旋转90度，先把原点移动到x,y处，(i[0] - x, i[1] - y)
绕（0， 0）点逆时针旋转90度后是(y - i[1], i[0] - x)，
再将坐标换回到原来的位置，有(y - i[1] + x, i[0] - x + y)
"""

"""
枚举4个点的所有状态，依此进行组合， 判断是否为正方形，
"""
def roate(x1, y1, x2, y2):
    # x1,y1 绕 x2，y2节点逆时针旋转90度
    return y2 - y1 + x2, x1 - x2 + y2
    # x1,y1 绕 x2，y2节点顺时针旋转90度
    # return y1-y2+x2, x2-x1+y2


def dis(x1, y1, x2, y2):
    # 两点之间距离公式
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def change(i, x, y):
    return [x + y - i[1], y - x + i[0]]


def dis1(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def isSquare(a, b, c, d):
    dist = [dis1(a, b), dis1(a, c), dis1(a, d), dis1(b, c), dis1(b, d), dis1(c, d)]
    dist.sort()
    if dist[0] != 0 and dist[0] == dist[1] and dist[1] == dist[2] and dist[2] == dist[3] and dist[4] == dist[5] \
            and dist[0] * 2 == dist[5]:
        return True
    else:
        return False


# 读入一个整数
n = int(input())
for w in range(n):
    best = 100
    p = []
    for i in range(4):
        # 读入一行整数
        hang = list(map(int, input().split()))
        temp1 = [[hang[0], hang[1]]]
        for j in range(3):
            # 存储一个点的4个位置
            temp1.append(change(temp1[-1], hang[2], hang[3]))
        p.append(temp1)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if isSquare(p[0][i], p[1][j], p[2][k], p[3][l]):
                        best = min(best, i+j+k+l)
    if best == 100:
        print(-1)
    else:
        print(best)
