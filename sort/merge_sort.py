class Solution:
    def sort(self, nums):
        return self.merge_sort(nums)

    def merge_sort(self, arr):
        return self.partition(arr, 0, len(arr) - 1)

    def partition(self, arr, left, right):
        if left >= right:
            return [arr[left]]
        mid = left + (right - left) // 2
        left_partition = self.partition(arr, left, mid)
        right_partition = self.partition(arr, mid + 1, right)
        return self.merge(left_partition, right_partition)

    def merge(self, left, right):
        idx1 = idx2 = 0
        res = []
        while idx1 < len(left) and idx2 < len(right):
            if left[idx1] <= right[idx2]:
                res.append(left[idx1])
                idx1 += 1
            else:
                res.append(right[idx2])
                idx2 += 1
        if idx1 < len(left):
            res.extend(left[idx1:])
        if idx2 < len(right):
            res.extend(right[idx2:])
        return res


if __name__ == '__main__':
    sol = Solution()
    arr1 = [2, 1]
    print([1, 2] == sol.sort(arr1))
    arr2 = [5,4,3,2,1]
    print([1,2,3,4,5] == sol.sort(arr2))