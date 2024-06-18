from typing import List


class Solution:
    def __init__(self):
        self.DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.res = 0

    def is_valid(self, row, col, grid, visited):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row]) and (row, col) not in visited and grid[row][col] > 0

    def dfs(self, row, col, grid, visited, cur):
        cur += grid[row][col]
        self.res = max(self.res, cur)
        for dir in self.DIR:
            next_row, next_col = row + dir[0], col + dir[1]
            if self.is_valid(next_row, next_col, grid, visited):
                visited.add((next_row, next_col))
                self.dfs(next_row, next_col, grid, visited, cur)
                visited.remove((next_row, next_col))

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    self.dfs(i, j, grid, set([(i, j)]), 0)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    grid1 = [[0,6,0],[5,8,7],[0,9,0]]
    grid2 = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    grid3 = [[0,0,34,0,5,0,7,0,0,0],
             [0,0,0,0,21,0,0,0,0,0],
             [0,18,0,0,8,0,0,0,4,0],
             [0,0,0,0,0,0,0,0,0,0],
             [15,0,0,0,0,22,0,0,0,21],
             [0,0,0,0,0,0,0,0,0,0],
             [0,7,0,0,0,0,0,0,38,0]]
    print(24 == sol.getMaximumGold(grid1))
    print(28 == sol.getMaximumGold(grid2))
    print(38 == sol.getMaximumGold(grid3))