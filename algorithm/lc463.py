from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def is_valid(self, grid, row, col, visited):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col] == 1 and (row, col) not in visited

    def helper(self, grid, row, col):
        visited = set([(row, col)])
        q = deque()
        q.append((row, col))
        res = 0
        while q:
            cur = q.popleft()
            # check up
            if cur[0] - 1 < 0 or grid[cur[0] - 1][cur[1]] == 0: res += 1
            # check down
            if cur[0] + 1 == len(grid) or grid[cur[0] + 1][cur[1]] == 0: res += 1
            # check left
            if cur[1] - 1 < 0 or grid[cur[0]][cur[1] - 1] == 0: res += 1
            # check down
            if cur[1] + 1 == len(grid[cur[0]]) or grid[cur[0]][cur[1] + 1] == 0: res += 1
            for dir in self.DIR:
                next_row, next_col = cur[0] + dir[0], cur[1] + dir[1]
                if self.is_valid(grid, next_row, next_col, visited):
                    visited.add((next_row, next_col))
                    q.append((next_row, next_col))
        return res

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return self.helper(grid, i, j)
        return 0


if __name__ == '__main__':
    sol = Solution()
    grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(16 == sol.islandPerimeter(grid1))