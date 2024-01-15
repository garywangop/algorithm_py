# from linecache import cache
from functools import cache
from typing import List

# from pip._internal.commands import cache


# from pip._internal import cache


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.res = float("inf")
        cache = {}

        def get_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # @cache
        def helper(worker_idx, visited, cur_sum):
            if worker_idx == len(workers):
                self.res = min(self.res, cur_sum)
                return

            for i in range(len(bikes)):
                if i not in visited:
                    cur_sum += get_distance(workers[worker_idx], bikes[i])
                    visited.add(i)
                    helper(worker_idx + 1, visited, cur_sum)
                    visited.remove(i)

        helper(0, set(), 0)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    print(6 == sol.assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))
    print(4 == sol.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))
    print(4995 == sol.assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]]))
    print(sol.assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]],
                                  [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999],[9,999]]))