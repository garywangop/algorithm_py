class Solution:
    '''
    非常有意思的一道题
    通过读题可以发现我们只关注字母出现的次数是奇数还是偶数，所以就可以用bit operation来做。
    用abcde来代表aeiou出现的是奇数还是偶数
    1. 奇数时，设为1
    2. 偶数是，flip成0
    把abcde存到一个map里，当map中出现一样的key时，我们就知道当前idx和map里的idx之间就是我们要的结果
    因为要求最大值，所以只需要存最早的那个abcde就行
    '''
    def findTheLongestSubstring(self, s: str) -> int:
        idx = {0: -1}
        res = 0
        vowels = "aeiou"
        state = 0
        for i in range(len(s)):
            cur = vowels.find(s[i])
            if cur > 0:
                state ^= 1 << (4 - cur)
            if state not in idx:
                idx[state] = i
            res = max(res, i - idx[state])

        return res


if __name__ == '__main__':
    sol = Solution()
    s1 = "eleetminicoworoep"
    print(13 == sol.findTheLongestSubstring(s1))