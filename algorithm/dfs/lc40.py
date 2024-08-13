from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(cur, cur_sum, idx):
            if idx == len(candidates):
                if cur_sum == target:
                    res.append(cur[:])
                return

            if cur_sum == target:
                res.append(cur[:])
                return
            if cur_sum > target:
                return

            # add
            cur.append(candidates[idx])
            dfs(cur, cur_sum + candidates[idx], idx + 1)
            cur.pop()
            # don't add. If don't add, we have to skip all the same numbers in order to dedup
            while idx < len(candidates) - 1 and candidates[idx + 1] == candidates[idx]:
                idx += 1
            dfs(cur, cur_sum, idx + 1)

        dfs([], 0, 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    candidates1, target1 = [10, 1, 2, 7, 6, 1, 5], 8
    print(sol.combinationSum2(candidates1, target1))

    candidates2, target2 = [1, 2, 3], 3
    print(sol.combinationSum2(candidates2, target2))