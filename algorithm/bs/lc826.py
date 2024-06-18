from typing import List


class Solution:
    def bs(self, arr, target):
        l, r = 0, len(arr) - 1

        while l < r - 1:
            mid = l + (r - l) // 2
            if arr[mid][0] == target:
                return arr[mid][1]
            elif arr[mid][0] < target:
                l = mid
            else:
                r = mid - 1

        if arr[r][0] <= target:
            return arr[r][1]
        elif arr[l][0] <= target:
            return arr[l][1]

        return 0

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        l = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
        l.sort(key=lambda x: (x[0], -x[1]))

        prev = l[0][1]
        for i in range(1, len(l)):
            l[i][1] = max(prev, l[i][1])
            prev = l[i][1]

        res = 0
        for i in range(len(worker)):
            res += self.bs(l, worker[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    d1, p1, w1 = [2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]
    print(100 == sol.maxProfitAssignment(d1, p1, w1))
    d2, p2, w2 = [85, 47, 57], [24, 66, 99], [40, 25, 25]
    print(0 == sol.maxProfitAssignment(d2, p2, w2))
    d3, p3, w3 = [23, 30, 35, 35, 43, 46, 47, 81, 83, 98], [8, 11, 11, 20, 33, 37, 60, 72, 87, 95], [95, 46, 47, 97, 11, 35, 99, 56, 41, 92]
    print(553 == sol.maxProfitAssignment(d3, p3, w3))