from typing import List

'''
方法一是个比较标准的DP，但是会超时
方法二：
在方法一的基础上，每个元素去找上一排元素最大值这里做了优化
元素不用傻傻的每一个都去计算上一排
只用从左到右再从右到左计算最大值就行了。这样就可以把时间复杂度从row ^ 2降到row 
'''
class Solution:
    def maxPoints1(self, points: List[List[int]]) -> int:
        arr = points[0]
        for i in range(1, len(points)):
            next = [0 for _ in range(len(points[i]))]
            for j in range(len(points[i])):
                cur_max = 0
                for k in range(len(points[i])):
                    cur_max = max(cur_max, arr[k] - abs(k - j))
                next[j] = cur_max + points[i][j]
            arr = next
        return max(arr)

    def maxPoints2(self, points: List[List[int]]) -> int:
        ROW, COL = len(points), len(points[0])
        arr = points[0]
        for i in range(1, ROW):
            left_to_right = [0 for _ in range(COL)]
            left_to_right[0] = arr[0]
            right_to_left = [0 for _ in range(COL)]
            right_to_left[-1] = arr[-1]
            for j in range(1, COL):
                left_to_right[j] = max(arr[j], left_to_right[j - 1] - 1)
            for j in range(COL - 2, -1, -1):
                right_to_left[j] = max(arr[j], right_to_left[j + 1] - 1)
            for j in range(COL):
                arr[j] = points[i][j] + max(left_to_right[j], right_to_left[j])
        return max(arr)


if __name__ == '__main__':
    sol = Solution()
    points1 = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    print(sol.maxPoints2(points1) == 9)
    points2 = [[1, 5], [2, 3], [4, 2]]
    print(sol.maxPoints2(points2) == 11)
    points3 = [[2,2],[2,2],[2,2]]
    print(6 == sol.maxPoints2(points3))
    points4 = [[5,2,1,2],[2,1,5,2],[5,5,5,0]]
    print(13 == sol.maxPoints2(points4))