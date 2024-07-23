import collections
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        m = collections.Counter(nums)
        sorted_key = sorted(m, key=lambda x: (m[x], -x))
        res = []
        for i in sorted_key:
            l = [i for _ in range(m[i])]
            res.extend(l)
        return res


if __name__ == '__main__':
    sol = Solution()
    print([3,1,1,2,2,2] == sol.frequencySort([1,1,2,2,2,3]))
    print([1,3,3,2,2] == sol.frequencySort([2,3,1,3,2]))