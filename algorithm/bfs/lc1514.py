import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        def build_graph():
            res = defaultdict(list)
            for i in range(len(edges)):
                edge1, edge2, prob = edges[i][0], edges[i][1], succProb[i]
                res[edge1].append((edge2, prob))
                res[edge2].append((edge1, prob))
            return res

        graph = build_graph()  # graph[i][0] is edge, graph[i][1] is prob
        if graph[start_node] is None or len(graph[start_node]) == 0:
            return 0

        maxheap = [(-y, x) for (x, y) in graph[start_node]]
        heapq.heapify(maxheap)
        visited = set([start_node])
        while maxheap:
            cur = heapq.heappop(maxheap)
            prob, edge = -cur[0], cur[1]
            visited.add(edge)
            if edge == end_node:
                return prob
            for e in graph[edge]:
                if e[0] not in visited:
                    heapq.heappush(maxheap, (-prob * e[1], e[0]))
        return 0


if __name__ == '__main__':
    sol = Solution()
    n1, edges1, succProb1, start1, end1 = 3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2
    print(sol.maxProbability(n1, edges1, succProb1, start1, end1))

    n2, edges2, succProb2, start2, end2 = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2
    print(sol.maxProbability(n2, edges2, succProb2, start2, end2))

    n3, edges3, succProb3, start3, end3 = 3, [[0,1]], [0.5], 0, 2
    print(sol.maxProbability(n3, edges3, succProb3, start3, end3))