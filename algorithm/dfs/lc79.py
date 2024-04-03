from typing import List


class Solution:
    def __init__(self):
        self.direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def dfs(self, board, idx, x, y, target, visited):
        if idx == len(target): return True
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != target[idx] or (x, y) in visited:
            return False

        visited.add((x, y))
        for dir in self.direction:
            row = x + dir[0]
            col = y + dir[1]
            if self.dfs(board, idx + 1, row, col, target, visited):
                return True
        visited.remove((x, y))
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.dfs(board, 0, i, j, word, set()):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(True == sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    print(True == sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    print(False == sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
    print(True == sol.exist([["a"]], 'a'))
