from typing import List


class Solution:
    """
    这个题目要用3个指针，分别为
    - index： 当前写入的index
    - left, fast: [left, fast]用来记录需要压缩的区间

    起始状态3个指针都是0
    1. arr[left] == arr[right]: 什么都不做，right++
    2. arr[left] != arr[right]: 确定了需要压缩的区间
        a. 把需要压缩的char写到arr[index] -> arr[index] = arr[left]
        b. 需要压缩的count是: left - right
            - 如果count == 1：无需压缩
            - 如果count > 1，把count变成string然后一个个赋值到arr里去
        c.  压缩结束，left = right

    post processing：最后处理一次[left, right]
        a. 把需要压缩的char写到arr[index] -> arr[index] = arr[left]
        b. 需要压缩的count是: left - right
            - 如果count == 1：无需压缩
            - 如果count > 1，把count变成string然后一个个赋值到arr里去

    最后return的是index
    """

    def compress(self, arr: List[str]) -> int:
        left = right = index = 0

        while right <= len(arr):
            if right == len(arr) or arr[left] != arr[right]:
                arr[index] = arr[left]
                index += 1
                count = str(right - left)
                if count > "1":
                    # for i in range(len(count)):
                    #     arr[index] = count[i]
                    #     index += 1
                    arr[index:index + len(count)] = list(count)
                    index += len(count)
                left = right

            right += 1

        return index


if __name__ == '__main__':
    sol = Solution()
    # print(sol.compress(["a"]))
    # print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))

    l1 = [1,2,3,4,5,6,7]
    l2 = [11,12,13]
    print(list("abc"))
    l1[:len(l2)] = l2
    print(l1)

