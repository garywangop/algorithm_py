from collections import deque
from typing import List

'''
这个题目很容易就想到要算的sub array length取决于sub array里的最大值和最小值
只要abs(arr[i] - min) <= limit and abs(arr[i] - max) <= limit
那当前的sub array就是符合条件的sub array，那么找到最长的那个sub array就行
问题是，如何有效率的找到sub array里的最大值和最小值呢？

方法一: naive
用一个array记录sub array里的所有元素，然后不停sort新的array就好。这样会超时

方法二：单调栈
这个题目需要用两个单调栈，一个记录最大值的递减栈，一个记录最小值的递增栈
运用sliding window
if abs(arr[i] - min) <= limit and abs(arr[i] - max) <= limit: do nothing
else，要更新l
不断的l++直到abs(arr[i] - min) <= limit and abs(arr[i] - max) <= limit
注意：当移除单调栈里的元素的时候，需要把l之前的元素全部移除，所以单调栈里面不能存value，要存idx，不然没有办法知道只不是l之前的元素
'''


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = res = 0
        min_deque, max_deque = deque(), deque()

        for r in range(len(nums)):
            while l < r and (
                (min_deque and abs(nums[r] - nums[min_deque[0]]) > limit)
                or (max_deque and abs(nums[r] - nums[max_deque[0]]) > limit)
            ):
                l += 1
                if min_deque and min_deque[0] < l:
                    min_deque.popleft()
                if max_deque and max_deque[0] < l:
                    max_deque.popleft()

            while min_deque and nums[min_deque[-1]] > nums[r]:
                min_deque.pop()
            min_deque.append(r)

            while max_deque and nums[max_deque[-1]] < nums[r]:
                max_deque.pop()
            max_deque.append(r)

            res = max(r - l + 1, res)

        return res

    def longestSubarray_naive(self, nums: List[int], limit: int) -> int:
        arr = []
        l = 0
        res = 1
        for r in range(len(nums)):
            while l < r and arr and (abs(arr[0] - nums[r]) > limit or abs(arr[-1] - nums[r]) > limit):
                arr.remove(nums[l])
                l += 1

            arr.append(nums[r])
            arr.sort()
            res = max(res, r - l + 1)

        return res


if __name__ == '__main__':
    sol = Solution()
    nums1, limit1 = [8, 2, 4, 7], 4
    print(2 == sol.longestSubarray(nums1, limit1))

    nums2, limit2 = [10, 1, 2, 4, 7, 2], 5
    print(4 == sol.longestSubarray(nums2, limit2))

    nums3, limit3 = [4, 2, 2, 2, 4, 4, 2, 2], 0
    print(3 == sol.longestSubarray(nums3, limit3))

    nums4, limit4 = [1, 5, 6, 7, 8, 10, 6, 5, 6], 4
    print(5 == sol.longestSubarray(nums4, limit4))
