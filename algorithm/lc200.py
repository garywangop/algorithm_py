from collections import deque
from typing import List


class Solution:
    def is_valid(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == '1'

    def helper(self, grid, row, col):
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        q.append((row, col))
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                for dir in DIR:
                    next_row, next_col = cur[0] + dir[0], cur[1] + dir[1]
                    if self.is_valid(grid, next_row, next_col):
                        q.append((next_row, next_col))
                        grid[next_row][next_col] = '0'


    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    res += 1
                    self.helper(grid, i, j)

        return res

if __name__ == '__main__':
    sol = Solution()
    grid1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(1 == sol.numIslands(grid1))
