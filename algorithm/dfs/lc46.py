from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def swap(nums, a, b):
            nums[a], nums[b] = nums[b], nums[a]

        def dfs(nums, res, index):
            if index >= len(nums):
                res.append(nums[:])
                return

            for i in range(index, len(nums)):
                swap(nums, index, i)
                dfs(nums, res, index + 1)
                swap(nums, index, i)

        dfs(nums, res, 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([0 ,1]))
    print(sol.permute([1]))
    print(sol.permute([1,2,3]))

    s = "abcd"
    print(s[:-1])