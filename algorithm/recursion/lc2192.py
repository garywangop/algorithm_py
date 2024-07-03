from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        if edges is None or len(edges) == 0:
            return []

        def build(arr):
            res = [[] for _ in range(n)]
            for i, j in arr:
                res[i].append(j)
            return res

        path = build(edges)
        res = [set() for _ in range(n)]

        def dfs(m, cur, cur_path):
            cur_path.add(cur)
            for next in m[cur]:
                dfs(m, next, cur_path)
                for i in cur_path:
                    res[next].add(i)
            cur_path.remove(cur)

        for i in range(n):
            dfs(path, i, set())
        res = [list(i) for i in res]
        print(res)
        return res


if __name__ == '__main__':
    sol = Solution()
    n1, edgeList1 = 8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    print([[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]] == sol.getAncestors(n1, edgeList1))

    n2, edgeList2 = 5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    print([[],[0],[0,1],[0,1,2],[0,1,2,3]] == sol.getAncestors(n2, edgeList2))