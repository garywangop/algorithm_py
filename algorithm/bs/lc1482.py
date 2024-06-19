from typing import List

'''
这个题目要用二分搜索来做
要从结果来二分搜索
题目给定了结果的取值范围是[1, 10**9]，所以就可以从这个范围开始搜
正常面试的时候感觉就碰不到这种题目，没有结果的取值范围很难往这个方向上想
'''
class Solution:
    def is_valid(self, arr, day, m, k):
        consective = count = 0
        for i in range(len(arr)):
            if arr[i] > day:
                consective = 0
            else:
                consective += 1

            if consective == k:
                count += 1
                consective = 0
        return count >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        start, end = 1, 10 ** 9
        while start < end:
            mid = start + (end - start) // 2
            if self.is_valid(bloomDay, mid, m, k):
                end = mid
            else:
                start = mid + 1
        return start if self.is_valid(bloomDay, start, m, k) else end


if __name__ == '__main__':
    sol = Solution()
    bloomDay1, m1, k1 = [1, 10, 3, 10, 2], 3, 1
    print(3 == sol.minDays(bloomDay1, m1, k1))

    bloomDay2, m2, k2 = [1, 10, 3, 10, 2], 3, 2
    print(-1 == sol.minDays(bloomDay2, m2, k2))

    bloomDay3, m3, k3 = [7, 7, 7, 7, 12, 7, 7], 2, 3
    print(12 == sol.minDays(bloomDay3, m3, k3))