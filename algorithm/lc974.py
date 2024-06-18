from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res, cnt, cur = 0, defaultdict(int), 0
        cnt[0] = 1
        for num in nums:
            cur += num
            cur_mod = cur % k
            if cur_mod in cnt:
                res += cnt[cur_mod]
            cnt[cur_mod] += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    nums1, k1 = [4,5,0,-2,-3,1], 5
    print(7 == sol.subarraysDivByK(nums1, k1))

    nums2, k2 = [5], 9
    print(0 == sol.subarraysDivByK(nums2, k2))