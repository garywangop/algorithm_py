from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def dfs(index, cur):
            if index == len(digits):
                if cur != "":
                    res.append(cur)
                return

            digit = digits[index]
            for i in range(len(nums[digit])):
                cur += nums[digit][i]
                dfs(index + 1, cur)
                cur = cur[:-1]

        dfs(0, "")
        return res
