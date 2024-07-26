import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for v1, v2, dist in edges:
            adj[v1].append((v2, dist))
            adj[v2].append((v1, dist))

        def helper(src):
            heap, visited = [(0, src)], set()
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei, dist2 in adj[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap, (nei_dist, nei))
            return len(visited) - 1

        res, min_count = -1, n
        for src in range(n):
            count = helper(src)
            if count <= min_count:
                res, min_count = src, count
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold = 4
    print(3 == sol.findTheCity(n, edges, distanceThreshold))