from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        path = defaultdict(list)
        for edge in edges:
            path[edge[0]].append(edge[1])
            path[edge[1]].append(edge[0])

        res, min_height = [], float("inf")
        q = deque()
        for start in path:
            cur = 0
            q.append(start)
            visited = set([start])
            while q:
                size = len(q)
                for i in range(size):
                    node = q.popleft()
                    next = path[node]
                    for j in next:
                        if j not in visited:
                            q.append(j)
                            visited.add(j)
                cur += 1
            if cur == min_height:
                res.append(start)
            elif cur < min_height:
                min_height = cur
                res = [start]
        return res


if __name__ == '__main__':
    sol = Solution()
    print([1] == sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))