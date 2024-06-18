from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cnt, cur = {0: -1}, 0
        for idx, num in enumerate(nums):
            cur += num
            cur_mod = cur % k
            if cur_mod in cnt and idx - cnt[cur_mod] > 1:
                return True
            elif cur_mod not in cnt:
                cnt[cur_mod] = idx
        return False


if __name__ == '__main__':
    sol = Solution()
    nums1, k1 = [23,2,4,6,7], 6
    print(True == sol.checkSubarraySum(nums1, k1))

    nums2 , k2 = [23,2,6,4,7], 6
    print(True == sol.checkSubarraySum(nums2, k2))

    nums3, k3 = [23,2,6,4,7], 13
    print(False == sol.checkSubarraySum(nums3, k3))