from typing import List

'''
非常有意思的题目
要算最大数的话首先要第一位是1，这样就可以把每个row都flip到最大
flip column:
遍历all columns，一行行的看，grid[i][j]在flip row的时候是0还是1，可以看grid[i][j]和grid[i][0]是不是一样，如果是一样的话，那就知道grid[i][j]是1
算出column j有多少个0，多少个1，要算最大值的话需要把0 flip成1
'''


def matrixScore(grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])
    res = (1 << (col - 1)) * row

    for j in range(1, col):
        cnt = 0
        val = 1 << (col - j - 1)
        for i in range(row):
            cnt += 1 if grid[i][0] == grid[i][j] else 0
        x = max(cnt, row - cnt)
        res += val * x

    return res


if __name__ == '__main__':
    grid1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(39 == matrixScore(grid1))