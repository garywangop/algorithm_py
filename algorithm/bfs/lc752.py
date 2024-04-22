from collections import deque
from typing import List

"""
蛮有意思的一道题，将来再做做
BFS加限制条件找最短路径
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        if "0000" in deadends or "target" in deadends:
            return -1

        res, q, visited = 0, deque(["0000"]), set(["0000"] + deadends)

        while q:
            size = len(q)
            res += 1
            for _ in range(size):
                cur = q.popleft()
                for idx in range(4):
                    for j in range(-1, 3, 2):
                        num = str((int(cur[idx]) + j) % 10)
                        next = cur[:idx] + num + cur[idx + 1:]
                        if next == target:
                            return res
                        if next not in visited:
                            q.append(next)
                            visited.add(next)

        return -1


if __name__ == '__main__':
    sol = Solution()
    # print(6 == sol.openLock(["0201","0101","0102","1212","2002"], "0202"))
    print(-1 == sol.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))