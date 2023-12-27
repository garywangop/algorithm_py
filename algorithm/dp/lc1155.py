"""
这是一个标准的DP题
以n = 2， k = 6， target = 7举例:
n\target 0 1 2 3 4 5 6 7
1        0 1 1 1 1 1 1 1
2        0 0 1 2 3 4 5 6

最后的结果就是右下角的那个count
通过观察可以知道，对n = i时，我只需要知道n = i - 1时每个target的count是多少就行了
当n = i时，每个target value我只用考虑一个dice，每个dice的value m我只能选[1, k]，那么当前target value的count就是sum(i - 1层的count(target_value - m))
dp[i][j] = sum(
    m in [1, k]
        dp[i - 1][j - m]
    )

这个二维DP是可以优化的，我们要计算当前层的话只需要知道上层是什么，所以该二维DP完全可以用一维DP来解决
"""


def numRollsToTarget(n: int, k: int, target: int) -> int:
    mod = 10 ** 9 + 7
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        next_dp = [0] * (target + 1)
        for j in range(i, target + 1):
            for k in range(1, k + 1):
                if j - k >= 0:
                    next_dp[j] = (next_dp[j] + dp[j - k]) % mod
        dp = next_dp

    return dp[target]

"""
Recusion的解法也很有意思，recursion里运用了memoization
每次摇一个dice，dice的value为[0, k]
通过观察可以发现其中有大量重复的运算，所以可以利用memoization避免重复运算
重复运算发生于(n, target)
"""
def numRollsToTarget_recursion(n: int, k: int, target: int) -> int:
    mod = 10 ** 9 + 7
    cache = {}

    def count(n, target):
        if n == 0:
            return 1 if target == 0 else 0

        if (n, target) in cache:
            return cache[(n, target)]

        res = 0
        for i in range(1, k + 1):
            res = (res + count(n - 1, target - i)) % mod
        cache[(n, target)] = res
        return res

    return count(n, target)


if __name__ == '__main__':
    print(numRollsToTarget(1, 6, 3) == 1)
    print(numRollsToTarget(2, 6, 7) == 6)
    print(numRollsToTarget(2, 6, 8) == 5)
    print(numRollsToTarget(30, 30, 500) == 222616187)

    print(numRollsToTarget_recursion(1, 6, 3) == 1)
    print(numRollsToTarget_recursion(2, 6, 7) == 6)
    print(numRollsToTarget_recursion(2, 6, 8) == 5)
    print(numRollsToTarget_recursion(30, 30, 500) == 222616187)
