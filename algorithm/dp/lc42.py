from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # l2r[i]: max value in range[0, i)
        # r2l[]: max value in range(i, len(height))
        l2r, r2l = [0 for _ in range(len(height))], [0 for _ in range(len(height))]

        for i in range(1, len(height)):
            l2r[i] = max(l2r[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            r2l[i] = max(r2l[i + 1], height[i + 1])

        res = 0

        for i in range(1, len(height) - 1):
            if height[i] < r2l[i] and height[i] < l2r[i]:
                res += min(l2r[i], r2l[i]) - height[i]

        return res


if __name__ == '__main__':
    sol = Solution()
    print(6 == sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))