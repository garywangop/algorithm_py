from typing import List


class Solution:
    """
    解法：
    这题的关键在于怎么找到一个点，这个点和所有的点距离最短。可以先考虑一维的情况
    1 1 0 0 1
    算各个点的average是肯定不对的，通过观察可以发现，所有点的median就是所要的答案。

    怎么找median：
    1. LC答案的方法：
    在遍历grid的时候，只要把横纵坐标存起来就行了，横坐标存的时候就是按顺序存的，纵坐标存完之后顺序是乱的，所以需要sort一下
    当有了排好序的横纵坐标之后，median的index其实就是length / 2

    2. 自己琢磨的方法，有点麻烦
    顺着median的思路继续分析，可以得出在i时，只要左边和右边的sum是一样的那就为median了
    此时回到这个题目，在二维里怎么找median？那么只需要把二维压缩成两个一维就可以了，两个一维的median就是二维里的横纵坐标
    注意：在压缩成一维的时候会出现这样的情况：l = [2, 0, 1]
    此时l[0]为2，可以很轻易的得到坐标0就是median。所以在找median的时候，从坐标0开始，只要left_sum >= right_sum的时候就是median了
    """

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        row_list, col_list = [], []
        res = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    row_list.append(i)
                    col_list.append(j)

        def get_median(l):
            mid = len(l) // 2
            return l[mid]

        col_list.sort()
        median = [get_median(row_list), get_median(col_list)]

        for i in range(len(row_list)):
            res += abs(median[0] - row_list[i]) + abs(median[1] - col_list[i])

        return res


if __name__ == '__main__':
    sol = Solution()
    print(6 == sol.minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
    print(1 == sol.minTotalDistance([[1, 1]]))
