from collections import defaultdict


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        l, res = defaultdict(int), 0
        for i in s:
            cur_max = l[i] + 1
            for j in range(-k, k + 1):
                cur = chr(ord(i) + j)
                if 'a' <= cur <= 'z' and j != 0:
                    cur_max = max(l[cur] + 1, cur_max)
            l[i] = cur_max
            res = max(res, l[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(4 == sol.longestIdealString("acfgbd", 2))
    print(4 == sol.longestIdealString("aaaa", 2))