class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        res, cur_cost, l, r = 0, 0, 0, 0

        # sum[l,r] <= maxCost
        while r < len(cost):
            cur_cost += cost[r]

            while cur_cost > maxCost and l <= r:
                cur_cost -= cost[l]
                l += 1

            res = max(res, r - l + 1 if r >= l else 0)
            r += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    s1, t1, maxCost1 = "abcd", "bcdf", 3
    print(3 == sol.equalSubstring(s1, t1, maxCost1))

    s2, t2, maxCost2 = "krrgw", "zjxss", 19
    print(2 == sol.equalSubstring(s2, t2, maxCost2))

    s3, t3, maxCost3 = "abcd", "cdef", 3
    print(1 == sol.equalSubstring(s3, t3, maxCost3))