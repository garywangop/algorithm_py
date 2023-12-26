from typing import List


class Solution:
    """
    DP
    建立一个length为len(s) + 1的dp list, dp[i]代表[0, i)的切法数量。所以最后要return的是dp[len(s)]
    解法：
    dp[i]是多少，其实只需要看dp[i - 1]和dp[i - 2]是多少，dp[i] = dp[i - 1] + dp[i - 2]
    对s[i]来说，只有两种组合方式：
        1. 如果s[i]不是0，可以自己组合，那么组合的数量就是dp[i - 1]了
        2. 如果s[i - 1, i + 1]不是'00'且小于26，那么组合的数量就是dp[i - 2]
    每次算完dp[i]之后看看dp[i]是不是0，如果是0那就证明当前无法切了，那之后也就没必要继续看了

    Note:
        为什么dp list的长度要比s的长度多1？
        如果不这样建立的话，s中的前两位要写好几个if才能给dp[0], dp[1]赋值
    """
    def numDecodings_dp(self, s: str) -> int:
        if s[0] == '0':
            return 0

        # dp[i]: 到index i的切法数量
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = dp[1] = 1

        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if s[i - 2] != "0" and "00" < s[i - 2:i] <= "26":
                dp[i] += dp[i - 2]

            if dp[i] == 0:
                return 0

        return dp[len(s)]

    """
    DFS的方法就不多说了，非常常规的DFS，只是要注意在切割string的时候注意一下别切到index外面去了
    """
    def numDecodings(self, s: str) -> int:
        # return self.dfs(s, 0, [])
        return self.dfs(s, 0)

    def dfs(self, s: str, index: int) -> int:
        if index >= len(s):
            return 1

        count = 0
        for i in range(2):
            if self.is_valid(s, index, index + i + 1):
                count += self.dfs(s, index + i + 1)
        return count

    def is_valid(self, s: str, start: int, end: int):
        return s[start] != "0" and end <= len(s) and int(s[start:end]) <= 26

    def test(self, l: List[int]):
        return 'abc'


if __name__ == '__main__':
    sol = Solution()
    # print(sol.numDecodings('06'))
    # print(sol.numDecodings('12'))
    # print(sol.numDecodings('226'))

    print(sol.numDecodings_dp('06'))
    print(sol.numDecodings_dp('12'))
    print(sol.numDecodings_dp('226'))
